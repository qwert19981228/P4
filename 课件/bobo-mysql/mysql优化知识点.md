
#day1

##mysql 优化

从 哪些开始优化?
1. sql 语句

2. 表结构

3. 优化计算机硬件


怎么做优化?

insert  ....  (key,val)  (k1,v1)
优化:  把 key val  k1 v1  放入数组  直接 insert 一个array

少用* 多用限定字段  和 分页

索引优化


如何分析sql需要还是不需要优化?
根据慢查询日志,来分析
desc/explain  分析日志中的sql语句



最后,总结:
mysql优化一般步骤?
1. 开启慢查询日志

2. 分析sql语句

3. 分析是否加上索引

4. 分析是否用上索引




课堂代码:

索引操作

```
mysql> alter table xintest add index xin_test(name);
Query OK, 3 rows affected
Records: 3  Duplicates: 0  Warnings: 0

mysql> show index from xintest;
+---------+------------+----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
| Table   | Non_unique | Key_name | Seq_in_index | Column_name | Collation | Cardinality | Sub_part | Packed | Null | Index_type | Comment | Index_comment |
+---------+------------+----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
| xintest |          1 | xin_test |            1 | name        | A         | NULL        | NULL     | NULL   | YES  | BTREE      |         |               |
+---------+------------+----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
1 row in set

mysql> alter table xintest add unique xin_unin(name);
Query OK, 3 rows affected
Records: 3  Duplicates: 0  Warnings: 0

mysql> show index from xintest;
+---------+------------+----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
| Table   | Non_unique | Key_name | Seq_in_index | Column_name | Collation | Cardinality | Sub_part | Packed | Null | Index_type | Comment | Index_comment |
+---------+------------+----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
| xintest |          0 | xin_unin |            1 | name        | A         | NULL        | NULL     | NULL   | YES  | BTREE      |         |               |
| xintest |          1 | xin_test |            1 | name        | A         | NULL        | NULL     | NULL   | YES  | BTREE      |         |               |
+---------+------------+----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
2 rows in set

mysql> alter table xintest add primary key(id);
Query OK, 3 rows affected
Records: 3  Duplicates: 0  Warnings: 0

mysql> alter table xintest drop index xin_test;
Query OK, 3 rows affected
Records: 3  Duplicates: 0  Warnings: 0

mysql> alter table xintest drop index xin_unin;
Query OK, 3 rows affected
Records: 3  Duplicates: 0  Warnings: 0

mysql> show index from xintest;
+---------+------------+----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
| Table   | Non_unique | Key_name | Seq_in_index | Column_name | Collation | Cardinality | Sub_part | Packed | Null | Index_type | Comment | Index_comment |
+---------+------------+----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
| xintest |          0 | PRIMARY  |            1 | id          | A         |           3 | NULL     | NULL   |      | BTREE      |         |               |
+---------+------------+----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
1 row in set

mysql> alter table xintest drop primary key;
Query OK, 3 rows affected
Records: 3  Duplicates: 0  Warnings: 0

mysql> show index from xintest;
Empty set


```

1.3 视图
使用 mysql视图的理由?

1. 安全性       给视图分配权限 分配到用户
2. 查询性能提高				只需要调用视图. 不需要重新定义sql
3. 灵活的需求,可以使用其来减少表的修改          
4. 复杂查询需求,可以将问题分解,然后创建多个视图,最后把视图联合起来,就可以得到问题的结果了


注意: 视图  相当于表查询的一个快捷方式

视图 本身不存储数据!!!!!  每次数据 都会从 定义好的sql 中去查询

所以视图,不需要维护. 只需要维护真实表中的数据就可以了

```

mysql> create view v_xin as select * from user where id >1 and id <26;
Query OK, 0 rows affected
mysql> select * from v_xin;
+----+----------+-----+-----+----------+
| id | name     | sex | age | province |
+----+----------+-----+-----+----------+
|  2 | 麦克雷   |   1 |  40 | 纽约     |
|  3 | 卢西奥   |   0 |  26 | 纽约     |
|  4 | 半藏     |   1 |  38 | 东京     |
|  5 | 法老之鹰 |   0 |  30 | 江苏     |
|  6 | 安娜     |   0 |  80 | 江苏     |
|  7 | 天使     |   0 |  30 | 江苏     |
|  8 | 查莉娅   |   0 |  36 | 浙江     |
|  9 | 黑百合   |   0 |  32 | 上海     |
| 10 | 猎空     |   0 |  23 | 北京     |
| 11 | 狂鼠     |   1 |  40 | 新疆     |
| 12 | 托比昂   |   1 |  50 | 新疆     |
| 13 | D.Va     |   0 |  20 | 上海     |
| 14 | 源氏     |   1 |  35 | 东京     |
| 15 | 死神     |   1 |  40 | 纽约     |
| 16 | 士兵76   |   1 |  40 | 纽约     |
| 17 | 堡垒     |   1 |  99 | 纽约     |
| 18 | 老王     |   2 |  40 | 隔壁的   |
| 19 | 小美     |   0 |  23 | 北京     |
| 20 | 莱因哈特 |   1 |  80 | 纽约     |
| 21 | 路霸     |   1 |  43 | 上海     |
| 22 | 温斯顿   |   2 |  20 | 上海     |
| 23 | 秩序之光 |   0 |  19 | 上海     |
| 24 | 小王     |   1 |  40 | 北京     |
| 25 | 小王八   |   1 |   4 | 纽约     |
+----+----------+-----+-----+----------+
24 rows in set

mysql> show tables;
+-----------------+
| Tables_in_s67   |
+-----------------+
| hc_lover        |
| hc_user         |
| lover           |
| pay_businessman |
| pay_user        |
| s72_user        |
| score           |
| t1              |
| t1_copy         |
| t2              |
| t3              |
| t4              |
| user            |
| user2           |
| user_test       |
| v_t1            |
| v_xin           |
| xin             |
| xintest         |
+-----------------+
19 rows in set

mysql> drop view v_xin;
Query OK, 0 rows affected

mysql> show tables;
+-----------------+
| Tables_in_s67   |
+-----------------+
| hc_lover        |
| hc_user         |
| lover           |
| pay_businessman |
| pay_user        |
| s72_user        |
| score           |
| t1              |
| t1_copy         |
| t2              |
| t3              |
| t4              |
| user            |
| user2           |
| user_test       |
| v_t1            |
| xin             |
| xintest         |
+-----------------+
18 rows in set


```


1.4.MySQL内置函数

请尽量减少使用 内置函数.
让mysql好好的做仓库管理员.

处理好数据 是php 应该做的.

```
mysql> select concat('dawei','xihuan','lluguan');
+------------------------------------+
| concat('dawei','xihuan','lluguan') |
+------------------------------------+
| daweixihuanlluguan                 |
+------------------------------------+
1 row in set

mysql> select lcase('A')
;
+------------+
| lcase('A') |
+------------+
| a          |
+------------+
1 row in set

mysql> select lcase('AOOOOO
');
+-----------------+
| lcase('AOOOOO') |
+-----------------+
| aooooo          |
+-----------------+
1 row in set

mysql> select lcase('AOOOOO');
+-----------------+
| lcase('AOOOOO') |
+-----------------+
| aooooo          |
+-----------------+
1 row in set

mysql> select ABS('-9');
+-----------+
| ABS('-9') |
+-----------+
|         9 |
+-----------+
1 row in set

mysql> select pi();
+----------+
| pi()     |
+----------+
| 3.141593 |
+----------+
1 row in set


```



1.5.MySQL预处理语句

就是一个 方法  只不过 是 已经加载好的, 只需要你填写一些参数 
就能获得相应的结果

关键词:  prepare

连接词 : from

```
mysql> prepare liwei from 'select * from user where id >?';
Query OK, 0 rows affected
Statement prepared
mysql> set @i = 24;
Query OK, 0 rows affected

mysql> execute liwei;
1210 - Incorrect arguments to EXECUTE
mysql> execute liwei using @i;
+----+--------+-----+-----+----------+
| id | name   | sex | age | province |
+----+--------+-----+-----+----------+
| 25 | 小王八 |   1 |   4 | 纽约     |
| 26 | 小霸王 |   1 |   4 | 上海     |
| 27 | 王尼玛 |   1 |  40 | 深圳     |
| 28 | 王老五 |   0 |   0 | 江苏     |
| 29 | 王麻子 |   0 |   0 | 四川     |
| 30 | 王中王 |   1 |   0 | 贵州     |
| 31 | 王守义 |   1 |   0 | 四川     |
| 32 | 王老吉 |   2 |  88 | 江苏     |
+----+--------+-----+-----+----------+
8 rows in set

mysql> 

```




-------------------

#day2
## 1.6 mysql事务
###是什么?
是多个步骤为一个过程的事务（整体）  

例子:

在学员管理系统中,有学员表,成绩表,讲师表,活动表,会议表,其他表等等

删除一个学员.

需要删除下面这些表!
学员表,成绩表,活动表,会议表,其他表等等

这些数据库的操作语句 就构成一个事务.

###前提

1. 事务使用 INNODB 数据库引擎  

如果你不是INNODB ,开启事务,删除那就真的删除了.

2. 要么成批的sql全部执行,要么不执行
3. 事务用来管理   insert  update  delete 的语句


###事务条件:
原子性   一组事务,要么成功,要么撤回.
稳定性	有非法数据(外键约束),事务撤回
隔离性  事务独立运行.   一个事务,处理后的结果影响到了其他事务,则事务撤回!
可靠性  软件或者硬件崩溃,Innodb 表驱动,会利用日志文件,重构修改.      可靠性  高速度  不可兼得

### 关键字
commit  roolback



```
set autocommit = 0;
-- delete from t3 where id =4;
-- select * from t3;
-- desc t2;
-- show create table t3;

-- -- 1 2 3 5 6
-- savepoint p1;
-- 
-- delete from t3 where id =2;
-- 
-- 
-- -- 1 3 5 6
-- savepoint p2;
-- 
-- 
-- delete from t3 where id =3;
-- 
-- -- 1 5 6
-- savepoint p3;


-- ROLLBACK to p2;

-- ROLLBACK to p1;

-- SELECT * from t3;

commit;

```




##1.8 触发器  trigger

###是什么
监视某种时间,并触发某种操作(商品的添加,订单的删除 等等 连贯操作时候使用)


###触发四要素
1. 监视地点 table
2. 触发时间 (after/ before)
3. 监视事件 (insert/update/delete)
4. 触发事件 (insert/update/delete)


### 例子

```

mysql> insert into t1 values('adc');
    -> //
1136 - Column count doesn't match value count at row 1
mysql> create trigger yu before insert on t2 for each row
    -> begin
    -> insert into a values(20,'safjasdkf');
    -> end//
Query OK, 0 rows affected

mysql> insert into t2 values(200,'chao')
;
    -> //
Query OK, 1 row affected

delimiter ;

```



1.7.MySQL存储（MySQL的自定义函数）10:14-

mysql 函数. 传参调用

适用于  封装后的传参,同样式的sql操作.

例如:  查询用户数据, 查询订单数据    删除  




```


mysql> delimiter //
mysql> create procedure p1()
    -> begin
    -> set @i=1;
    -> while @i<6 do
    -> select * from user where id=@i;
    -> set @i=@i+1;
    -> end while;
    -> end//
Query OK, 0 rows affected
mysql> call p1;
    -> //
+----+------+-----+-----+----------+
| id | name | sex | age | province |
+----+------+-----+-----+----------+
|  1 | bobo |   1 |  88 | 上海     |
+----+------+-----+-----+----------+
1 row in set

+----+--------+-----+-----+----------+
| id | name   | sex | age | province |
+----+--------+-----+-----+----------+
|  2 | 麦克雷 |   1 |  40 | 纽约     |
+----+--------+-----+-----+----------+
1 row in set

+----+--------+-----+-----+----------+
| id | name   | sex | age | province |
+----+--------+-----+-----+----------+
|  3 | 卢西奥 |   0 |  26 | 纽约     |
+----+--------+-----+-----+----------+
1 row in set

+----+------+-----+-----+----------+
| id | name | sex | age | province |
+----+------+-----+-----+----------+
|  4 | 半藏 |   1 |  38 | 东京     |
+----+------+-----+-----+----------+
1 row in set

+----+----------+-----+-----+----------+
| id | name     | sex | age | province |
+----+----------+-----+-----+----------+
|  5 | 法老之鹰 |   0 |  30 | 江苏     |
+----+----------+-----+-----+----------+
1 row in set

Query OK, 0 rows affected

mysql> 


mysql> drop procedure p1;
    -> //
Query OK, 0 rows affected

mysql> call p1;//
1305 - PROCEDURE s67.p1 does not exist
mysql> 

```

3、查看所有procedure的status信息
mysql>show procedure status
4、查看procddure p1()的具体信息
mysql>show create procedure p1
5、删除procedure
mysql>drop procedure p1;






2. 索引的使用情况

序号	情况	使用索引情况
1	where or	都使用不到索引，并进行全表扫描
2	where and	可能
	组合索引	先到先得   status email  查前面的status 有索引 查后面的email就没有索引
3	字段类型不符	使用不到索引
4	like	当%号在第一个字符，使用不到索引
5	is null	可以


### 测试分析sql语句
关键字:   desc  explain
关键字段:  table  keys(索引)  keys_possible(可能用到的索引) rows





###面试题:
什么是组合索引,使用情况?
	再问:  id name  password  建立组合索引 怎么建立?为什么?
	name,password
	因为先到先得,  name查询是多!!!  很少会通过password来查
	先到先得 如何设置我索引?
		根据字段的辨识度来做
	
问: 为什么不分开加索引?而非要加组合索引
		1. 索引不是越多越好.   浪费资源   索引暂用资源,影响插入性能
		2. 根据要加索引的字段辨识度而来. 如果你给辨识度小的字段加索引
			第一, 加了你不常用  第二,影响性能
		3. 尤其是 name pasword 经典的组合索引例子

为什么likt 在% 第一个字符 用不到索引

like %校  会查处当前所有的姓, 再去查名中有没有校   所以 会进行全表扫描




** 组合索引列子 **
```

# 加邮箱字段 插入数据
mysql> alter table users add email varchar(255);
		update users set email = concat(name,'@qq.com');
		insert into users (name,email) values ('jack','jack2@foxmail.com');



# 查询状态 和 email  分析索引使用情况
# email 现在没有索引 所以 用不到索引
mysql> desc select * from users where  status =0  and email like "ja%";


# email加上索引
mysql> alter table users add index ind_email(email);

# 再测试一次
mysql> desc select * from users where  status =0  and email like "ja%";
# 结果 是用了inde_status  就已经查到数据了 .  根据实际查询情况,如果用一个索引就查到数据了. 所以说实际上会有偏差



# 加上一个组合索引
mysql> alter table users add index ind_status_email (status,email);

# 做status email 两个字段的共同查询 分析
mysql> desc select * from users where  status =0  and email like "ja%";



# 得到结果用到组合索引  通过组合索引已经查到数据了. 自身的索引 就不会再用了.


# 再看其他情况


# 把status 和 email 的索引删除 只留  组合索引  ind_status_emial

mysql> alter table users drop index ind_email;
		alter table users drop index ind_status;
# 执行分析
mysql> desc select * from users where email like "ja%";
# email 在后面  查询分析 用不到组合索引

mysql> desc select * from users where  status =0;
# status 在前面  所以 用到了 组合索引



```


