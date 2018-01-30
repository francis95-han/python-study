#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import urllib.parse
import urllib.request

ls = os.linesep
local_path = '.\webpage'


def download(url="http://www.baidu.com"):
    try:
        retval = urllib.request.urlopen(url)
    except IOError:
        retval = None
    if retval.geturl():
        urllib.request.urlretrieve(url, local_path)
if __name__ == '__main__':
    website = input('please input the website which you want to grab,if you don\'t input ,this page will be www.baidu.com :')
    if website == '':
        url = "http://www.baidu.com"
    else:
        url = "http://" + website
    print('The webpage which you want to grab is %s' % url)
    download(url)

