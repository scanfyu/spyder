# -*- coding: utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bs0bj = BeautifulSoup(html, "lxml")

namelist = bs0bj.find_all('span', {"class":'green'})
for name in namelist:
    print(name.get_text())