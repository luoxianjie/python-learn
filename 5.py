#! -*- coding: utf-8 -*-

# python 爬取网站图片

import urllib
import re

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = 'src="(.+?\.jpg)" '
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    x = 0
    for imgurl in imglist:
        urllib.urlretrieve(imgurl, './photo/%s.jpg' % x)
        x+=1
    return imglist

# html = getHtml()
# imglist =  getImg(html)

# print imglist

