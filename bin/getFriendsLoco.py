#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("/Users/wkodate/Develop/Juminhyo/classes")
import twitterapi

argvs = sys.argv
argc = len(argvs)

def printDebug():
    print 'Usage: $ python %s <twitter_account>' % argvs[0]
    quit()

if argc != 2 : 
    printDebug()

account = argvs[1]

t=twitterapi.twitterapi()
#print t.lookupFriendship(account)
friends_statuses = t.getFriends(account);
follower_statuses = t.getFollowers(account);
for fr_s in friends_statuses:
    for fo_s in follower_statuses:
        if fr_s.id == fo_s.id:
            print fr_s.screen_name
            print fr_s.location
