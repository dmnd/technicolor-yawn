from distutils.core import setup

setup(
    name='technicolor-yawn',
    version='0.1.1',
    author='Desmond Brand',
    author_email='dmnd@desmondbrand.com',
    scripts=['bin/technicolor-yawn'],
    url='https://github.com/dmnd/technicolor-yawn',
    license='LICENSE.txt',
    description='Colours and filters request logs from'
                ' the Google App Engine dev server',
    long_description=open('README.md').read(),
    install_requires=[
        "termcolor >= 1.1.0",
    ],
)
