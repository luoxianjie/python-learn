#!/usr/bin/python

import pymysql

# 连接mysql数据库

connection = pymysql.connect(host='127.0.0.1',port=3306,user='root',password='',db='lxj',charset='utf8',cursorclass=pymysql.cursors.DictCursor)

# sql

sql = "select * from lxj_user"

cursor = connection.cursor()
cursor.execute(sql)

result = cursor.fetchall()

print(result)