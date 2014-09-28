#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import urllib2
import re
import json
import twitter
import sys
sys.path.append("../")
import secret

class twitterapi:
    def __init__(self):
        self.charEncoding = "utf-8"
        self.keyphraseUrl = "http://jlp.yahooapis.jp/KeyphraseService/V1/extract"
        self.yahooApiAppId = secret.dict['APP_ID']
        self.twitterApi = twitter.Api( 
            consumer_key        = secret.dict['CONSUMER_KEY'],
            consumer_secret     = secret.dict['CONSUMER_SECRET'],
            access_token_key    = secret.dict['ACCESS_TOKEN'],
            access_token_secret = secret.dict['ACCESS_TOKEN_SECRET']
        )

    def verifyCredentials(self):
        return self.twitterApi.VerifyCredentials()

    def getUserTimeline(self, name='wkodate', cnt=20):
        return self.twitterApi.GetUserTimeline(screen_name=name, count=cnt)

    def getSearch(self, tm, cnt=200):
        return self.twitterApi.GetSearch(term=tm, count=cnt)

    def printTweets(self, statuses):
        for s in statuses:
            print s.text.encode(self.charEncoding)

    def getTweets(self, statuses):
        tweets = []
        for s in statuses:
            tweets.append(s.text)
        return tweets

    def removeReply(self, text):
        return re.sub(r'@\w+ ', '', text.encode(self.charEncoding))

    def getFeaturedWords(self, statuses):
        for s in statuses:
            self.extractFeature(s.text)

    def extractFeature(self, text):
        normText = self.normalizeTweet(text)
        sentence = urllib.quote_plus(normText)
        query = "%s?appid=%s&output=%s&sentence=%s" % (self.keyphraseUrl, self.yahooApiAppId, "json", sentence)
        c = urllib2.urlopen(query)
        result = json.loads(c.read())
        if len(result) == 0:
            return
        for k,v in sorted(result.items(), key=lambda x:x[1], reverse=True):
            print k.encode(self.charEncoding)

    def normalizeTweet(self, text):
        # encoding
        encodedText = text.encode(self.charEncoding)
        # remove replied user's name
        rmReply = re.sub(r'@\w+[: | ]', '', encodedText)
        # remove RT
        rmRT = re.sub(r'RT ', '', rmReply)
        # remove urls
        rmUrl = re.sub(r'https?://[\w/:%#\$&\?\(\)~\.=\+\-]+', '', rmRT)
        # remove white space in front and behind
        return rmUrl.strip().decode(self.charEncoding)

def list2String(list):
    return " " . join(list)
