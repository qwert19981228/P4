# 用户详情页


# 引入 cgi模块
import cgi,cgitb,pymysql,json,time
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

# 用于接收 get 或 post 传递过来的值
data = cgi.FieldStorage()

# print(data)
# print(data['id']) 			# 获取其中一条数据 	
# print(data['id'].name) 		# 获取其中具体的下标
# print(data['id'].value) 	# 获取其中具体的值
# exit()


sql = 'select * from user where id = %s ' % data['id'].value

# 4. 执行sql
cursor.execute(sql)

# 5. 获取数据	
# 将获取到的数据 以 HTML 方式来打印
res = cursor.fetchone()

sex = '男' if res['sex'] == 1 else '女'
status = '激活' if res['status'] == 1 else '禁用'
regtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(res['regtime']))

html = '''
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>用户管理系统</title>

    <link href="../boot/css/bootstrap.min.css" rel="stylesheet">

    <!--[if lt IE 9]>
      <script src="../boot/js/html5shiv.min.js"></script>
      <script src="../boot/js/respond.min.js"></script>
    <![endif]-->
</head>
<body>
    <div class="container">
        <h3> 用户详情 </h3>
        <table class="table table-bordered table-hover table-striped table-condensed">
            <tr>
                <th>编号</th>
                <td>%s</td>
            </tr>
            <tr>
                <th>昵称</th>
                <td>%s</td>
            </tr>
            <tr>
                <th>电话</th>
                <td>%s</td>
            </tr>
            <tr>
                <th>性别</th>
                <td>%s</td>
            </tr>
            <tr>
                <th>生日</th>
                <td>%s</td>
            </tr>
            <tr>
                <th>住址</th>
                <td>%s</td>
            </tr>
            <tr>
                <th>状态</th>
                <td>%s</td>
            </tr>
            <tr>
                <th>注册时间</th>
                <td>%s</td>
            </tr>
        </table>
    </div>
    <script src="../boot/js/jquery.min.js"></script>
    <script src="../boot/js/bootstrap.min.js"></script>
</body>
</html>
''' % (res['id'], res['nickname'], res['tel'], sex, res['birthday'], res['address'], status, regtime)

print(html)








