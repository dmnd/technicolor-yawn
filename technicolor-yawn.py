#!/usr/bin/env python

import sys
import re
import io

from termcolor import colored


pattern = """
    ^
    (?P<level>\w+)
    \s+
    (?P<date>\d\d\d\d-\d\d-\d\d)
    \s+
    (?P<time>\d\d:\d\d:\d\d,\d\d\d)
    \s+
    (?P<filename>.*?)
    :
    (?P<line>\d+)
    \]\s
    (?P<message>.*)
    $
    """


def format_line(parsed_line):
    output = ""
    order = ['level', 'date', 'time', 'filename', 'line', 'message']
    groups = {
        'level': {
            'DEBUG': 'blue',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'magenta',
        },
        'date': 'grey',
        'time': 'grey',
        'filename': 'grey',
        'line': 'grey',
        'message': 'white'
    }

    default_colour = 'grey'
    i = 0
    for g in order:
        colour = groups[g]
        if isinstance(colour, dict):
            colour = colour[parsed_line.group(g)]
        output += colored(parsed_line.string[i:parsed_line.start(g)], default_colour)
        output += colored(parsed_line.group(g), colour or default_colour)
        i = parsed_line.end(g)

    output += colored(parsed_line.string[i:], default_colour)
    return output


def suppress_message(message):
    m = message[0]
    level = m.group('level')
    message = m.group('message')
    filename = m.group('filename')
    blacklist = [
        level == "DEBUG" and "KALOG" not in message,
        level == "INFO" and message.startswith('"GET /gae_mini_profiler'),
        level == "INFO" and message.startswith('Saved; key: __appstats__'),
        level == "INFO" and filename == "render.py" and message.startswith('Dynamically loading'),
        level == "INFO" and filename == "render.py" and message.startswith("Compiled"),
    ]
    return any(blacklist)


def output_log(message):
    if suppress_message(message):
        return

    sys.stdout.write(format_line(message[0]))
    for line in message[1:]:
        sys.stdout.write(line)
    sys.stdout.flush()


def read_stream(stream):
    nextline = re.match(pattern, stream.readline(), re.VERBOSE)
    assert nextline

    while True:
        lines = [nextline]
        while True:
            # start of a new log message - read until the end
            line = stream.readline()
            m = re.match(pattern, line, re.VERBOSE)
            lines.append(m or line)
            if m:
                break
        nextline = lines.pop()
        output_log(lines)


def main():
    if len(sys.argv) == 1:
        read_stream(sys.stdin)
    else:
        filename = sys.argv[1]
        with io.open(filename) as s:
            read_stream(s)


if __name__ == '__main__':
    main()
