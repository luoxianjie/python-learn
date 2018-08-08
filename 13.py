#!/usr/bin/python

import requests


# get 请求
r = requests.get('https://unsplash.com')

# 带参数的get请求
# payload = {'key1':'value1','key2':'value2'}
# r = requests.get('http://httpbin.org/get',params=payload)

# post 请求
# payload = {'key1':'value1','key2':'value2'}
# r = requests.post('https://httpbin.org/post',data=payload)

# 其他请求
# r = requests.put('https://httpbin.org/put')
# r = requests.delete('https://httpbin.org/delete')
# r = requests.head('https://httpbin.org/get')
# r = requests.options('https://httpbin.org/get')


print(type(r))