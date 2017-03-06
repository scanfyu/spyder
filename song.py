import urllib.request
import urllib.parse
import re
import xlwt
import time

def test():
    request = urllib.request.Request("https://www.researchgate.net/institution/Southeast_University_China/members/")
    with urllib.request.urlopen(request) as f:
        str_html = f.read().decode('utf-8')
        fhtml = open('./songyu.html','w')
        fhtml.write(str_html)
        fhtml.close()
    return 'ok'

if __name__ == '__main__':
    test()

