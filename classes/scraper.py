#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("../")
import urllib2
from bs4 import *
import re

class scraper:
    def __init__(self):
        pass

    def getHtml(self, url, param=None):
        paramStr = ''
        if (param is not None and isinstance(param, int)):
            paramStr =  str(param)
        c = urllib2.urlopen(url + paramStr)
        return c.read()

    def parseTwLink(self, content):
        soup = BeautifulSoup(content)
        pattern = re.compile(r'on Twitter$')
        anchor = soup.find(name='a', text=pattern)
        if anchor is None:
            return
        name = re.sub(pattern, '', anchor.renderContents()).strip()
        return (name, anchor['href'])

