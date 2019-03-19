# 添加用户


# 引入 cgi模块
import cgi, cgitb, pymysql, json, hashlib

# 开启错误提示
cgitb.enable()

# 配置 请求头
print('Content-Type: text/html')
print()

# 1. 连接数据库
db = pymysql.connect('localhost', 'root', '123456', 'p4', charset="utf8mb4")

# 2. 创建游标(指针), 用于操作数据库
cursor = db.cursor(cursor=pymysql.cursors.DictCursor)

# 3. 准备sql:  查询所有的用户
# 3.1 接收参数
data = cgi.FieldStorage()


data_dict = {}
for i in data.keys():
   data_dict[i] = data[i].value





# 3.3 完善数据
# md5加密
# data_dict['pwd'] = hashlib.md5( 二进制 密码字符串 ).hexdigest()
data_dict['pwd'] = hashlib.md5(data_dict['pwd'].encode()).hexdigest()

# 3.3 凑数据格式

data_edit = ''
for k, v in data_dict.items():
    data_edit += '`%s`="%s",' % (k, v)
data_edit = data_edit.strip(',')

# 3.4 准备sql语句
# sql = 'INSERT INTO `user`( ``, ``, ``, ``, ... )  VALUES( "","","","", ...  )';
# sql = 'INSERT INTO `user`( %s )  VALUES( %s )' % (field, values);

sql = 'UPDATE  `user` SET %s WHERE `id` = %s ' % (data_edit, data_dict['id'])
print(sql)
exit()
# 4. 执行sql
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 提交给 mysql 改变数据库 (只有增删改才需要提交,  查询操作不需要)
    db.commit()

    print('添加成功')
except:
    print('添加失败')

# 5. 跳转为 用户列表页
script = '''
    <script>
        setTimeout( function(){
            location.href = './show.py';
        }, 3000)
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




