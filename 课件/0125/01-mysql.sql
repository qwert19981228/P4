/*
	
	数据库
	1. 定义
		是按照数据结构来组织, 存储 和 管理数据的 仓库

		组成: 库  database
			  表  table

			  库中包含了 表
			  表中包含了 数据

	2. 分类
		2.1 关系型数据库
			MySQL, SQLServer, Oracle ...
			优点:
				保持数据的一致性
				擅长做复杂数据查询
				支持事务

			缺点:
				读写性能比 非关系的差一点.  尤其是 海量数据的高效率读写
				表结构固定, 不灵活


		2.2 非关系型数据库
			Redis, MongoDB, ...
			优点:
				读写速度快
				格式灵活
				开源

			缺点:
				表结构复杂, 导致复杂查询能力较弱
				不支持事务

	
	3. 注释
		/* 多行注释 * /
		-- 单行
		#  单行
		
		注意:
			单行注释符  与  注释内容 之间至少保留一个空格

	4. 基本语法
		命令大写, 自定义名字小写
		自定义名字 不能使用关键字
		每条命令 均已 分号结尾.
*/

-- 常见命令
-- 1. 设置密码
--  	set password = password('密码')

-- 2. 查看数据库
--  	show databases; 		复数

-- 3. 创建数据库
--  	create database ` 库名 `;
--  	create database if not exists ` 库名 `;
--  	create database if not exists ` 库名 ` default charset=编码;

-- 注意:
--  	1) 编码不要写成utf-8,  写成 utf8, 中间没有 "-".
--  	2) if not exists 判断库若存在 , 则不创建
--  						  库若不存在, 则创建
--  	3) 反引号 具有屏蔽关键字的作用. 
--  		推荐:  库名, 表名, 字段名 最好都加上反引号

create database `p4`;
create database if not exists `p4`;
create database if not exists `p4` default charset=utf8;
create database p5;
create database create;
create database `create`;


-- 4. 删除数据库
--  	drop database `库名`;


-- 5. 使用数据库
--  	use `库名`;
-- 
--     注意:
--  		在使用 表之前, 必须先使用 库


-- 6. 查看数据表
--  	show tables;

-- 7. 创建数据表
-- 		create table if not exists `表名`(
-- 			`字段名` 	字段类型 	字段属性,
-- 			`字段名` 	字段类型 	字段属性,
--  		...
-- 			`字段名` 	字段类型 	字段属性 		(最后一个字段的分号, 不能写)
--  	)engine=引擎 default charset=编码;

create table if not exists `user`(
	`id`  			int 		 	auto_increment primary key,	
	`nickname` 		varchar(30) 	not null,
	`pwd` 			char(32) 	 	not null 	comment '加密32位',
	`tel` 			char(11) 		unique not null,
	`sex` 			tinyint(1) 	default 1 	comment '1-男  2-女',
	`birthday` 		date ,			
	`address` 		varchar(50),
	`status` 		tinyint(1) 	default 1,
	`regtime` 		int
)engine=myisam default charset=utf8;


-- 8. 删除数据表
--  	drop table `表名`


-- 9. 查看表结构
--  	desc `表名`


-- 10. 查看建表语句
--  	show create  table `表名`
