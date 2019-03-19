# 在python中,pymysql 来操作数据库
# 
# 1. 安装pymysql
# 	进入 cmd
# 	输入 pip install pymysql



# 2. python 连接数据库
	# pymysql.connect('主机或IP', '用户名', '密码', '库名', charset='编码')


# 3. 创建游标
	# db对象.cursor()
	# 		参数:
	# 			默认 元组
	# 			cursor=pymysql.cursors.DictCursor  以 字典形式接收

# 4. 执行sql
	# 游标.execute( sql语句 )

# 5. 获取游标数据
	# 游标.fetchone()  	获取一条数据, 以一维元组接收
	# 游标.fetchall() 		获取所有数据, 以二维元组接收
	# 游标.rowcount属性 	获取执行execute()所影响的行数

	# 当 数据全部获取完之后, 再获取, 则返回None


# 6. cgi 接收get 或 post 数据的方法
	# cgi.FieldStorage()

# 7. 开启 cgi 错误提示
	# cgitb.enable()

# 8. python 中另类的 三元运算
# 		true环境 if 条件 else false环境

# 9. 关闭游标
	#游标对象.close()

# 10. 关闭数据库
	# 库对象.close()





