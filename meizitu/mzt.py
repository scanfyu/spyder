from bs4 import BeautifulSoup
import os
from Download import request # 导入模块变了一下
from pymongo import MongoClient
import datetime


class mzitu():

    def __init__(self):
        client = MongoClient() #与MongoDB建立连接（默认本地数据库）
        db = client['meinvxiezhenji'] #选择一个数据库
        self.meizitu_collection = db['meizitu'] #在 meinvxiezhenji 这个数据库中，选择一个集合
        self.title = '' #保存页面主题
        self.url = '' #保存页面地址
        self.img_urls = [] #初始化一个列表保存图片地址

    def all_url(self, url):

        html = request.get(url, 3) ##这儿更改了一下（删掉 self ；3为timeout参数）
        all_a = BeautifulSoup(html.text, 'lxml').find('div', class_='all').find_all('a')
        for a in all_a:
            title = a.get_text()
            self.title = title #将主题保存到self.title中
            print(u'开始保存：', title)
            path = str(title).replace("?", '_')
            self.mkdir(path)
            os.chdir("E:\mzitu\\"+path)
            href = a['href']
            self.url = href #将页面地址保存到self.url中
            if self.meizitu_collection.find_one({'主题页面': href}): #判断主题是否在数据库中
                print(u'这个页面已经爬取过了')
            else:
                self.html(href)

    def html(self, href):
        html = request.get(href, 3)##这儿更改了一下（删掉 self ；3为timeout参数）
        max_span = BeautifulSoup(html.text, 'lxml').find_all('span')[10].get_text()
        page_num = 0 #计数器（判断图片是否下载完毕）
        for page in range(1, int(max_span) + 1):
            page_num += 1 #循环+1 当page_num == max_span时，证明在下最后一张图片
            page_url = href + '/' + str(page)
            self.img(page_url, max_span, page_num) #将上边的两个变量传递给下一个参数

    def img(self, page_url, max_span, page_num): #添加上边传递参数
        img_html = request.get(page_url, 3) ##这儿更改了一下（删掉 self ；3为timeout参数）
        img_url = BeautifulSoup(img_html.text, 'lxml').find('div', class_='main-image').find('img')['src']
        self.img_urls.append(img_url) #每一次 for page in range(1, int(max_span) + 1)获取到的图片地址都会添加到 img_urls这个初始化的列表
        if int(max_span) == page_num: #传递来的两个参数 当max_span和page_num相等时，即为最后一张图片，下载图片并保存至数据库
            self.save(img_url)
            post = {  #构造一个字典
                '标题': self.title,
                '主题页面':self.url,
                '图片地址':self.img_urls,
                '获取时间':datetime.datetime.now()
            }
            self.meizitu_collection.save(post) #将post内容写入数据库
            print(u'插入数据库成功')
        else:   #max_span 不等于 page_num执行下面
            self.save(img_url)

    def save(self, img_url):
        name = img_url[-9:-4]
        print(u'开始保存：', img_url)
        img = request.get(img_url, 3) ##这儿更改了一下（删掉 self ；3为timeout参数）
        f = open(name + '.jpg', 'ab')
        f.write(img.content)
        f.close()

    def mkdir(self, path): 
        path = path.strip()
        isExists = os.path.exists(os.path.join("E:\mzitu", path))
        if not isExists:
            print(u'建了一个名字叫做', path, u'的文件夹！')
            os.makedirs(os.path.join("E:\mzitu", path))
            return True
        else:
            print(u'名字叫做', path, u'的文件夹已经存在了！')
            return False


Mzitu = mzitu() ##实例化
Mzitu.all_url('http://www.mzitu.com/all') ##给函数all_url传入参数  你可以当作启动爬虫（就是入口）