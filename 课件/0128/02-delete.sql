-- 删除数据

-- 1. 删除一张表的所有数据
-- delete from `表名`

-- 2. 删除一张表中 部分数据
-- delete from `表名` where 条件
delete from `user` where `sex` = 2

-- 3. 删除一张表中 按照排序的 前几条[满足条件]数据
-- delete from `表名` [where 条件] order by 排序依据 limit 行数
delete from `user` order by `birthday` asc limit 5;


-- 如果为了删除整张表的数据, 不建议用delete, 效率太低, 消耗太高
-- truncate table `表名`


-- 小结:
--  	delete 清除数据, 不会删表, auto_increment 不受影响
--  	truncate 清除结构, 先删表结构, 再重构表结构, auto_increment重新从1 开始计算


/*

配置"环境变量"

	如何在 cmd 中使用mysql
	1. 右击 "计算机"
	2. 选择 "属性"
	3. 左上角 "高级系统设置"
	4. 选择 "高级" -> "环境变量"
	5. 新建/编辑 Path
	6. 复制 mysql.exe 所在目录位置 "C:\Program Files\MySQL\MySQL Server 5.7\bin"
	7. 粘贴进 Path 值里面

	8. 输入 win + R
	9. 输入 cmd
	10. 输入 mysql -u 用户名 -p 回车
	11. 输入密码

	
	备份:
		1. 进入 cmd 
		2. mysqldump -u 用户名 -p 数据库名 > 目标地址
			mysqldump -u root -p p4 > C:/demo.sql

	
	导入:
		1. 进入 cmd
		2. mysql -u 用户名 -p 数据库名 < 来源地址

		注意:
			如果数据库 不存在, 则导入失败.  
			解决: 先自己创建一个库, 再导入


 */