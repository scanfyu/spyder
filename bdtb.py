#!/usr/bin/python
# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
import Tool

#百度贴吧爬虫类
class BDTB:
 
    #初始化，传入基地址，是否只看楼主的参数
    def __init__(self,baseUrl,seeLZ):
        self.baseURL = baseUrl
        self.seeLZ = '?see_lz='+str(seeLZ)
 
    #传入页码，获取该页帖子的代码
    def getPage(self,pageNum):
        try:
            url = self.baseURL+ self.seeLZ + '&pn=' + str(pageNum)
            #print url
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            return response.read().decode('utf-8')
        except urllib2.URLError, e:
            if hasattr(e,"reason"):
                print u"连接百度贴吧失败,错误原因",e.reason
                return None

    #获得帖子标题
    def getTitle(self):
        page = self.getPage(1)
        pattern = re.compile('<h3 class="core_title_txt.*?>(.*?)</h3>',re.S)
        result = re.search(pattern,page)
        if result:
            print (result.group(1))          #测试输出
            return result.group(1).strip()
        else:
            print 'nothing found'       #测试报错
            return None

    #获取帖子总页数
    def getPageNum(self):
        page = self.getPage(1)
        pattern = re.compile('<li class=="l_reply_num".*?<span.*?>(.*?)</span>',re.S)
        result = re.search(pattern,page)
        if result:
            print result.group(1)          #测试输出
            return result.group(1).strip()
        else:
            return None

    #获取每层楼的内容，传入页面内容
    def getContent(self,page):
        pattern = re.compile('<div id="post_content_.*? class="d_post_content j_d_post_content ">(.*?)</div>',re.S)
        items = re.findall(pattern,page)
        #for item in items:
            #print item
        print self.tool.replace(items[1])

baseURL = 'http://tieba.baidu.com/p/3138733512'
bdtb = BDTB(baseURL,1)
bdtb.getContent(bdtb.getPage(1))


