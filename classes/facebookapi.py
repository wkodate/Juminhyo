#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("/Users/wkodate/Develop/Juminhyo/")
import urllib2
import json

# FourSquare API
# https://github.com/mLewisLogic/foursquare

class facebookapi:
    def __init__(self):
        self.baseUrl = "https://graph.facebook.com/"

    def getUser(self, fbid):
        response = urllib2.urlopen(self.baseUrl+fbid)
        return response.read()

    def getName(self, user):
        decodedJson = json.loads(user)
        name = decodedJson['name']
        return name

    def getGender(self, user):
        decodedJson = json.loads(user)
        gender = decodedJson['gender']
        return gender

    def getLink(self, user):
        decodedJson = json.loads(user)
        link = decodedJson['link']
        return link

    def getLocale(self, user):
        decodedJson = json.loads(user)
        locale = decodedJson['locale']
        return locale
