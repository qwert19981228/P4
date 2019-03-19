redis模拟微博的简单用户管理
包括用户的增删改查，关注等功能
-------------------------------
页面创建顺序与功能描述：
1、redis.php		//redis实例化、连接、验证
2、add.php			//添加用户，提交至reg.php
3、reg.php			//处理post传值，userid(string)、user:id(hashs)、uid(list)、username:username(string)
4、login.php		//form表单登陆，本页面验证，设置cookie后跳转list页面
5、list.php			//判断登陆状态，欢迎语username，分页，表格遍历，关注被关注。
6、addfans.php		//添加粉丝，id关注谁，uid谁关注，following关注，followers粉丝
7、mod.php			//修改页面，通过id获取旧值遍历
8、domod.php		//将新值覆盖旧值
9、del.php			//删除用户，hash键和list的值
10、logout.php		//登出，auth删除、cookie失效
-------------------------------
keys解释：

userid					//string，用于id自增
user:$uid				//hash，存放用户详情
uid 					//list，存放ids用户遍历和分页
username:$username		//string，用于存放用户id，便于登录时查询
auth:$auth				//string，用于存放登陆用户cookie，判断登陆状态
user:$id:following		//set，用于存放id用户的关注成员
user:$id:followers		//set，用户存放id用户被关注的成员