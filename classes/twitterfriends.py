#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

class twitterfriends:
    def __init__(self, st):
        self.LINE_SEPARATOR_PATTERN = re.compile(r'[\r\n|\r|\n]')
        self.name = st.screen_name
        self.loco = ""
        if st.location is not None:
            self.loco = st.location
        self.desc = ""
        if st.description is not None:
            self.desc = st.description
            self.desc = re.sub(self.LINE_SEPARATOR_PATTERN, '', self.desc)

    def getName(self):
        return self.name

    def getLoco(self):
        return self.loco

    def getDesc(self):
        return self.desc
