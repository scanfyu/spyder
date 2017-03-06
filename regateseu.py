# -*- coding: utf-8 -*-
# python3
import requests
from bs4 import BeautifulSoup

headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
bash_url = 'https://www.researchgate.net/institution/Southeast_University_China/members/'

url = bash_url + '1'
start_html = requests.get(url, headers=headers)
print(start_html.status_code)
print(start_html.text)