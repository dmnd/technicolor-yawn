Technicolor Yawn colours and filters the request logs from the Google App
Engine dev server. It's pretty rough at the moment and still contains Khan
Academy specific stuff.

Usage:
dev_appserver.py --debug /path/to/your/app 2>&1 | python -u technicolor-yawn.py
