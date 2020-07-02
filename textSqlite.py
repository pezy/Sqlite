# -*- coding = Utf-8 -*-
# @Time : 2020/6/23 22:31
# @Author : 张
# @File : textSqlite.py
# @software : PyCharm

import sqlite3

conn = sqlite3.connect("text.db")  # 连接数据
print("成功打开数据库")
c = conn.cursor()  # 获取游标
c.execute('''create table if not exists company (id integer primary key asc, name text, age integer, address text, salary integer)''')

sql = '''
    insert into company (name,age,address,salary)
     values ("张三",32,"成都",2000);
'''

c.execute(sql)  # 执行sql语句
conn.commit()  # 提交数据库操作
conn.close()  # 关闭数据库
print("成功建表")
