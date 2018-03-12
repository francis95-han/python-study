#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author zhangbohan.dell@gmail.com
# 学习使用，网络爬虫，爬取新浪网国内新闻
# @create 2018-03-08 9:32
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import json
import re
import pandas


# 获取内容 编辑 评论数等
def getContent(ab):
    result = {}
    res = requests.get(ab, allow_redirects=False)
    # 设置抓取的编码格式为utf-8
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    # 判断页面是否存在
    if soup.select('title')[0].text.strip() != '页面没有找到':
        # 获取编辑
        result['author'] = soup.select(".show_author")[0].text.strip("责任编辑：")
        # 获取文章内容
        #  for p in soup.select('#article p')[2:-2]:
        #     content.append(p.text.strip())
        result['content'] = [p.text.strip() for p in soup.select('#article p')[1:-2]]
        # 获取标题
        result['title'] = soup.select('.main-title')[0].text
        # 获取发表时间
        timesource = soup.select('.date')[0].text
        result['timesource'] = datetime.strptime(timesource, '%Y年%m月%d日 %H:%M')
        # 获取新闻id 常规方法
        # newsid = ab.split('/')[-1].strip('.shtml').strip('doc-i')
        # 获取新闻id 正则表达式匹配
        newsid = re.search("doc-i(.+).shtml", ab).group(1)
        # newsid.group(0)获取所有匹配的内容  newsid.group(1)获取（）内的内容
        # 构建json地址
        commentssourceURL = 'http://comment5.news.sina.com.cn/page/info?version=1&format=json&channel=gn&newsid=comos-' + newsid + '&group=undefined&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=3&t_size=3&h_size=3&thread=1'
        #  用format也可以
        # commentssourceURL = 'http://comment5.news.sina.com.cn/page/info?version=1&format=json&channel=gn&newsid=comos-{}&group=undefined&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=3&t_size=3&h_size=3&thread=1'
        # commentssourceURL.format(newsid)
        commentssource = requests.get(commentssourceURL)
        # 获取json
        jd = json.loads(commentssource.text.strip("var data="))
        result['commentcount'] = jd['result']['count']['total']
        return result


# def grabMain(newsurl='http://news.sina.com.cn/china'):
#     # 网站链接不设置则默认为新浪网国内新闻
#     res = requests.get(newsurl)
#     # 设置抓取的编码格式为utf-8
#     res.encoding = 'utf-8'
#     # print(res.text)
#     # 将抓取到的内容变为DOM
#     soup = BeautifulSoup(res.text, 'html.parser')
#     # 查找css class为news-item的内容
#     header = soup.select('.news-item')
#     for news in header:
#         if len(news.select("h2")) > 0:
#             pass
#             print(news.select('h2'))
#             获取文章标题
#             h2 = news.select('h2')[0].text
#             获取文章地址
#             a = news.select('a')[0]['href']
#             获取文章发表时间
#             timesource = "2018年" + news.select('.time')[0].text
#             time = datetime.strptime(timesource, '%Y年%m月%d日 %H:%M')
#
#             if getContent(a) != {}:
#                 print(h2, a, time)
#                 print(getContent(a))
#             else:
#                 print("******************************")
#         # print(i['href'])
#     print(header)
#     print(soup.text)


def getNewTails(newtail):
    news_total = []
    res = requests.get(newtail)
    # 将res中的除了json外多余的js代码移除掉
    jd = json.loads(res.text.lstrip(' newsloadercallback(').rstrip(');'))
    for i in jd['result']['data']:
        news_total.append(getContent(i['url']))
    return news_total

if __name__ == '__main__':
    # grabMain()
    news_total = []
    url = "http://api.roll.news.sina.com.cn/zt_list?channel=news&cat_1=gnxw&cat_2==gdxw1||=gatxw||=zs-pl||=mtjj&level==1||=2&show_ext=1&show_all=1&show_num=22&tag=1&format=json&page={}&callback=newsloadercallback&_=1520686186491"
    for i in range(1,10):
        newsurl = url.format(i)
        news = getNewTails(newsurl)
        news_total.extend(news)
    df = pandas.DataFrame(news_total)
    df.to_excel('news2.xlsx')