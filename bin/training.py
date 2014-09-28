#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("/Users/wkodate/Develop/Juminhyo/classes")

import twitterapi
import classifier

argvs = sys.argv
argc = len(argvs)

def printDebug():
    print 'Usage: $ python %s <account> [male|female|other]' % argvs[0]
    quit()

if argc != 3 : 
    printDebug()
if argvs[2] != 'male' and argvs[2] != 'female' and argvs[2] != 'other':
    printDebug()

account = argvs[1]
sex = argvs[2]
count = 200
dbpath = '/Users/wkodate/Develop/Juminhyo/db/test.db'

t=twitterapi.twitterapi()
statuses = t.getUserTimeline(account, count)
textList=t.getTweets(statuses)
normTextList = []
for s in statuses:
    normTextList.append(t.normalizeTweet(s.text))
cl=classifier.fisherclassifier(classifier.getwords)
cl.setdb(dbpath)
print 'Training ...'
classifier.sampletrain(cl, normTextList, sex)
print 'Success: '+account+' has been trained as '+sex
