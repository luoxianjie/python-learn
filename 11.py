#!/usr/bin/python

import re

# match 从字符串开始位置匹配
print(re.match(r'www','www.baidu.com').span())
print(re.match(r'com','www.baidu.com'))

# search 扫描整个字符串并返回第一个成功的匹配

print(re.search(r'com','www.baidu.com').span())

phone = "1234-2354-5689 # 这是注释"

# 删除注释
str = re.sub(r'#.*$','',phone)

print(str)

# 删除非数字
str = re.sub('\D','',phone)

print(str)