# Importing base64 library because we'll need it ONLY in case if the proxy
# we are going to use requires authentication
import random


# Start your middleware class
class ProxyMiddleware(object):
    proxypool = []
    i = 0

    def get_ip_pool(self):
        with open('proxy.txt') as inf:
            for proxy in inf:
                self.proxypool.append("https://" + proxy.replace('\n', ''))

    def process_request(self, request, spider):
        self.i += 1
        print(len(self.proxypool))
        if len(self.proxypool) < 400:
            self.get_ip_pool()
        proxy = random.choice(self.proxypool)
        print(proxy)
        request.meta['proxy'] = proxy
        return

    def process_exception(self, request, exception, spider):
        proxy = request.meta['proxy']
        try:
            self.proxypool.remove(proxy)
            print('remove proxy:' + proxy)
        except:
            pass
        finally:
            return

# 中间件配置
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 100,
    'glosbe.middle.ProxyMiddleware': 110,
}