#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("/Users/wkodate/Develop/Juminhyo/")
import urllib2
import json

# Facebook API

class facebookapi:
    def __init__(self, fbid):
        self.baseUrl = "https://graph.facebook.com/"
        self.user = self.requestUser(self.baseUrl + fbid)
        self.decodedUser = json.loads(self.user)

    def requestUser(self, url):
        response = urllib2.urlopen(url)
        return response.read()

    def decodeJson(self, jsonReq):
        return json.loads(jsonReq)

    def getName(self):
        name = self.decodedUser['name']
        return name

    def getGender(self):
        gender = self.decodedUser['gender']
        return gender

    def getLink(self):
        if not 'link' in self.decodedUser:
            return
        link = self.decodedUser['link']
        return link

    def getLocale(self):
        locale = self.decodedUser['locale']
        return locale
