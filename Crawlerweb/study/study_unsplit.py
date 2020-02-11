#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from urllib.parse import urlunsplit

params_urlunsplit = ('https', 'www.geekdigging.com', 'index.html;people', 'a=1', 'geekdigging')
print(urlunsplit(params_urlunsplit))
