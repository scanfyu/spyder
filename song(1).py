import urllib.request
import urllib.parse
import re
import xlwt
import time

def test():
    request = urllib.request.Request("https://www.researchgate.net/institution/Southeast_University_China/members/")
    with urllib.request.urlopen(request) as f:
        str_html = f.read().decode('utf-8')
    name_re = r'name">  <a href="profile/(.*?)" class="display-name"'
    name = re.findall(name_re,str_html)
    print(name)
    return name

if __name__ == '__main__':
    test()
