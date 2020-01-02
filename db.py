# -*- coding: UTF-8 -*-
#安装 MYSQL DB for python
import MySQLdb as mdb
import os

current_dir = os.path.dirname(__file__)
#current_dir = 'C:\Users\HCKJ\Desktop\image'

# 创建一个svg文件，文件名为mytxtfile,并向文件写入msg
def text_create(name, msg):
    full_path = current_dir + '%d' % int(name) + '.svg'
    file = open(full_path, 'w')
    file.write(msg)   #msg也就是下面的Hello world!
    # file.close()

# 调用函数创建一个名为mytxtfile的.txt文件，并向其写入Hello world!
#text_create('mytxtfile', 'Hello world!')


con = None
try:
    #连接 mysql 的方法： connect('ip','user','password','dbname') 
    con = mdb.connect('ip','user','password','dbname') 
 
    #所有的查询，都在连接 con 的一个模块 cursor 上面运行的
    cur = con.cursor()
 
    #执行一个查询
    cur.execute("SELECT VERSION()")
    #取得上个查询的结果，是单个结果
    data = cur.fetchone()
    print ("Database version : %s " % data)

    #执行一个查询
    cur.execute("SELECT * FROM open_svg_logos")
    #使用 fetchall 函数，将结果集（多维元组）存入 rows 里面
    rows = cur.fetchall()
 
    #依次遍历结果集，发现每个元素，就是表中的一条记录，用一个元组来显示
    for row in rows:
        id = row[0]
        source = row[3]
        text_create(id, source)
        print(id, source)

finally:
    if con:
        #无论如何，连接记得关闭
        con.close()