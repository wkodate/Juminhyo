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

    def getUser(self):
        response = urllib2.urlopen(self.url)
        return response.read()

    def getGender(self, user):
        decodedJson = json.loads(user)
        gender = decodedJson['response']['results'][0]['gender']
        return gender

    def getName(self, user):
        decodedJson = json.loads(user)
        firstName = decodedJson['response']['results'][0]['firstName']
        lastName = decodedJson['response']['results'][0]['lastName']
        name = firstName + ' ' + lastName
        return name

    def getDescription(self, user):
        decodedJson = json.loads(user)
        desc = decodedJson['response']['results'][0]['bio']
        return desc

    def getFacebookId(self, user):
        decodedJson = json.loads(user)
        fbid = decodedJson['response']['results'][0]['contact']['facebook']
        return fbid

    def getHomeCity(self, user):
        decodedJson = json.loads(user)
        homeCity = decodedJson['response']['results'][0]['homeCity']
        return homeCity
