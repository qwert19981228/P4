# 添加用户


# 引入 cgi模块
import cgi, cgitb, pymysql, json, hashlib

# 开启错误提示
cgitb.enable()

# 配置 请求头
print('Content-Type: text/html')
print()



# 3. 准备sql:  查询所有的用户
# 3.1 接收参数
data = cgi.FieldStorage()

data_dict = {}
for i in data.keys():
   data_dict[i] = data[i].value

html='''
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
        <div class="row">
            <div class="col-md-2 col-md-offset-5" style="margin-bottom: 30px;">
                <h3> 修改用户 </h3>
            </div>
            <div class="col-md-6 col-md-offset-3">
                <form class="form-horizontal" action="./edit-main.py" method="post">

                  <div class="form-group">
                    <label for="inputEmail3" class="col-sm-2 control-label"></label>
                    <div class="col-sm-10">
                      <input type="hidden" class="form-control" id="inputEmail3" placeholder="your ID" name="id" value="%s">
                    </div>
                  </div>


                    <div class="form-group">
                    <label for="inputEmail3" class="col-sm-2 control-label">昵称</label>
                    <div class="col-sm-10">
                      <input type="text" class="form-control" id="inputEmail3" placeholder="your Nickname" name="nickname" value="%s" >
                    </div>
                  </div>

                  <div class="form-group">
                    <label for="inputEmail3" class="col-sm-2 control-label">电话</label>
                    <div class="col-sm-10">
                      <input type="text" class="form-control" id="inputEmail3" placeholder="your Tel" name="tel" maxlength="11" value="%s">
                    </div>
                  </div>


                  <div class="form-group">
                    <label for="inputPassword3" class="col-sm-2 control-label">密码</label>
                    <div class="col-sm-10">
                      <input type="password" class="form-control" id="inputPassword3" placeholder="Password" name="pwd" >
                    </div>
                  </div>

                  <div class="form-group">
                    <label for="inputPassword3" class="col-sm-2 control-label">性别</label>
                    <div class="col-sm-10">
                      <div class="radio">
                        <label>
                          <input type="radio" name="sex" value="sex1" id="optionsRadios1" checked> 男
                        </label>
                        <label>
                          <input type="radio" name="sex" value="sex2" id="optionsRadios1" > 女
                        </label>
                      </div>
                      <script>
                      %s
                      </script>
                    </div>
                  </div>


                  <div class="form-group">
                    <label for="inputEmail3" class="col-sm-2 control-label">住址</label>
                    <div class="col-sm-10">
                      <input type="text" class="form-control" id="inputEmail3" placeholder="your Address" name="address" value="%s">
                    </div>
                  </div>

                  <div class="form-group">
                    <div class="col-sm-offset-2 col-sm-10">
                      <button type="submit" class="btn btn-default">提交</button>
                    </div>
                  </div>
                </form>
            </div>
        </div>
    </div>
    <script src="../boot/js/jquery.min.js"></script>
    <script src="../boot/js/bootstrap.min.js"></script>
</body>
</html>
''' % (data_dict['id'],data_dict['nickname'],data_dict['tel'],data_dict['sex'],data_dict['address'])

print(html)






