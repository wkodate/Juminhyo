#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("/Users/wkodate/Develop/Juminhyo/classes")
import scraper
import time

BASE_URL = "http://www.talenttwit.com/tllink/tllink.php?mode=jump&id="
SLEEP_TIME = 1
END_PAGE_NUM = 2

s = scraper.scraper()
for i in range(1, END_PAGE_NUM):
    html = s.getHtml(BASE_URL, i)
    time.sleep(SLEEP_TIME)
    account = s.parseTwLink(html)
    if account is None:
        continue
    print '\t'.join([str(i) for i in account])

