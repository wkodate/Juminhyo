#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("/Users/wkodate/Develop/Juminhyo/")
import secret
import urllib2
import json

# FourSquare API
# https://github.com/mLewisLogic/foursquare

class foursquareapi:
    def __init__(self, account):
        self.account = account
        self.url = "https://api.foursquare.com/v2/users/search?oauth_token=" + secret.fsid['OAUTH_TOKEN'] + '&v=' + '20141005' + '&twitter=' + account
        self.user = None
        self.decodedUser = None
        self.fsUser = False
        self.GENDER      = 'gender'
        self.FIRST_NAME  = 'firstName'
        self.LAST_NAME   = 'lastName'
        self.DESCRIPTION = 'bio'
        self.HOME_CITY = 'homeCity'
        self.FACEBOOK_ID = 'facebook'

        self.user = self.requestUser(self.url)
        self.decodedUser = self.decodeJson(self.user)

    def requestUser(self, url):
        response = urllib2.urlopen(url)
        return response.read()

    def decodeJson(self, jsonReq):
        return json.loads(jsonReq)

    def is4sqUser(self):
        if len(self.decodedUser['response']['results']):
            return True
        return False

    def getGender(self):
        if not self.is4sqUser():
            return
        if not self.GENDER in self.decodedUser['response']['results'][0]:
            return
        gender = self.decodedUser['response']['results'][0][self.GENDER]
        return gender

    def getName(self):
        name = ''
        if not self.is4sqUser():
            return
        if self.FIRST_NAME in self.decodedUser['response']['results'][0]:
            firstName = self.decodedUser['response']['results'][0][self.FIRST_NAME]
            name += firstName
        if self.LAST_NAME in self.decodedUser['response']['results'][0]:
            lastName = self.decodedUser['response']['results'][0][self.LAST_NAME]
            name += ' ' + lastName
        if name is '':
            return
        return name.strip()

    def getDescription(self):
        if not self.is4sqUser():
            return
        if not self.DESCRIPTION in self.decodedUser['response']['results'][0]:
            return
        desc = self.decodedUser['response']['results'][0][self.DESCRIPTION]
        return desc

    def getHomeCity(self):
        if not self.is4sqUser():
            return
        if not self.HOME_CITY in self.decodedUser['response']['results'][0]:
            return
        homeCity = self.decodedUser['response']['results'][0][self.HOME_CITY]
        return homeCity

    def getFacebookId(self):
        if not self.is4sqUser():
            return
        if not self.FACEBOOK_ID in self.decodedUser['response']['results'][0]['contact']:
            return
        fbid = self.decodedUser['response']['results'][0]['contact'][self.FACEBOOK_ID]
        return fbid
