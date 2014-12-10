#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("/Users/wkodate/Develop/Juminhyo/classes")
import re
import twitterapi

argvs = sys.argv
argc = len(argvs)

def printDebug():
    print 'Usage: $ python %s <twitter_account>' % argvs[0]
    quit()

if argc != 2 : 
    printDebug()

LINE_SEPARATOR_PATTERN = re.compile(r'[\r\n|\r|\n]')
account = argvs[1]

t=twitterapi.twitterapi()
friends_statuses = t.getFriends(account);
follower_statuses = t.getFollowers(account);
for fr_s in friends_statuses:
    for fo_s in follower_statuses:
        name = ""
        timezone = ""
        loco = ""
        desc = ""
        if fr_s.id == fo_s.id:
            name = fr_s.screen_name
            if fr_s.time_zone is not None:
                timezone = fr_s.time_zone
            if fr_s.location is not None:
                loco = fr_s.location
            if fr_s.description is not None:
                desc = fr_s.description
                desc = re.sub(LINE_SEPARATOR_PATTERN, '', desc)
            print name+"\t"+timezone+"\t"+loco+"\t"+desc
