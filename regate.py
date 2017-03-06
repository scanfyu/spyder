# -*- coding: utf-8 -*-
# python3
import urllib.request
import urllib.parse
import requests
import re
import xlwt
import time
from bs4 import BeautifulSoup as bs
from pymongo import MongoClient

class gate():    

    def __init__(self):
        client = MongoClient()  # 与MongoDB建立链接
        db = client['xuezheziliao']  # 选择一个数据库
        self.regate_collection = db['researchgate']  # 在xuezheziliao数据库中选择集合
        self.name = ''  # 保存学者姓名
        self.regateurl = ''  # 保存学者主页
        self.rg = ''  # 保存学者rg值
        self.numbers = ''  # 保存学者相关数据
        self.skills = ''  # 保存学者技能
        self.topics = ''  # 保存学者主题
        self.co_authors = ''  # 保存合作作者
        self.following = ''  # 保存关注者
        self.followers = ''  # 保存被关注者

    #解析获得用户主页姓名
    def test(self, url):

        name = [] 

        starturl = ("https://www.researchgate.net/institution/Southeast_University_China/members/")

        for page in range(1, 40):
            page_url = starturl + str(page)
            request = urllib.request.Request(page_url) #访问主页获得学校人员名单
            with urllib.request.urlopen(request) as f:  #打开并解析网页
                str_html = f.read().decode('utf-8')
            name_re = r'name">  <a href="profile/(.*?)" class="display-name"' #正则式析取姓名
            name1 = re.findall(name_re,str_html)   #存储所有姓名
            name.append(name1)
            time.sleep(3)
            print(name)
            return name

