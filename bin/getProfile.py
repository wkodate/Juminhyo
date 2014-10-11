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
fsq.requestUser()
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
fb = facebookapi.facebookapi()
fbid = fsq.getFacebookId()
if fbid is not None:
    profile['fbId'] = fbid
    fbuser = fb.getUser(fbid)
    fbName = fb.getName(fbuser)
    profile['fbName'] = fbName
    fbGender = fb.getGender(fbuser)
    profile['fbGender'] = fbGender
    fbLocale = fb.getLocale(fbuser)
    profile['fbLocale'] = fbLocale

# print
for k,v in profile.items():
    print k,v
