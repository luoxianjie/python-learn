#! -*- coding: utf-8 -*-

# python 读取数据库并写入excel

import sys
import json

reload(sys)
sys.setdefaultencoding('utf-8')

import MySQLdb
import xlwt

def output():
    try:
        export_sql = "select args,filename,id from hqjf_export where type='overtime' and status = 0"

        export_results = query(export_sql)

        for export_row in export_results:
            # 参数['部门','年月']
            args = json.loads(export_row[0])

            # 文件名
            filename = export_row[1]

            # id
            id = export_row[2];

            # 部门
            department = args['department']

            # 日期
            date = args['ym']

            sql="select d.department_name,u.nickname,o.ymd,o.overtime \
                from hqjf_overtime as o \
                left join hqjf_user u on u.id = o.uid \
                left join hqjf_department as d on d.department_id = u.department \
                where d.department_id = "+ str(department) +" and left(o.ymd,8) = '"+ str(date) +"-'"

            # 获取结果集
            results = query(sql)

            # 获取字段信息
            workbook = xlwt.Workbook()
            sheet = workbook.add_sheet('Sheet1',cell_overwrite_ok=True)

            title = [u"部门",u"姓名",u"日期",u"加班时数(h)",u"报销金额"]

            # 设置title
            for field in range(0,len(title)):
                sheet.write(0,field,title[field])

            row = 1     # 从第二行开始
            col = 0
            for row in range(1,len(results)+1):
                for col in range(0,len(title)):
                    if col < len(title)-1:
                        sheet.write(row,col,u'%s'%results[row-1][col])
                    else:
                        if results[row-1][col-1] <= 2:
                            sheet.write(row,col,20)
                        else:
                            sheet.write(row,col,10*(results[row-1][col-1]-2)+20)

            workbook.save(r'./'+filename)

            # 修改状态
            update_sql = 'update hqjf_export set status = 1 where id ='+str(id)+' '
            # execa(update_sql)

    except MySQLdb.Error,e:
        print 'MySQL Error %d:%s' %(e.args[0],e.args[1])

def query(sql):
    try:
        conn=MySQLdb.connect(host='db.elecfans.net',user='kaoqing',passwd='5DKn4ypbefPszxrV',db='kaoqing',port=3306,charset='utf8')
        cursor=conn.cursor()
        cursor.execute(sql)
        # cursor.scroll(0,mode='absolute')
        data = cursor.fetchall()
        cursor.close()
        conn.close()

        return data;
    except MySQLdb.Error,e:
        print 'MySQL Error %d:%s' %(e.args[0],e.args[1])

def execa(sql):
    try:
        conn=MySQLdb.connect(host='db.elecfans.net',user='kaoqing',passwd='5DKn4ypbefPszxrV',db='kaoqing',port=3306,charset='utf8')
        cursor=conn.cursor()
        cursor.execute(sql)
        # cursor.scroll(0,mode='absolute')
        # data = cursor.fetchall()
        cursor.close()
        conn.close()

        return ;
    except MySQLdb.Error,e:
        print 'MySQL Error %d:%s' %(e.args[0],e.args[1])

if __name__=="__main__":
    output()