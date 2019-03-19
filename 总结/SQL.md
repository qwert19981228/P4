# 数据库

1. 定义

   是按照数据结构来组织, 存储 和 管理数据的 仓库

   组成: 

   ​	库  database

   ​	表  table

   库中包含了 表

   表中包含了 数据

2. 分类

   关系型数据库

   MySQL, SQLServer, Oracle ...

   优点:

   ​	保持数据的一致性

   ​	擅长做复杂数据查询

   ​	支持事务

   缺点:

   ​	读写性能比 非关系的差一点.  尤其是 海量数据的高效率读写

   ​	表结构固定, 不灵活

   非关系型数据库

   Redis, MongoDB, ...

   优点:

   ​	读写速度快

   ​	格式灵活

   ​	开源

   缺点:

   ​	表结构复杂, 导致复杂查询能力较弱

   ​	不支持事务

3. 注释

   /* 多行注释 * /

    -- 单行

   #单行

    注意:

   ​	 单行注释符  与  注释内容 之间至少保留一个空格

4. 基本语法

   命令大写, 自定义名字小写

   自定义名字 不能使用关键字

   每条命令 均已 分号结尾.



## 常见命令

1. 设置密码

   set password = password('密码')

2. 查看数据库

   show databases;    复数

3. 创建数据库

   create database ` 库名 `;

   create database if not exists ` 库名 `;

   create database if not exists ` 库名 ` default charset=编码;

   ​	注意:

   ​		1) 编码不要写成utf-8,  写成 utf8, 中间没有 "-".

   ​		2) if not exists 判断库若存在 , 则不创建

   ​						库若不存在, 则创建

   ​		3) 反引号 具有屏蔽关键字的作用. 

   ​		推荐:  库名, 表名, 字段名 最好都加上反引号

4. 删除数据库

   drop database `库名`;

5. 使用数据库

   use `库名`;

6. 查看数据表

   show tables;

7. 创建数据表

   create table if not exists `表名`(
        `字段名`  字段类型   字段属性,
        `字段名`  字段类型   字段属性,
       ...
        `字段名`  字段类型   字段属性    (最后一个字段的分号, 不能写)

   )engine=引擎 default charset=编码;

8. 删除数据表

   drop table `表名`;

9. 查看表结构

   desc `表名`;

10. 查看建表语句

    show create  table `表名`;





## 插入数据

1. 插入一条完整的数据

   insert into ``表名``  values(值1,值2,.  .  .)

   ```mysql
   INSERT INTO `user` VALUES (null,'小王',md5('123456'),'12345678901',default,'2019-01-28','老宋隔壁',2,unix_timestamp());
   ```

   注意

   - 插入所有的字段值
   - 带有 auto_increment属性的字段,可以用null代替
   - 带有default属性的字段,可以用default代替
   - 带有unique属性的字段,避免重复

2. 插入一条部分字段的数据

   insert into  ``表名`` (字段名1,字段名2, . . .) values (值1,值2, . . .)

   ```mysql
   INSERT INTO `user`(`tel`, `pwd`, `nickname`) VALUES('15000000001', MD5('123456'), '亚瑟');
   INSERT INTO `user`(`tel`, `pwd`, `nickname`) VALUES('15000000001', MD5('123456'), '亚瑟2号');
   ```

   注意

   - 前面有多少字段名,后面就得有多少字段值
   - 含有not null 属性的字段名,必须插入
   - 带有unique属性的字段,避免重复

3. 插入多条完整的数据

   insert into ``表名`` values (值1,值2, . . .) , (值1,值2, . . .) , (值1,值2, . . .), . . .

4. 插入多条部分字段的数据

   insert into ``表名`` (字段名1,字段名2, . . .) values (值1 , 值2 , . . .) , (值1, 值2 , . . .) ,  . . . 



## 删除数据

1. 删除一张表的所有数据

   delete from ``表名``

2. 删除一张表中部分数据

   delete from ``表名`` where 条件

   ```mysql
   delete from `user` where `sex` = 2
   ```

3. 删除一张表中 按照排序的前几条[满足条件]数据

   delete from ``表名`` [where 条件] order by 排序依据 limit 行数

   ```mysql
   delete from `user` order by `birthday` asc limit 5; 
   ```

如果为了删除整张表的数据,不建议用delete,效率太低,消耗太高

truncate table ``表名``

小结

- delete 清除数据 ,不会删表,auto_crement 不受影响
- truncate 清除结构 ,先删表结构,再重构表结构,auto_crement重新从1开始计算



## 更新数据

1. 全部更新

   update `表名` set  `字段名1` = "值1" ,  `字段名2` = "值2" , . . . 

   ```mysql
   update `user` set `sex` = 2, `status` = 2
   ```

2. 局部更新(带条件更新)

   update `表名` set `字段名1` = "值1" , `字段名2` = "值2", . . . where 条件

   ```mysql
   update `user` set `sex` = 2, `status` = 2 where `birthday` < `1990-01-01`
   ```



## 聚合函数

- count( )	统计
  - select count(`id`) from `user`;
- sum( )	求和
  - select sum(`id`) from `user`;
- avg( )	平均值
  - select avg(`id`) from `user`;
- max( )	最大值
- min( )	最小值
  - select max(`id`) from `user`;
  - select min(`id`) from `user`;
- 字符串拼接函数
- concat(字符串或字段名,字符串或字段名, . . .)
  - select concat(`nickname` ,  '----' , `tel` ,'---',`sex` ) from `user`;



## 查询数据

##### 完整语句格式

- select  字段名 , 字段名 , . . .
- [from 表名]
- [where]
- [group by]
- [having]
- [order by]
- [limit]



##### 公式

查询函数

select now( );				#当前时间

select unix_timestamp( );	#当前时间戳

select version( );			#当前版本

select md5('123456');		#md5加密

算术运算

select 10 + 20;

select 10 % 20;

查询user表中的所有数据

select * from user;

`*` 代表所有的字段,你需要的和不需要的都查出来,影响的效率,建议少用

查询user表中的部分字段数据

select 字段名1,字段名2, . . . from 表名

select id , nickname , tel from user;

条件查询

1. 精确查询

   **字段名 = 值**

   select nickname , tel , sex

   from user

   where sex = 2

2. 空查询

   **is null** 

   **is not null**

   select nickname

   from user

   where address is null;

   

   select nickname

   from user

   where address is not null;

3. 区间查询

   **between A and B**

   **not between A and B**

   select nickname , birthday

   from user

   where birthday between '1990-01-01' and '1999-12-31';

   

   select nickname , birthday

   from user

   where birthday not between '1990-01-01' and '1999-12-31'; 

4. 模糊查询

   **字段名 like "%值%"**

   **字段名 like "值%"**

   **字段名 like "%值"**

   **% : 匹配0个,1个或多个字符**

   **_下划线: 只匹配 1个字符**

   select nickname

   from user

   where nickname like "%老师%"

   

   select nickname

   from user

   where nickname like "%小"

   

   select nickname

   from user

   where nickname like "小__"

5. in 操作

   查询 address 是 "召唤师峡谷" 或 "老王隔壁"的所有昵称

   select nickname , address

   from user

   where address in ("召唤师峡谷","老王隔壁");

6. 逻辑运算

   逻辑与 : and

   逻辑或 : or

   逻辑非 : not

   逻辑异或 : xor 相异为真,相同为假



##### 运算符

算术: + - * / % 
比较: 

- = != 
- < <=
- is null
- is not null
- between A and B 
- not between A and B 
- like 
- not like 
- in

逻辑:

- and
- or
- not
- xor





##### 完整公式

- select all| distinct  * | 字段名 | 表名.字段名 | 字段名 as 别名 | 函数
- [ FROM 表名1 | 表名1 as 别名1 |表名1, 表名2, ... ]
- [ WHERE 条件 ]
- [ GROUP BY 分组依据] 
- [ HAVING 筛选条件]
- [ ORDER BY 排序依据 ] 
- [ LIMIT 键,行 ]; 



group by  分组操作

```mysql
-- 查询salary表中每个部门 各有多少人
SELECT dep, count(id) 
FROM salary
GROUP BY dep;
```



having 筛选操作

配合 group by 使用

```mysql
-- 查询salary表中人数超过2个的 部门
SELECT dep, count(id)
FROM salary
GROUP BY dep
HAVING count(id) > 2;
```



嵌套查询

```mysql
SELECT uid
FROM salary
WHERE money in (SELECT max(`money`) FROM salary GROUP BY dep);
```



多表查询

SELECT 字段 

FROM 表名1, 表名2, ...

WHERE 关系声明

- from 表名可以有多个

- select 可查询的字段 是所有表的字段总和

- where 必须写, 必须声明表与表之间的关系

  ​		关系个数最少是:  表个数 - 1 

```mysql
-- 查询所有的人的用户id, 昵称, 电话, 部门, 工资
SELECT user.id, nickname, tel, dep, money
FROM user, salary
WHERE user.id = salary.uid;
```



别名 as

- as 写在表名 或 字段名的 后面. 有时可省略, 用 空格隔开

  ```mysql
  SELECT u.id, nickname, tel, dep, money
  FROM user as u, salary as s
  WHERE u.id = s.uid
  ```



order 排序

- 按照 工资由高到低 排序, 查看昵称, 部门, 工资
- desc 降序  asc 升序

```mysql
SELECT nickname, dep, money
FROM salary s, user u
WHERE u.id = s.uid
ORDER BY money desc(asc)
```



limit 分页

- limit key,rows

```mysql
SELECT id, nickname
from user
limit 0,5

SELECT id, nickname
from user
limit 5,5
```



取消重复

```mysql
-- 查询该公司 一共有哪些部门
select distinct dep
from salary
```



## pymysql

> 在 Python 中 ,pymysql 来操作数据库



### 操作步骤

1. 安装pymysql

   进入 cmd

   输入 pip install pymysql

2. python连接数据库

   pymysql.connect('主机或IP','用户名','密码','库名',charset="编码")

3. 创建游标

   db对象.cursor( )

4. 执行sql

   游标.execute(sql语句)

5. 获取游标数据

   游标.fetchone( )		获取一条数据,以一维元组接收

   游标.fetchall()		获取 所有数据,以二维元组接收

   游标.rowcount属性	获取执行execute( ) 所影响的行数

   当数据全部获取完之后，再获取，则返回none

6. cgi 接收get 或 post 数据的方法

   cgi.FieldStorage( )

7. 开启cgi 错误提示

   cgitb.enable( )

8. python 中另类的三元运算

   true环境 if 条件 else false 环境

9. 关闭游标

   游标对象.close( )

10. 关闭数据库

    库对象.close( )