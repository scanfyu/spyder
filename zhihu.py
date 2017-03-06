# -*- coding: utf-8 -*-
# python3
import urllib.request
import re
import html.parser
import requests
import sys

#reload(sys)
#sys.setdefaultencoding('utf-8')  # 输出的内容

url = "https://daily.zhihu.com/"
# 获取源代码
def getHtml(url):
    header = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    request = urllib.request.Request(url, headers=header)
    response = urllib.request.urlopen(request)
    text = response.read()
    print(text)
    return text

html = getHtml(url)  # 调用