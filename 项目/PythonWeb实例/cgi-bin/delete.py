# -*- coding:utf-8 -*-
# 引入 cgi模块
import cgi,cgitb,pymysql,json
# 开启错误提示
cgitb.enable()

# 配置 请求头
print('Content-Type: text/html')
print()

# 1. 连接数据库
db =pymysql.connect('localhost', 'root', '123456', 'p4', charset="utf8")

# 2. 创建游标(指针), 用于操作数据库
cursor = db.cursor( cursor=pymysql.cursors.DictCursor )

# 3. 准备sql:  查询所有的用户
# 3.1 接收参数
data = cgi.FieldStorage()

# 3.2 准备sql语句
sql = 'DELETE FROM  `user`   WHERE `id`  = %s  ' % data['id'].value

# 4. 执行sql
try:
    # 执行SQL语句 
    cursor.execute(sql)
    # 提交给 mysql 改变数据库 (只有增删改才需要提交,  查询操作不需要)
    db.commit()   

    print('删除成功')  
except:
    print('删除失败')


# 5. 跳转为 用户列表页
script = '''
    <script>
        setTimeout( function(){
            location.href = './show.py';
        }, 1)
    </script>
    
    <!--
        重定向
        <meta http-equiv="refresh" content="秒数; url=地址" />
    -->
'''
print(script)

# 6. 关闭游标 和 数据库
cursor.close()
db.close()




