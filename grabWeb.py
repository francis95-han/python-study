# encoding=UTF-8
__author__ = 'love_huan'
from urllib import urlretrieve
import os

ls = os.linesep


def firstNonBlank(lines):
    for eachLine in lines:
        if not eachLine.strip():
            continue
        else:
            return eachLine + ls


def firstLast(webpage):
    f = open(webpage)
    lines = f.readlines()
    f.close()
    print(firstNonBlank(lines))
    lines.reverse()
    print(firstNonBlank(lines))


def download(url="http://www.baidu.com", process=firstLast):
    try:
        retval = urlretrieve(url)[0]
    except IOError:
        retval = None
    if retval:
        process(retval)


if __name__ == '__main__':
    website = raw_input('please input the website which you want to grab,if you don\'t input ,this page will be www.baidu.com :')
    if website == '':
        url = "http://www.baidu.com"
    else:
        url = "http://" + website
    print('The webpage which you want to grab is %s' % url)
    download(url)

