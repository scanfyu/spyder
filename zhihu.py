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
    #print(text)
    return text

# 解析日报链接
def getUrls(html):
    pattern = r'<a href="/story/(.*?)"',re.S  # re.S匹配换行符
    items = re.findall(pattern, html)
    #print(items)
    #return items
    urls = []  # 拼接好的链接
    for item in items:
        urls.append('https://daily.zhihu.com/story/'+item)
        print(urls[-1])  # 列表最末尾元素 去掉重复链接（链接新加入）
    return urls

# 解析日报标题+正文
def getContent(url):
    html = getHtml(url)  # 调用函数
    pattern = r''
    items = re.findall(pattern, html)
    print(items)

    for items in items_withtag:  # 将内容输出为中文
        print items

def characterProcessing(html):
    htmlParser = htmlParser


# 去掉杂志   sub('<.*?>', '',content_tag)  从后边标签 找到第一个 用第二个参数代替

html = getHtml(url)  # 调用

def main():
    url =
    html = getHtml(url)
    urls = 

if __name__ == "__main__":  # 判断文件入口
    main()