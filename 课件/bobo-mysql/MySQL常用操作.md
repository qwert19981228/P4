# MySQL常用操作 #
## 0. 准备 ##

	GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY '123' WITH GRANT OPTION;

	create table t1 (
	id int primary key auto_increment,
	name char(50)
	);
	insert into t1 values(1,'jack'),(2,'rose'),(3,'mary');
	desc t1;


## 1. 表复制 ##
>复制表结构+复制表数据（推荐）

	mysql>create table t2 like t1;
	mysql>insert into t2 select * from t1;

>直接复制表数据，但无索引和约束

	mysql>create table t3 select * from t1;

## 2.	函数 ##

>数学

	ABS(x)   					返回x的绝对值
	BIN(x)   					返回x的二进制（OCT返回八进制，HEX返回十六进制）
	CEILING(x)   				返回大于x的最小整数值
	FLOOR(x)   					返回小于x的最大整数值
	GREATEST(x1,x2,...,xn)		返回集合中最大的值
	LEAST(x1,x2,...,xn)      	返回集合中最小的值
	LN(x)                    	返回x的自然对数
	LOG(x,y)					返回x的以y为底的对数
	MOD(x,y)                 	返回x/y的模（余数）
	PI()						返回pi的值（圆周率）
	RAND()						返回０到１（不含1）的随机值,可以通过提供一个参数(种子)使RAND()随机数生成器生成一个指定的值。
	ROUND(x,y)					返回参数x的四舍五入的有y位小数的值
	SIGN(x) 					返回代表数字x的符号的值
	SQRT(x) 					返回一个数的平方根
	TRUNCATE(x,y)            	返回数字x截短为y位小数的结果

>聚合(常用于GROUP BY从句的SELECT查询中)

	AVG(col)					返回指定列的平均值
	COUNT(col)					返回指定列中非NULL值的个数
	MIN(col)					返回指定列的最小值
	MAX(col)					返回指定列的最大值
	SUM(col)					返回指定列的所有值之和
	GROUP_CONCAT(col) 			返回由属于一组的列值连接组合而成的结果

>字符串函数

	ASCII(char)					返回字符的ASCII码值
	BIT_LENGTH(str)				返回字符串的比特长度
	CONCAT(s1,s2...,sn)			将s1,s2...,sn连接成字符串
	CONCAT_WS(sep,s1,s2...,sn)	将s1,s2...,sn连接成字符串，并用sep字符间隔
	LCASE(str)或LOWER(str)		返回将字符串str中所有字符改变为小写后的结果
	LEFT(str,x)					返回字符串str中最左边的x个字符
	LENGTH(s)					返回字符串str中的字符数
	LTRIM(str) 					从字符串str中切掉开头的空格
	POSITION(substr,str)		返回子串substr在字符串str中第一次出现的位置
	REPEAT(str,srchstr,rplcstr)	返回字符串str重复x次的结果
	REVERSE(str) 				返回颠倒字符串str的结果
	RIGHT(str,x) 				返回字符串str中最右边的x个字符
	RTRIM(str) 					返回字符串str尾部的空格
	TRIM(str)					去除字符串首部和尾部的所有空格
	UCASE(str)或UPPER(str) 		返回将字符串str中所有字符转变为大写后的结果


>日期和时间函数

	CURDATE()或CURRENT_DATE() 	返回当前的日期
	CURTIME()或CURRENT_TIME() 	返回当前的时间
	DATE_FORMAT(date,fmt)  		依照指定的fmt格式格式化日期date值
	FROM_UNIXTIME(ts,fmt)  		根据指定的fmt格式，格式化UNIX时间戳ts
	HOUR(time)   				返回time的小时值(0~23)
	MINUTE(time)   				返回time的分钟值(0~59)
	MONTH(date)   				返回date的月份值(1~12)
	NOW()    					返回当前的日期和时间
	WEEK(date)   				返回日期date为一年中第几周(0~53)
	YEAR(date)   				返回日期date的年份(1000~9999)

>加密函数

	MD5(str)    				计算字符串str的MD5校验和
	PASSWORD(str)   			返回字符串str的加密版本，这个加密过程是不可逆转的，和UNIX密码加密过程使用不同的算法。
	SHA(str)    				计算字符串str的安全散列算法(SHA)校验和

>格式化函数

	FORMAT(x,y)   				把x格式化为以逗号隔开的数字序列，y是结果的小数位数
	INET_ATON(ip)   			返回IP地址的数字表示
	INET_NTOA(num)   			返回数字所代表的IP地址

>系统信息函数

	DATABASE()   				返回当前数据库名
	BENCHMARK(count,expr)  		将表达式expr重复运行count次
	CONNECTION_ID()   			返回当前客户的连接ID
	FOUND_ROWS()   				返回最后一个SELECT查询进行检索的总行数
	USER()或SYSTEM_USER()  		返回当前登陆用户名
	VERSION()   				返回MySQL服务器的版本

>以上函数全部使用select调用输出，以下为常用show操作

	SHOW CHARACTER SET			显示所有可用的字符集
	SHOW COLLATION				输出包括所有可用的校对字符集
	SHOW COLUMNS				显示在一个给定表中的各列的信息,对于视图，本语句也起作用。
	SHOW CREATE DATABASE		显示用于创建给定数据库CREATE DATABASE语句。
	SHOW DATABASES				SHOW DATABASES可以在MySQL服务器主机上列举数据库。
	SHOW ENGINES				检查一个存储引擎是否被支持，或者对于查看默认引擎是什么
	SHOW INDEX					会返回表索引信息。
	SHOW TABLES					列举了给定数据库中的非TEMPORARY表。
	SHOW VARIABLES				列举当前环境变量



## 3. 预处理 ##
>预先处理SQL的语法，通过传值完成SQL。

>优势：提高效率（重用），防止SQL注入（安全）。
PDO中的prepare就是调用该方法！！！

	1、设置stmt1预处理，传递一个数据作为一个where判断条件
		mysql>prepare stmt1 from ‘select * from t1 where id>?’;
	2、设置一个变量
		msyql>set @i=1;
	3、执行stmt1预处理
		mysql>execute stmt1 using @i;
	4、删除预处理
		mysql>drop prepare stmt1;

## 4.	事务 ##
	insert into t1 (name) select t1.name from t1;

>多个步骤为一个过程的事物（整体）,中间有任何一个环节出问题，都会造成事物的回滚

>表类型（引擎）：innodb

	1、	关闭自动提交功能或开启事务
	mysql>set autocommit=0;
	mysql>begin;
	2、	删除记录
	mysql>delete from t1 where id = 2;
	3、	创建还原点
	mysql>savepoint p1;
	4、	删除记录
	mysql>delete from t1 where id = 3;
	5、	再创建还原点
	mysql>savepoint p2;
	6、	删除记录
	mysql>delete from t1 where id = 4;
	7  退回还原点
	mysql>rollback to p1;
	mysql>rollback to p2;
	8	退回起始点
	mysql>rollback;
	9  确认提交
	mysql>commit;

## 5.	存储 ##
>批量的有规律的mysql操作可以事前存在procedure中，后期调用。

	1、	创建一个存储p1()
	mysql>\d //		//将结束符修改为”//”  或者delimiter //
	mysql>create procedure p1()
	->begin
	->set @i=1;
	->while @i<6 do
	->select * from t1 where id=@i;
	->set @i=@i+1;
	->end while;
	->end//
	2、	执行存储p1()
	mysql>\d ;			//将结束符修改回；
	mysql>call p1;
	3、	查看所有procedure的status信息
	mysql>show procedure status\G
	4、	查看procddure p1()的具体信息
	mysql>show create procedure p1\G
	5、	删除procedure
	mysql>drop procedure p1;
## 6.	触发器 ##

>监视某种事件，并触发某种操作。（商品添加，订单消除等连贯表操作时使用）

>触发四要素：
>
>1、监视地点（table）2、触发时间（after/before）3、监视事件（insert/update/delete）4、触发事件（insert/update/delete）

	1、	修改delimiter为//
	mysql>\d //
	2、	创建一个名为tg1的触发器，当向t1表中插入数据前，就向a表中插入一条数据
	mysql>create trigger tg1 before insert on t1 for each row	#固定写法
	->begin
	->insert into a values (4);
	->end//
	3、	修改delimiter为;
	mysql>\d ;
	4、	插入数据测试
	insert into t1 values (null,'tom');

## 7.	视图 ##

	创建视图：
		mysql>create view v_t1 as select * from t1 where id>1 and id<5;
	视图帮助信息：
		mysql>?  view
		ALTER VIEW
		CREATE VIEW
		DROP VIEW
	查看视图：
		mysql>show tables;
		mysql>select * from v_t1;
	删除视图：
		drop view v_t1;
		视图相当于表查询的快捷方式，表数据改变，视图也跟着变。


## 8.	临时表 ##
>仅在当前session有效的存在于内存中的临时表。

	create temporary table tmp1 (id int) ;

>只对当前会话(连接)有效，断开后，临时表自动清除，也可以自己drop table tmp1;临时表在销毁前，文件暂存/tmp下。

## 9.	虚拟表 dual ##
>在Oracl中有虚拟表技术，MySQL也效仿设置虚拟表。MySQL中直接查数据或者调用函数可以不用from表，但为了照顾select from 的习惯固设立虚拟表 **dual**


	mysql>select now();		//实际操作为下句
	mysql>select now() from dual;

## 10.	重置自增 ##

>MySQL数据库自增ID如何恢复

	清空表
		delete	from  tablename			//只能清空数据，不能重置ID
	修改表
		alter table tablename auto_increment=1；
	或者
		truncate	table tablename;	//推荐

## 11.	数据导入导出 ##

>完整备份：

	[root@localhost ~]# /usr/local/mysql/bin/mysqldump -uroot -p -l -F test>'/tmp/test.sql'

>导出一个数据库中每一个表的相关SQL语句，包含建表、增删改查等导入导出速度慢！

>完整导入：

	create database test2;

	[root@localhost ~]# /usr/local/mysql/bin//mysql -uroot -p123 test2</tmp/test.sql

>单表数据备份：

	mysql>select * from t1 into outfile '/tmp/t1.txt';

>仅仅是导出表数据，查什么就导出什么。

>导入数据：

	truncate t1;		#准备工作，先清空表，或自己创建一个表
	mysql>load data infile '/tmp/t1.txt' into table t1;

	可以指定某一些列，空置字段为NULL或者默认值
	mysql>load data infile '/test/users.txt' into table users(id,name);


## 12. 索引操作 ##
>什么是索引？
就像是书的目录，能够提高查询速度，降低写入速度，占用磁盘空间

>分类：主键、唯一、普通、全文(sphinx等检索引擎代替)

	ALTER TABLE ADD				//增
	ALTER TABLE table_name ADD INDEX idx_name(column_list)
	ALTER TABLE table_name ADD UNIQUE uk_name (column_list)
	ALTER TABLE table_name ADD PRIMARY KEY (column_list)
	ALTER TABLE DROP			//删
	ALTER TABLE table_name DROP INDEX idx_name/uk_name	//唯一和普通都用此方式
	ALTER TABLE table_name DROP PRIMARY KEY
	show index from table_name	//查

>注意：
>
>删除主键索引，该字段不能有auto_increment，如果有先修改掉再删。
>
>修改索引：先增再删

## 13. root密码丢失找回 ##
>丢失时的密码重置

	1、	停止服务
		pkill mysqld
	2、	重启服务，但需要跳过授权表限制
		/usr/local/mysql/bin/mysqld_safe --skip-grant-tables --user=mysql &
	3、	登录
		mysql -uroot
		不用密码即可
	4、	查看现有用户
		select user,host,password from mysql.user;
	5、	修改密码
		update mysql.user set password=password('123') where user='root' and host='localhost'
	6、	退出
		exit
	7、	重启MySQL
		pkill mysqld
		/usr/local/mysql/bin/mysqld_safe --user=mysql &

>正常修改密码方式：

	方法一：
	正常登陆mysql后，
	mysql> set password for root@localhost=password("123");

	方法二：
	脚本命令行
	./mysqladmin -u root -p password mypasswd（新密码）
	然后输入旧密码


