#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
from bs4 import *
import re

import sys
sys.path.append("../")

class scraper:
    def __init__(self):
        pass

    def getHtml(self, url):
        c = urllib2.urlopen(url+"9258")
        return c.read()

    def parseLink(self, content):
        soup = BeautifulSoup(content)
        pattern = re.compile(r'on Twitter$')
        anchor = soup.find(name='a', text=pattern)
        name = re.sub(pattern, '', anchor.renderContents()).strip()
        return (name, anchor['href'])

