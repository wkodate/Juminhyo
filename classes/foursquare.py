#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("/Users/wkodate/Develop/Juminhyo/")
import secret
import urllib2

# FourSquare API
# https://github.com/mLewisLogic/foursquare

url = "https://api.foursquare.com/v2/venues/search?client_id=" + secret.fsid['CLIENT_ID'] + '&client_secret=' + secret.fsid['CLIENT_SECRET'] + '&v=' + '20141005' + '&q&ll=35.6,139.7'
response = urllib2.urlopen(url)
print response.read()

