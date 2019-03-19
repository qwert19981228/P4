# MySQL优化 #
## 序 ##
>**为什么需要MySQL优化？**

>避免出现页面访问错误
>
- 由于数据库连接timeout产生页面5xx的错误
- 由于慢查询造成页面无法加载
- 由于阻塞造成数据无法提交

>增加数据库稳定性
>
- 很多数据库问题都是由于低效的查询引起的

>优化用户体验
>
- 流畅页面的访问速度
- 良好的网站功能体验

![](http://i.imgur.com/6NYeBlz.png)

>根据此表得出结论:优化最佳方式是SQL及索引的优化，效果好成本低，所以我们以逆向的顺序介绍优化方式

# 一、SQL及索引 #

>以下所有案例都包括在MySQL官方测试库Sakila上，Sakila是一个模拟电影出租厅信息管理系统的数据库，具体请参见《SakilaMySQL样例数据库解析》

## 1.1 优化SQL语句的一般步骤 ##
### 1. 通过show status命令了解服务器状态和SQL执行频率 ###
>通过show status命令可以提供服务器状态信息

	格式： show [session|global] status [like]	//session是默认参数表示当前连接，global表示全局
	mysql>show status like 'com_%';				//显示各类语句执行次数，所有表
	mysql>show status like 'Innodb_rows%';		//只统计Innodb表

	以下几个参数便于用户了解数据库基本情况

	Connections：视图连接MySQL服务的次数
	Uptime：服务器工作时间
	Slow_queries：慢查询次数

### 2. 定位执行效率低的SQL语句 ###
>顾名思义，会将你认为慢的SQL记录下来，MySQL自带日志记录功能。

	慢查询相关属性：
	mysql>show variables like 'slow_query%';		//返回功能是否开启和日志存放位置
	mysql>show variables like "long_query_time";	//返回慢查询的限定值单位秒（几秒算慢？）
	mysql>show status like 'slow_queries';			//返回慢查询次数

	开关慢查询：
	【临时】重启后失效
	mysql>set global slow_query_log=1;

	【永久】修改配置文件 my.ini
	Linux版本：
		在my.cnf的[mysqld]之后添加

		slow_query_log = 1
		slow_query_log_file = slow.log
		long_query_time=1							//可根据具体情况修改 单位秒

	WAMP版本：
		在my.ini的[wampmysqld]之后添加

		slow_query_log = ON
		slow_query_log_file = C:/wamp/bin/mysql/mysql5.7.9/kid-PC-slow.log
		long_query_time = 1

>慢查询日志主要包含内容为：
>

- SQL主机信息
- SQL执行信息
- SQL执行时间
- SQL内容

>经过筛查可以发现有问题的SQL

### 3. 通过EXPLAIN 或 DESC 分析低效的SQL ###
>通过以上步骤获取到效率低的SQL后可以通过EXPLAIN或者DESC命令对SQL语句进行分析

	mysql>desc select sum(amount) from customer a,payment b where 1=1 and a.customer_id =\
	b.customer_id and email = 'JANE.BENNETT@sakilacustomer.org'\G

>对显示内容的说明

- select_type：表示SELECT类型
	- SIMPLE（简单表，不使用多表联查或子查询）
	- PRIMARY（主查询，即外层查询）
	- SUBQUERY（子查询中的第一个SELECT）
	- DEPENDENT SUBQUERY（子查询内层的第一个SELECT，依赖于外部查询的结果集）
	- DERIVED（子查询在from子句中，执行查询的时候会把子查询的结果集放到临时表）
	- UNION（UNION中的第二个或者后面的查询）
	- UNION RESULT（从UNION临时表获得结果集合）
- table：输出结果集的表
- type：表示MySQL在表中找到数据的方式或者访问类型，性能由差到优
	- ALL（全表）
	- inedx（索引扫描）
	- range（索引范围扫描）
	- index_merge（非主键的联合查询）
	- index_subquery（非主键子查询）
	- unique_subquery（主键子查询）
	- ref_or_null（同前面对null查询）
	- ref（使用非唯一或唯一索引的前缀扫描）
	- eq_ref（类似ref，区别使用的是唯一索引，对于每个值只有一条记录如primary key 或者 unique index）
	- const/system（单表中只有一行匹配，非常迅速）
	- NULL（不访问索引即能得到结果）


	>以下为常见select_type的示例：

		mysql>desc select * from film where rating >9\G
		mysql>desc select title from film\G
		mysql>desc select * from payment where customer_id >= 300 and customer_id <= 350\G
		mysql>desc select * from payment where customer_id = 350\G
		mysql>desc select b.*, a.* from payment a, customer b where a.customer_id = b.customer_id\G
		mysql>desc select * from film a, film_text b where a.film_id = b.film_id\G
		mysql>desc select * from (select * from customer where email = 'AARON.SELBY@sakilacustomer.org')a\G
		mysql>desc select 1 from dual where 1\G

- possible_keys：表示查询时可能用到的索引
- key：表示实际用到的索引
- key_len：使用到索引字段的长度
- rows：扫描行数
- Extra：执行情况说明，包含不适合在其他列显示但对执行计划非常重要的额外信息
	- using index（出现这个说明mysql使用了覆盖索引，避免访问了表的数据行，效率不错！）
	- using where（这说明服务器在存储引擎收到行后将进行过滤。有些where中的条件会有属于索引的列，当它读取使用索引的时候，就会被过滤，所以会出现有些where语句并没有在extra列中出现using where这么一个说明）
	- using temporary（使用了一张临时表）
	- using filesort（数据使用一个外部的索引排序）
- filtered：在添加EXTENDED时出现（5.7后直接显示）与rows一起使用计算EXPLAIN的行，源码分析几乎无用！
>EXPLAIN 后加 EXTEDNED 可显示扩展信息如：WARNGING
>
>出现的WARNING信息多为MySQL优化语句（真正执行的语句）
>可通过下面的语句查询WARNING详情：

	show warnings();

### 4. 通过 show profile分析SQL ###
>show profile功能可针对具体SQL的子步骤分析问题

	检查是否支持
	mysql>select @@have_profiling;

	检查是否开启
	mysql>select @@profiling;

	设置开启
	mysql>set profiling = 1;

	查询执行情况
	mysql>show profiles;

	查看具体执行ID的情况
	mysql>show profile for query n;

### 5. 确定问题采取相应的优化措施 ###

## 1.2 索引问题 ##
>索引是数据库优化中最常用的手段之一，通过索引的使用可提升SQL性能，本部分将详细讨论索引分类、存储、使用方法。

>1. 索引的分类
	1. 按类型名区分
		- PRIMARY KEY	（ID）
		- UNIQUE		（用户名、电话号、邮箱等唯一性）
		- INDEX		（主要）
	2. 按字段数量分
		- 单列
		- 多列		（分区使用）
	3. 按存储结构分
		- B-Tree		（主要）
		- HASH		（Memory独有）
		- R-Tree		（MyISAM在存储地理空间时使用）
		- Full-text	（全文搜索，对中文支持不佳）

>2. 如何使用

### 经典使用场景 ###

>匹配全值：

	mysql>desc select * from rental where rental_date = '2005-05-25 17:22:10' and inventory_id = 373 and customer_id = 343\G

>匹配范围：

	mysql>desc select * from rental where customer_id >= 373 and customer_id < 400\G

>最左前缀：

	mysql>alter table payment add index idx_payment_date(payment_date, amount, last_update);
	mysql>desc select * from payment where payment_date = '2006-02-14 15:16:03' and last_update = '2006-02-15 22:12:32'\G
	mysql>desc select * from payment where amount = 3.98 and last_update = '2006-02-15 22:12:32'\G
说明：多列联合索引为 col1+col2+col3... 能用到的条件必须为col1开头， where 条件为 col2+col3则用不到

>仅搜索索引（覆盖索引扫描，不需要回表）：

	mysql>desc select last_update from payment where payment_date = '2006-02-14 15:16:03' and amount = 3.98\G

>匹配列前缀（多列索引）：
	使用多列索引的第一列

	mysql>alter table film_text add index idx_title_desc_part(title(10),description(20));
	mysql>desc select title from film_text where title like 'AFRICAN%'\G
说明：Extra的值为Using where 表示优化器需要通过索引回表查询数据。
另：对Full-text 的使用  MATCH(col1,col2...)  AGAINST('STR')  注意忽略

	desc select * from film_text where match(title,description) against('CRUE')\G

>部分精确其它范围：

	mysql>desc select inventory_id from rental where rental_date = '2006-02-14 15:16:03' and customer_id >= 300 and customer_id <= 400\G
说明：条件导致Using where 但查询的数据为inventory_id所以

>列为索引 col_name is null：

	mysql>desc select * from payment where rental_id is null\G

>ICP优化：

	mysql>select version();		//  >5.6 支持
	mysql>desc select * from rental where rental_data = '2006-02-14 15:16:02' and customer_id >= 300 and customer_id <= 400\G
说明：Extra中显示Using index condition，ICP优化

### 存在带不能使用的场景 ###

>以 % 开头的LIKE条件：

	mysql>desc select * from actor where last_name like '%NI%'\G
说明：key为NULL，使用不到索引

>数据类型出现隐式转换：

	mysql>desc select * from actor where last_name = 1\G

>多列索引查询条件不包括最左部分，即不满足左原则：

	mysql> desc select * from payment where amount = 3.98 and last_update = '2006-02-14 22:12:32'\G

>如果使用索引比全表扫描慢：

	mysql> update film_text set title = concat('S',title);
	mysql> desc select * from film_text where title like 'S%'\G
说明：辨识度越高，越喜欢喜欢使用索引

>用or分开的条件：

	mysql>desc select * from payment where customer_id = 203 or amount = 3.96\G

>条件索引使用函数：


说明：逻辑或后面没有索引就要全表扫描，前面还不如不用

### 检查索引使用情况 ###

	show status like 'Handler_read%';

>Handler_read_first：索引中第一条被读的次数。如果较高，它建议服务器正执行大量全索引扫描。
>
>**Handler_read_key**：根据键读一行的请求数。如果较高，说明查询和表的索引正确。
>
>Handler_read_next：按照键顺序读下一行的请求数。如果你用范围约束或如果执行索引扫描来查询索引列，该值增加。
>
>Handler_read_prev：按照键顺序读前一行的请求数。该读方法主要用于优化ORDER BY ... DESC。
>
>Handler_read_rnd：大量的都表文件。
>
>**Handler_read_rnd_next**：在文件中读下一行的请求数，高则意味着查询运行低效，应该添加索引补救。

## 1.3 简单实用的优化方式 ##
### 定期分析和检查表 ###

	analyze table payment；
	check table payment;

### 定期优化表 ###

	optimize table payment;
说明：默认情况下，直接对InnoDB引擎的数据表使用OPTIMIZE TABLE，可能会显示「 Table does not support optimize, doing recreate + analyze instead」的提示信息。这个时候，我们可以用mysqld --skip-new或者mysqld --safe-mode命令来重启MySQL，以便于让其他引擎支持OPTIMIZE TABLE。

>Innodb表可能是独立表空间，在删除大量数据后可通过修改表引擎的方式回收空间

>注意：以上优化命令会有锁表，需在不繁忙是使用。

## 1.4 常用SQL的优化 ##
### 大批量插入数据 ###
>当load data时适当的设置可提高导入速度，对于MyISAM可通过以下方式提高导入速度。

	ALTER TABLE tbl_name DISABLE KEYS;
	loading the data……
	ALTER TABLE tbl_name ENABLE KEYS;

>开启或者关闭MyISAM的非唯一索引的更新，在导入大量数据到非空表示提高，空表默认就是先导入再创建，固不用设置。
对于InnoDB并不能提高效率，InnoDB提供以下几种方案：


1.导入数据按照主键顺序

2.导入前关闭唯一性校验，导入后开启

	SET UNIQUE_CHECKS = 0;	//关闭
	loading the data……
	SET UNIQUE_CHECKS = 1;	//开启


3.关闭自动提交

	SET AUTOCOMMIT = 0；		//关闭
	loading the data……
	SET AUTOCOMMIT = 1;		//开启


### 优化INSERT语句 ###
>大量数据添加使用多值INSERT语句代替多个INSERT单句

	insert into test values(1, 2),(2, 3)……

>LOAD DATA INFILE 比INSERT快20倍（理论）

##大量数据插入实例##

>检测

	文件大小
	watch -n1 ls -lh /usr/local/mysql/data/test
	每一秒刷新一次，可动态查看文件大小变化。

	内存和CPU的使用
	free –m
	top

>准备工作

1、建表

	create table t1 (id int auto_increment primary key,name varchar(255),name1 varchar(255)) engine=myisam default charset=utf8;

2、插入测试数据

	mysql -uroot -p123 test < /root/10000.sql

3、复制成约512万条

	ALTER TABLE tbl_name DISABLE KEYS;

	insert into t1 (name,name1) select name,name1 from t1;

	将本表现存数据再次插入，相当于复制。
	或者用单表导入：

	select * from t1 into outfile '/tmp/t1.txt';

	load data infile '/tmp/t1.txt' into table t1 (name,name1);

	ALTER TABLE tbl_name ENABLE KEYS;

4、复制过程中查看服务器信息（文件大小、内存、CPU%）

5、查看数据文件

MyISAM引擎的表有三个文件

	xxx.frm		是表的表结构

	xxx.MYD		是表的数据

	xxx.MYI		是表的索引

InnoDB引擎的表有两个文件

	xxx.frm		是表的表结构

	在上层data下还有一个

	ibdata1是所有innodb表的数据，大小10M

500万条数据，自增主键的索引有51M

500万条数据，占了148M硬盘空间(只有两列姓名的数据)。

6、查看数据条数

	select count(id) from t1;

7、开始查询

	select count(*) from t1 where name like '王%';

	查询响应时间慢长

8、为name字段添加索引
	alter table t1 add index ind_name (name);

		在创建时，系统占用内存300M,占用CPU 90%

		在索引时，会使用临时文件，以#号开头的是临时文件

		-rw-rw---- 1 mysql mysql 8.5K 07-19 22:58 #sql-d09_2.frm

		-rw-rw---- 1 mysql mysql  57M 07-19 23:06 #sql-d09_2.MYD

			//这个临时文件大小，接近原数据大小时，说明快创建完成了

		-rw-rw---- 1 mysql mysql  24M 07-19 23:06 #sql-d09_2.MYI

		完成后索引文件变大

9、再次查询
	mysql>select count(*) from t1 where name like '王%';
	快很多

10、用不到索引的查询
	select count(*) from t1 where name like '%王%';
	select count(*) from t1 where name1 like '%王%';
	如果有索引用不到，比没索引还要慢


## 优化ORDER BY语句	 ##
### MySQL有两种排序方式 ###

>第一种为索引排序，desc的Extra显示为Using index

>第二种对返回数据进行排序，Filesort排序（非索引都叫），可能使用磁盘空间或临时表进行排序，具体情况看服务器和数据大小。

能用到索引的排序：

	select * from tbl_name order by key_part1, key_part2, ...;
	select * from tbl_name where key_part1 order by key_part1 desc, key_part2 desc;
	select * from tbl_name order by key_part1 desc, key_part2 desc;

不能使用索引的排序：

	混合使用asc和desc
	select * from tbl_name order by key_part1 desc, key_part2 asc;

	查询和排序条件不同
	select * from tbl_name where key2=constant order by key1;

	对不同关键字使用排序
	select * from tbl_name order by key1, key2;

>小结：尽量减少额外排序，尽量使用索引返回有序数据。

### 优化 GROUP BY语句 ###
>避免分组结果排序对性能的消耗可以指定 `order by null`

### 优化嵌套查询（子查询） ###
>MySQL5.5版本之后同样结果的子查询效率不及关联查询（JOIN），因为JOIN更高效不需要要简历临时表参与查询。

	mysql>desc select * from customer where customer_id not in(select customer_id from payment)\G
	mysql>desc select * from customer a left join payment b on a.customer_id = b.customer_id where b.customer_id is null\G

上一条查询类型为index_subquery，下一条为ref更加快速。

### 优化 WHERE OR 条件 ###
>在对含有OR的条件查询时，OR两边的条件都必须用到索引，如果没有请添加。

	mysql>desc select * from actor where actor_id=4 or last_name='DAVIS'\G

经过优化，改语句实际执行为两条分别执行的语句进行UNION。

### 优化 LIMIT 分页 ###
>常见分页场景 "limit 1000,20" ,先排好序1020条，但仅仅返回1001-1020，代价太高。

原sql：

	mysql>desc select film_id, description from film order by title limit 50,10\G

优化思路：

	mysql>desc select film_id, description from film where film_id > 50 order by title limit 10\G

# 二、优化数据库表结构 #
## 2.1 优化表的数据类型 ##
>使用函数 PROCEDURE ANALYSE() 提出优化建议

	select * from payment procedure analyse();
	select * from payment procedure analyse(16,256);

>根据统计出的现有数据，可给出优化建议进行字段类型的更改。
>第二个例子告诉PROCEDURE ANALYSE(  )不要为那些包含的值多于16个或者256字节的ENUM类型提出建议。

## 2.2 通过表拆分提高效率 ##
>拆分方式两种，垂直拆分和水平拆分。

垂直拆分：表拆分成主列和辅列，也就是业务中常用和不常用的，在常用查询中I/O会减少但查询全部数据时需要JOIN。

水平拆分：表很大、本身就具有独立性（区域、时期、级别、常用与否等）时拆分。

## 2.3 逆规范化（反三范式） ##
- 增加冗余列
- 增加派生列
- 重新组表（视图）
- 分割表

## 2.4 字段类型的选取 ##
>1. 整型

- 手机号：bigint
- IP地址：int
	- 使用函数INET_ATON(  )可将ip地址（点分十进制）转为数字
	- 使用函数INET_NTOA(  )可将数字再转为ip地址
	- PHP中也有相关的处理函数，为了提高效率可在PHP中处理 ip2long  long2ip
- 根据需求选择最小整数类型
- 值得种类很少时可适当选择枚举ENUM

>2. 字符型

- 计算varchar的最大长度
	- UTF8:varchar(21844)
	- GBK:varchar(32739)
- char和varchar的选择
	- 变化的值如地址等用varchar
	- 固定的值如密码等用char
	- varchar要用多一个字节存储值得长度

>3. 时间类型
- 优先选择TIMESTAMP，它会自动更新时间

## 2.5 采用合适的锁机制 ##
MySQL的锁有以下几种形式：
- 表级锁：开销小，加锁快；不会出现死锁；锁定颗粒度大，发生冲突概率最高，并发度最低。MyISAM属于此类级
- 行级锁：开销大，加锁慢；会出现死锁；锁定颗粒度小，发生冲突几率低，并发最高。InnoDB属于此类级
- 页面锁：介于表级和行级之间。NDB属于此类级

	mysql>lock table tbl_name read;
	//以只读方式锁定表
	mysql>unlock tables;
	//解锁

>在InnoDB表中，使用索引检索数据才会自动启用行锁，如果没有使用则表级锁

>死锁：多方获取一个资源的锁定，InnoDB自检释放一个并回退继续完成另一个事务。不可避免，可通过调整业务逻辑降低概率。

## 2.6 InnoDB和MyISAM的区别 ##
- MyISAM是非事务安全型，InnoDB是事务型支持ACID属性
- MyISAM锁定为表级，InnoDB支持行级，支持更好的并发写操作
- 存储文件不同，MyISAM迁移方便，InnoDB存储分为共享和独立两种
- InnoDB比MyISAM更安全
- InnoDB主键范围为MyISAM的两倍
- MyISAM自增索引必须单列，InnoDB可以是混合索引

# 三、系统配置调优 #
## 3.1 per_thread_buffers ##
### read_buff_size ###
>该参数用于顺序扫描，每个线程分配的缓冲区大小。每次扫描暂存在read_buffer_size中，写满或结束后返回给上层调用者，默认128KB。这个参数不易过大，一般在128-256KB即可。

### read_rnd_buffer_size ###
>该参数用于随机读取，不用索引会用此缓冲区暂存数据。默认256KB。这个参数不易过大，一般在128-256KB即可。

### sort_buffer_size ###
>如果在order by 和 group by没有使用索引导致 filesort时，为提高性能分配的缓冲区，默认为2MB。这个参数不易过大，一般在128-256KB即可，如果出现 Using filesort此缓冲区解决不了实质问题需要添加索引优化。

### thread_stack ###
>每个线程的堆栈大小默认192KB。如果是64位系统可设置为256KB，不要设置过大。

### join_buffer_size ###
>进行JOIN操作时，如果关联字段没索引会出现Using join buffer 为了提高性能设置此参数。默认128KB。这个参数不易过大，一般在128-256KB即可，如果出现 Using filesort此缓冲区解决不了实质问题需要添加索引优化。

### binlog_cache_size ###
>事务缓存值，设置为1-2MB比较合适，如果SQL有大事务可调整。

### max_connections ###
>该参数设置最大连接数，默认为100，一般设置为512-1000即可。

上面介绍了各种参数，那么此公式就是per_thread_buffers的含义：

	(read_buffer_size+read_rnd_buffer_size+read_rnd_buffer_size+thread_stack+join_buffer_size+binlog_cache_size)*max_connections

## 3.2 global_buffers 优化 ##
### innodb_buffer_poll_size ###
>InnoDB的核心参数，默认配置128MB，一般设置为MySQL服务器内存的60%~70%。

### innodb_additional_mem_pool_size ###
>用来存储表结构，表越多分配内存越多，如果用光则在日志中写警告，然后从操作系统借用内存，默认8M，当出现报错时则需要调整，一般可设置为16MB。

### innodb_log_buffer_size ###
>事务日志缓冲池，默认空间8MB，一般根据事务多少设置为16-64MB

### key_buffer_size ###
>此参数用来缓存MyISAM的索引，因为高版本默认用InnoDB所以这个参数64MB即可。

### query_cache_size ###
>缓存select语句的到的结果集

根据以上参数可计算出gloal_buffers

	innodb_buffer_poll_size+innodb_additional_mem_pool_size+innodb_log_buffer_size+key_buffer_size+query_cache_size

## 3.3 Query Cache的使用 ##
>MySQL自带的缓存结果集功能，第一次查后缓存，再查读缓存数据。如果数据有修改则清除缓存。当有些表不常修改查询量又很大时非常有用。

	query_cache_type=1;		//开启

>如果环境下写操作较多不适合开启，频繁的刷新缓存会让性能下降，此时应该关闭并且

	query_cache_size=0;

