Technicolor Yawn
================

![](http://24.media.tumblr.com/tumblr_m1x0br1mTD1r9ljkmo1_500.gif)

Technicolor Yawn colours and filters the request logs from the Google App
Engine dev server. It's pretty rough at the moment and still contains Khan
Academy specific stuff.

To install:

    pip install technicolor-yawn

Usage:

    dev_appserver.py --debug /path/to/your/app 2>&1 | technicolor-yawn

Then your log will look something like this:

![](http://i.imgur.com/95PxJCF.png)
