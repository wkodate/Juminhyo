#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("/Users/wkodate/Develop/Juminhyo/classes")
import twitterfriends
import twitterapi

def printDebug():
    print 'Usage: $ python %s <twitter_account>' % argvs[0]
    quit()

def isFriend(followId, followerId):
    return True if followId == followerId else False

argvs = sys.argv
argc = len(argvs)

if argc != 2 : 
    printDebug()

account = argvs[1]
BOT_DICT_FILE = '/Users/wkodate/Develop/Juminhyo/conf/botDict_desc.txt'

# bot辞書取得
dic = []
f = open(BOT_DICT_FILE, 'r')
for line in f:
    dic.append(line.rstrip())
f.close()

t=twitterapi.twitterapi()
friends_statuses = t.getFriends(account);
follower_statuses = t.getFollowers(account);
for fr_s in friends_statuses:
    for fo_s in follower_statuses:
        # フォローかつフォロワーの場合
        if(not isFriend(fr_s, fo_s)):
            continue
        tf = twitterfriends.twitterfriends(fr_s)
        print tf.getName()+"\t"tf.getLoco()+"\t"+tf.getDesc()
