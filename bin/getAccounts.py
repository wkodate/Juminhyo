#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("/Users/wkodate/Develop/Juminhyo/classes")
import scraper
import twitterapi
import time
import re

BASE_URL = "http://www.talenttwit.com/tllink/tllink.php?mode=jump&id="
SLEEP_TIME = 1
# TODO 引数から指定
START_PAGE_NUM = 1
END_PAGE_NUM = 2
LINE_SEPARATOR_PATTERN = re.compile(r'[\r\n|\r|\n]')

s = scraper.scraper()
for i in range(START_PAGE_NUM, END_PAGE_NUM):
    html = s.getHtml(BASE_URL, i)
    time.sleep(SLEEP_TIME)
    account = s.parseTwLink(html)
    if account is None:
        continue
    t = twitterapi.twitterapi()
    statuses = t.getUserTimeline(name=account[1], cnt=1)
    # 非公開設定対応のときはスキップ
    if statuses == None:
        continue
    desc = statuses[0].user.description.encode('utf-8')
    account.append(re.sub(LINE_SEPARATOR_PATTERN, '', desc))
    print '\t'.join([str(i) for i in account])

