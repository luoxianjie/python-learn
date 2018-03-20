import urllib.request
resp=urllib.request.urlopen('http://www.baidu.com')
html=resp.read()
fhandle=open("./1.html","wb")    #将爬取的网页保存在本地
fhandle.write(html)
fhandle.close()