from models import Mydb

# 实例化
mydb = Mydb(host="127.0.0.1",user="root",port=3306,database="py17",password="123456")

# 添加数据
sql = 'insert into user values(null,"zhansgan")'
num = mydb.excute(sql)
print(num)