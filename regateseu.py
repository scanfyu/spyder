# -*- coding: utf-8 -*-
# python3
import os
from proxy import request
from bs4 import BeautifulSoup
import datetime

class regate():
    
    def test(self, url):
        html = request.get(url, 3)
        all_a = BeautifulSoup(html.text, 'lxml').find('href', class_='display-name').find_all('a')
        
