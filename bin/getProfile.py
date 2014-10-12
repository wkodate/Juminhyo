#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("/Users/wkodate/Develop/Juminhyo/classes")
import foursquareapi
import facebookapi

argvs = sys.argv
argc = len(argvs)

def printDebug():
    print 'Usage: $ python %s <twitter_account>' % argvs[0]
    quit()

if argc != 2 : 
    printDebug()

account = argvs[1]

fsq=foursquareapi.foursquareapi(account)
profile = {}
if not fsq.is4sqUser():
    print account + ' is not 4sq user.'
    quit()
name = fsq.getName()
if name is not None:
    profile['name'] = name
gender = fsq.getGender()
if gender is not None:
    profile['gender'] = gender
desc = fsq.getDescription()
if desc is not None:
    profile['desc'] = desc
homeCity = fsq.getHomeCity()
if homeCity is not None:
    profile['homeCity'] = homeCity

# facebook
fbid = fsq.getFacebookId()
if fbid is not None:
    fb = facebookapi.facebookapi(fbid)
    profile['fbId'] = fbid
    fbName = fb.getName()
    profile['fbName'] = fbName
    fbGender = fb.getGender()
    profile['fbGender'] = fbGender
    fbLocale = fb.getLocale()
    profile['fbLocale'] = fbLocale
    fbLink = fb.getLink()
    if (fbLink is not None): profile['fbLink'] = fbLink

# print
for k,v in profile.items():
    print k,v
