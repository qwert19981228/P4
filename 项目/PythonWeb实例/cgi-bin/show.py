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
sql = 'select id, nickname, tel, sex, address from user'

# 4. 执行sql
cursor.execute(sql)

# 5. 获取数据	
# 将获取到的数据 以 HTML 方式来打印
# res = cursor.fetchall()
res = cursor.fetchall()

tr = ''
for i in res:
	tr += '<tr align="center">'
	tr += '<td> %s </td>' % i['id']
	tr += '<td> %s </td>' % i['nickname']
	tr += '<td> %s </td>' % i['tel']
	tr += '<td> %s </td>' % ('男' if i['sex'] == 1 else '女')
	tr += '<td> %s </td>' % i['address']
	tr += '''<td> 
		  		<a href="./detail.py?id=%s" class="btn btn-info glyphicon glyphicon-th"> 详情 </a>
		  		<a href="./edit.py?id=%s&nickname=%s&tel=%s&sex=%s&address=%s" class="btn btn-primary glyphicon glyphicon-pencil"> 编辑 </a>
		  		<a href="./delete.py?id=%s" class="btn btn-danger glyphicon glyphicon-trash"> 删除 </a>
		   </td>''' % (i['id'], i['id'],i['nickname'],i['tel'],i['sex'],i['address'],i['id'])
	tr += '</tr>'

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
    <style>
    	th{
    		text-align: center;
    	}
    </style>
</head>
<body>
    <div class="container">
		<h3>用户列表</h3>

        <a href="../add.html" class="btn btn-success"> 添加用户 </a>        

        <table class="table table-bordered table-hover table-striped table-condensed">
            <tr class="active warning" >
                <th>编号</th>
                <th>昵称</th>
                <th>电话</th>
                <th>性别</th>
                <th>住址</th>
                <th>操作</th>
            </tr>
           	%s 
        </table>
    </div>
    <script src="../boot/js/jquery.min.js"></script>
    <script src="../boot/js/bootstrap.min.js"></script>
</body>
</html>
''' % tr

print(html)








