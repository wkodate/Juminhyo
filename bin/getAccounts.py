#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("/Users/wkodate/Develop/Juminhyo/classes")
import scraper

s = scraper.scraper()
baseUrl = "http://www.talenttwit.com/tllink/tllink.php?mode=jump&id="
html = s.getHtml(baseUrl)
account = s.parseLink(html)
print account[0], account[1]

