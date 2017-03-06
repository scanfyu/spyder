import scrapy   # 导入scrapy包
from bs4 import BeautifulSoup as bs
from scrapy.http import Request   # 请求模块，跟进URL列表



class GateSpider(scrapy.Spider):

    name = "regate"
    allowed_domains = ["researchgate.net"]
    bash_url = 'https://www.researchgate.net/institution/Southeast_University_China/members/'
    bash_gate = 'https://www.researchgate.net/'

    def start_requests(self):
        for i in range(1, 40):
            url = self.bash_url + str(i)   # 拼接后找到所有members页面
            yield Request(url, self.parse)


    def parse(self, response):
        urls = bs(response.text, 'lxml').find_all('h5', class_='ga-top-coauthor-name')
        for url in urls:
            gate = url.find('a')['href']   # 所有用户地址后缀
            regate = self.bash_gate + gate   # 访问所有用户主页
            yield Request(regate, callback=self.get_gate, meta={'gateurl': regate})

    def get_gate(self, response):
        item = RegateItem()
        item['name'] = bs(response.text, 'lxml').find('a', class_='ga-profile-header-name').get_text()
        item['regateurl'] = response.meta['gateurl']
        try:
            item['target'] = response.xpath('//*[@id="target-sciences"]').extract()  # 提取用户研究方向
            item['rg'] = response.xpath('//*[@id="rgw9_58bbc8168883c"]').extract()  #提取用户rg值
            item['numbers'] = response.xpath('//*[@id="rgw13_58bbc8168883c"]/ul').extract()  # 提取所有研究成果数据
            item['topics'] = response.xpath('//*[@id="rgw30_58bbc8168883c"]/ul').extract()  # 提取所有Topics文字
            item['skills'] = response.xpath('//*[@id="rgw41_58badb37075d4"]/div/ul').extract()  # 提取所有Skills文字
            item['co_authors'] = response.xpath('//*[@id="rgw74_58badb37075d4"]/div/div/ul').extract()  # 提取所有合作作者 未去重
            item['following'] = response.xpath('//*[@id="rgw80_58badb37075d4"]/@href')  # 提取关注者链接
            item['followers'] = response.xpath('//*[@id="rgw92_58badb37075d4"]/@href')  # 提取被关注者链接
            return item
        except:
            item['target'] = None
            item['rg'] = None
            item['research'] = None
            item['articles'] = None
            item['conference'] = None
            item['reads'] = None
            item['citation'] = None
            item['topics'] = None
            item['skills'] = None
            item['co_authors'] = None
            item['following'] = None
            item['followers'] = None
            return item

# 访问项目
class RegateItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()  # 用户姓名
    regateurl = scrapy.Field()  # 用户主页
    target = scrapy.Field()  # 用户专业
    rg = scrapy.Field()  # 用户rg值
    numbers = scrapy.Field()  # 用户数据 研究数-文章-论文-阅读-被引
    skills = scrapy.Field()  # 技能特长
    topics = scrapy.Field()  # 关注主题
    co_authors = scrapy.Field()  # 合作作者
    following = scrapy.Field()  # 关注姓名
    followers = scrapy.Field()  # 被关注姓名