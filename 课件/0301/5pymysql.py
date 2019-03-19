import pymysql

try:
    # 连接数据库
    db = pymysql.connect(host="127.0.0.1",user="root",database='p4',password="123456",port=3306,charset="utf8",cursorclass=pymysql.cursors.DictCursor)
    # 创建游标
    cursor = db.cursor()
    print('连接成功')
except:
    print('连接失败')

# 执行sql
# 添加数据
sql = 'insert into user values(2,"zhansgan") on duplicate key update name="123"'
# cursor.execute(sql)
# db.commit()
# print(cursor.fetchall())
# db.close()
# CREATE TABLE `user`(
#     id int(10) not null auto_increment primary key,
#     name char(30)
# ) default charset=utf8

# https://xueqiu.com/hq#exchange=US&firstName=3&secondName=3_0
# sql 语句
# python基础