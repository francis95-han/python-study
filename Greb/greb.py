# !/usr/bin/env python3
# -*- coding: utf-8 -*-
""" @author zhangbohan.dell@gmail.com
    @create 2018-03-08 9:32
    @function 爬取新浪网国内新闻的爬虫"""
from datetime import datetime
import re
import json
import requests

from bs4 import BeautifulSoup
import pandas
import pymysql
from sqlalchemy import create_engine


def get_content(web_url):
    """
    :param web_url: 获取主要内容，编辑、日期时间、标题、正文
    :return: 一个存储有以上内容的字典
    """
    result = {}
    res = requests.get(web_url, allow_redirects=False)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    if soup.select('title')[0].text.strip() != '页面没有找到':
        result['author'] = soup.select(".show_author")[0].text.strip("责任编辑：")
        result['content'] = ' '.join([p.text.strip() for p in soup.select('#article p')[1:-2]])
        result['title'] = soup.select('.main-title')[0].text
        timesource = soup.select('.date')[0].text
        result['timesource'] = datetime.strptime(timesource, '%Y年%m月%d日 %H:%M')
        newsid = re.search("doc-i(.+).shtml", web_url).group(1)
        comments_source_url = 'http://comment5.news.sina.com.cn/page/info?version=1' \
                              '&format=json&channel=gn&newsid=comos-{}&group=undefined&' \
                              'compress=0&ie=utf-8&oe=utf-8&page=1&page_size=3&t_size=3&' \
                              'h_size=3&thread=1'
        comments_source = requests.get(comments_source_url.format(newsid))
        jd_temp = json.loads(comments_source.text.strip("var data="))
        result['commentcount'] = jd_temp['result']['count']['total']
        return result

def get_new_tails(newtail):
    """

    :param newtail: 从api中获取新网网址列表并调用getContent（）函数获取新闻内容
    :return: 一个包含有爬取内容的列表
    """
    news_total = []
    res = requests.get(newtail)
    # 将res中的除了json外多余的js代码移除掉
    jd_temp = json.loads(res.text.lstrip(' newsloadercallback(').rstrip(');'))
    for content in jd_temp['result']['data']:
        news_total.append(get_content(content['url']))
    return news_total


if __name__ == '__main__':
    # grabMain()
    # mysqlconnect()
    # news_total = []
    CONN = pymysql.connect(host='localhost', user='root',
                           password='gj5846gj', db='greb', charset='utf8')
    ENGINE = create_engine('mysql+pymysql://root:+gj5846gj@localhost:3306/greb?charset=utf8',
                           encoding='utf-8')
    for new_url in range(1, 20):
        url = "http://api.roll.news.sina.com.cn/zt_list?channel=news&cat_1=gnxw+&" \
              "cat_2==gdxw1||=gatxw||=zs-pl||=mtjj&level==1||=2&show_ext=1&show_all=1+&" \
              "show_num=22&tag=1&format=json&page={}&callback=newsloadercallback&_=1520686186491"
        newsurl = url.format(new_url)
        news = get_new_tails(newsurl)
        for i in news:
            arr = []
            arr.append(i)
            df = pandas.DataFrame(arr)
            pandas.io.sql.to_sql(df, name='sina', con=ENGINE, if_exists='append', index=False)
    CONN.close()
