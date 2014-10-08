#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("/Users/wkodate/Develop/Juminhyo/classes")
import foursquareapi

argvs = sys.argv
argc = len(argvs)

def printDebug():
    print 'Usage: $ python %s <twitter_account>' % argvs[0]
    quit()

if argc != 2 : 
    printDebug()

account = argvs[1]

fsq=foursquareapi.foursquareapi(account)
user = fsq.getUser()
fbid = fsq.getFacebookId(user)
print '[Facebook]' + fbid
name = fsq.getName(user)
print '[Name]' + name
gender = fsq.getGender(user)
print '[Gender]' + gender
desc = fsq.getDescription(user)
print '[Description]' + desc
homeCity = fsq.getHomeCity(user)
print '[HomeCity]' + homeCity
# TODO key-valueで保存
