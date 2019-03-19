<!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- 上述3个meta标签*必须*放在最前面，任何其他内容都*必须*跟随其后！ -->
    <title>登陆页</title>
    <!-- Bootstrap -->
    <link href="./dist/css/bootstrap.min.css" rel="stylesheet">
  </head>
  <body>
    <h1>你好，请登录</h1>
	<hr>
	<div class="container">
		<div class="row">
			<div class="col-md-4">
				<form action="doReg.php" method="post">
				  <div class="form-group">
				    <label >用户名</label>
				    <input type="text" class="form-control" name="username" placeholder="请输入用户名">
				  </div>
				  <div class="form-group">
				    <label >密码</label>
				    <input type="password" class="form-control" name='password' placeholder="请输入密码">
				  </div>
				  <div class="form-group">
				    <label for="exampleInputFile">年龄</label>
				    <input type="text" class="form-control" name='age' placeholder="请输入年龄">
				  </div>
				  <button type="submit" class="btn btn-primary">Submit</button>
				  <button type="reset" class="btn btn-info">Reset</button>
				</form>
			</div>
		</div>
	</div>
    <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="./dist/js/jquery.js"></script>
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <script src="./dist/js/bootstrap.min.js"></script>
  </body>
</html>

