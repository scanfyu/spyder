# -*- coding: utf-8 -*-
import requests

url = "http://www.baidu.com"

print('第一种方法')
response1 = requests.get(url)
print(response1.status_code)
print(len(response1.text))  #测量网页长度

print('第二种方法')
headers = {'User-Agent':"Mozilla/5.0(Windows NT 6.1; WOW64) AppleWebkit/537.1 (KHTML, like Gecko)Chrome/22.01207.1 Safari/537.1"}
response2 = requests.get(url, headers = headers)
print(response2.status_code)
print(len(response2.text)) #测量网页长度

from urllib import request

resp = request.urlopen(url)

print(resp.read().decode('utf-8'))