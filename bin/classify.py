#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("/Users/wkodate/Develop/Juminhyo/classes")

import twitterapi
import classifier

argvs = sys.argv
argc = len(argvs)

def printDebug():
    print 'Usage: python %s <account>' % argvs[0]
    quit()

if argc != 2: 
    printDebug()

account = argvs[1]
count   = 200
dbpath = '/Users/wkodate/Develop/Juminhyo/db/test.db'

t=twitterapi.twitterapi()
print account+' is ...'
statuses = t.getUserTimeline(account, count)
normTextList = []
for s in statuses:
    normTextList.append(t.normalizeTweet(s.text))
textString=twitterapi.list2String(normTextList)

cl=classifier.fisherclassifier(classifier.getwords)
cl.setdb(dbpath)
print cl.classify(textString)

