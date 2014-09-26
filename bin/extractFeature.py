#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("../classes")
import twitterapi

argvs = sys.argv
argc = len(argvs)

def printDebug():
    print 'Usage: python %s account' % argvs[0]
    quit()

if argc != 2: 
    printDebug()

account = argvs[1]
count = 200

t=twitterapi.twitterapi()
statuses = t.getUserTimeline(account);
fw = t.getFeaturedWords(statuses)
print fw
