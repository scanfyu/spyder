# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import os

headers = {'User-Agent':"Mozilla/5.0(Windows NT 6.1; WOW64) AppleWebkit/537.1 (KHTML, like Gecko)Chrome/22.01207.1 Safari/537.1"}
all_url = "http://www.mzitu.com/all"   #起始地址
start_html = requests.get(all_url, headers=headers)   #使用get方法获取地址，设置头文件
#print(start_html.text) ##打印出start_html (请注意，concent是二进制的数据，一般用于下载图片、视频、音频、等多媒体内容是才使用concent, 对于打印网页内容请使用text)
Soup = BeautifulSoup(start_html.text, 'lxml')  #解析获取网页
#li_list = Soup.find_all('li')  #找到所有标签并返回列表
#for li in li_list:
    #print(li)
all_a = Soup.find('div', class_='all').find_all('a')  #先查找class为all的div标签，再查找<a>标签
for a in all_a:
    title = a.get_text() #找出a标签的文本
    path = str(title).strip() #去掉空格
    os.makedirs(os.path.join("E:\mzitu", path)) #创建一个存放图片的文件夹
    os.chdir("E:\mzitu\\"+path) #切换到创建的文件夹
    href = a['href'] #取出a标签的href属性
    html = requests.get(href, headers=headers)  #获取各个单个页面地址
    html_Soup = BeautifulSoup(html.text, 'lxml')   #解析单个页面
    max_span = html_Soup.find('div',class_='pagenavi').find_all('span')[-2].get_text() #查找所有<span>标签获取第十个<span>中的文本

    for page in range(1, int(max_span)+1):
        page_url = href + '/' +str(page)        #获得图片页面地址
        img_html = requests.get(page_url, headers=headers)    #传入容器
        img_Soup = BeautifulSoup(img_html.text, 'lxml')
        img_url = img_Soup.find('div', class_='main-image').find('img')['src'] #获得图片地址
        name = img_url[-9:-4]  #取 URL 倒数 4-9 位作为图片名字
        img = requests.get(img_url, headers=headers)
        f = open(name+'.jpg', 'ab') #写入多媒体文件必须加 b 这个参数
        f.close()