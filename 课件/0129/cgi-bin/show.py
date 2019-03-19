# 引入 cgi模块
import cgi,cgitb,pymysql,json

# 配置 请求头
print('Content-Type: text/html')
print()

# 1. 连接数据库
db =pymysql.connect('localhost', 'root', '123123', 'p4', charset="utf8")

# 2. 创建游标(指针), 用于操作数据库
cursor = db.cursor()

# 3. 准备sql:  查询所有的用户
sql = 'select id, nickname, tel, sex, address from user'

# 4. 执行sql
cursor.execute(sql)

# 5. 获取数据	
# print(cursor.fetchone())
# print(cursor.fetchone())
# print(cursor.fetchone())
# print(cursor.fetchone())
# print(cursor.fetchone())
# print(cursor.fetchone())
# print(cursor.fetchone())
# print(cursor.fetchone())
# print(cursor.fetchone())
# print(cursor.fetchone())
# print(cursor.fetchone())
# print(cursor.fetchone())
# print(cursor.fetchone())
# print(cursor.fetchone())
# print(cursor.fetchone())
# print(cursor.fetchone())

# res = cursor.fetchone()
# while res:
# 	print(res)
# 	res = cursor.fetchone()

# res = cursor.fetchall()
# print(res)
# for i in res:
# 	print(i)


# 将获取到的数据 以 HTML 方式来打印
res = cursor.fetchall()


tr = ''
for i in res:
	tr += '<tr align="center">'
	tr += '<td> %s </td>' % i[0]
	tr += '<td> %s </td>' % i[1]
	tr += '<td> %s </td>' % i[2]
	tr += '<td> %s </td>' % i[3]
	tr += '<td> %s </td>' % i[4]
	tr += '<td> <a href="">详情</a> <a href="">编辑</a>  <a href="">删除</a> </td>' 
	tr += '</tr>'

html = '''
<!DOCTYPE html>
<html lang="en">
<head>
	<title>用户列表</title>
</head>
<body>
	<table border="1" width="800" height="400" cellspacing="0">
		<tr>
			<th>编号</th>
			<th>昵称</th>
			<th>电话</th>
			<th>性别</th>
			<th>住址</th>
			<th>操作</th>
		</tr>
		'''+tr+'''
	</table>

</body>
</html>
'''

print(html)








