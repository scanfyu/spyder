# -*- coding: utf-8 -*-
# python3
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs


html = urlopen("https://www.researchgate.net/institution/Southeast_University_China/members/")

seu = bs(html.read(), "lxml")

namelist = seu.find_all("h5", {"class":"display-name"})
print(namelist)