#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("../")
import urllib2
from bs4 import *
import re
import time

class scraper:
    def __init__(self):
        self.RETRY_COUNT_LIMIT = 2
        self.SLEEP_TIME = 1
        self._PATTERN = 'http://twitter.com/'
        self.NAME_REPLACEMENT = re.compile(r'on Twitter$')
        self.TWITTER_HOST = 'http://twitter.com/'
        pass

    def getHtml(self, url, param=None):
        paramStr = ''
        # 受け取ったパラメータを文字列型に置換
        if (param is not None and isinstance(param, int)):
            paramStr =  str(param)
        req = urllib2.Request(url + paramStr)
        retryCount = 0
        while True:
            try:
                if retryCount < self.RETRY_COUNT_LIMIT:
                    response = urllib2.urlopen(req)
                else:
                    break
            except urllib2.URLError, e:
                if e.code == 200:
                    break
                else:
                    # ステータスコードが200以外はリトライ　
                    retryCount += 1
                    time.sleep(self.SLEEP_TIME)
            else:
                return response.read()
        return

    def parseTwLink(self, content):
        soup = BeautifulSoup(content)
        # 正規表現にマッチしたaタグを取得
        anchor = soup.find(name='a', text=self.NAME_REPLACEMENT)
        if anchor is None:
            return
        # 人名を取得
        name = re.sub(self.NAME_REPLACEMENT, '', anchor.renderContents()).strip()
        # アカウント名を取得
        screenName = re.sub(self.TWITTER_HOST, '', anchor['href'])
        return [name, screenName]

