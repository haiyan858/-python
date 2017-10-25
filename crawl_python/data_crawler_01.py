# encoding:utf-8

import urllib2
import re

# usage: download('http://httpstat.us/500')
#
# date : 2017-10-24 17:13 pm

# 捕获异常
# 重试下载
# 设置用户代理
def download(url_str, user_agent='wswp', retries_num=2):
    print 'Downloading:', url_str
    headers = {'User-Agent':user_agent}
    req = urllib2.Request(url_str,headers=headers)
    # print 'req======',req
    try:
        html = urllib2.urlopen(req).read()
    except urllib2.URLError as ex:
        print 'Download error:', ex.reason
        html=None
        if retries_num > 0:
            # 当download函数遇到 5xx 错误码时，将会递归调用函数自身进行重试download
            if hasattr(ex, 'code') and 500 <= ex.code < 600:
                print '-------------retries_num:',retries_num
                return download(url_str, user_agent, retries_num-1)
    return html

# date: 2017-10-24 18:27 pm
#
# usage: crawl_sitemap('http://example.webscraping.com/sitemap.xml')

def crawl_sitemap(url):
    # download the sitemap file
    sitemap = download(url)
    # extract sitemap links
    links = re.findall('<loc>(.*?)</loc>',sitemap)
    for link in links:
        print 'link=====',link
        html = download(link)
        # todo

        

'''
# usage: download_fun('http://httpstat.us/500')
#
# date : 2017-10-24 15:43 pm

# 重试下载
def download_fun(url_str, retries_num=2):
    print 'Downloading:', url_str
    try:
        html = urllib2.urlopen(url_str).read()
    except urllib2.URLError as ex:
        print 'Download error:', ex.reason
        html=None
        if retries_num > 0:
            # 当download函数遇到 5xx 错误码时，将会递归调用函数自身进行重试download
            if hasattr(ex, 'code') and 500 <= ex.code < 600:
                print '-------------retries_num:',retries_num
                return download_fun(url_str, retries_num-1)
    return html
'''

