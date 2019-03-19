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

-  is null

-  is not null

-  between A and B 

-  not between A and B 

-  like 

-  not like 

-  in

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



# NoSQL

No-SQL是以**Key-Value**形式存储,不一定遵循传统数据库的基本要求

主要有以下特点:

​	非关系型

​	分布式

​	开源

​	水平可扩展

### 优势

1. 处理超大量的数据
2. 运行在便宜的PC机服务集群上
3. 击碎了性能瓶颈

### 使用场景

1. 对数据高并发读写
2. 对海量数据的高效率存储和访问
3. 对数据的高可扩展性和高可用性



# Redis

### 什么是Redis?

- 远程字典服务器
- 内存级数据库
- 数据结构服务器

### 数据类型

字符串(String)

哈希(Hash)

列表(List)

集合(Set)

有序集合(Sorted set)



## Redis命令

### String

1. set  键  "值"			           设置一个键 , 键存在,则覆盖
2. get  键                                        获取一个键的值,返回值
3. setnx  键  值                             只有当该键不存在时设置一个键的值
4. setex  键  [有效时间]  值         设置一个指定有效期的的键和值
5. ttl    键                                       以秒为单位,返回给定键的剩余时间
6. setrange  键  位置  字符串      替换子字符串(替换长度由子字符串长度决定)
7. mset 键1 值1 键2 值2 . . .        批量设置键和值
8. mget 键1 键2 键3 . . .               批量获取值
9. msetnx 键1 值1 键2 值2 . . .    批量设置不存在
10. getset 键 新值                           获取原值，并设置新值
11. getrange 键 0 4                        获取指定范围的值
12. incr 键                                        指定键的值做加1操作，返回加后的结果（只能加数字）
13. incrby 键 m                               加指定值，键不存在时候会设置键
14. decr 键                                       指定键的值做减1操作，返回减后的结果
15. decrby 键 n                               设置某个键减上指定值
16. append  键 追加字串                给指定key的字符串追加value，返回新字符串值的长度
17. strlen 键名                                 求一个键长度
18. del 键名                                      删除一个键

### Hsahs

1. hset key field value                  设置一个键，在键中保存字段和值
2. hsetnx  键  字段  值                   设置一个键中，不存在的字段和值。如果字段存在则报错（成功返回1，失败返回0）
3. hmset  键  字段1  值1  字段2  值2 …              在一个键中，批量设置字段
4. hget 键 字段                               获取键中的一个指定字段的值
5. hmget 键 字段1 [字段2…]         获取键中一个或多个字段的值
6. hexists 键 字段                           判断指定的字段是否存在于键中
7. hlen 键                                        获取键中的字段数量
8. hkeys 键                                     获取键中的所有字段名
9. hvals 键                                      获取键中所有字段的值
10. hgetall 键                                   获取键中的所有字段和值
11. hincrby 键 字段 指定数            将键中指定字段的值，增加指定的数字
12. hdel 键 字段1 字段2                 删除键中的一个或多个字段

### List

1. lpush 键 值1 [值2…]                从队列左边向队列写入一个或多个值
2. lrange 键 起始下标 终止下标  从队列中获取指定的返回值（从队列左边向右获取）
3. rpush 键 值1 [值2…]               从队列右边向队列写入一个或多个值
4. linsert  键  before|after  原值  新值     在队列中指定元素之前或之后插入新值
5. lset  键  下标  新值                   给队列中指定元素设定新值
6. lrem  键  n  指定值                   从队列中删除n个值为“指定值”的元素
7. ltrim  键  起始下标  结束下标  修剪队列，让队列只保留指定指定范围内的元素
8. lpop  键                                     从指定的队列左面移除一个值
9. rpop  键                                    从指定队列的右边移除一个值
10. rpoplpush 源队列  目标队列  移除源队列的最后一个元素，并把该元素写入目标队列 
11. lindex  键  下标                         获取队列中指定下标元素的值
12. llen  键                                       获得队列的长度

### Sets

1. sadd  键  值1[值2…]                 添加一个或多个元素到集合中
2. smembers  键                          获取集合里面所有的元素
3. srem  键  值1[值2…]                从集合中删除指定的一个或多个元素
4. spop  键                                    随机从集合中删除一个元素，并返回
5. srandmember  键  值             随机返回集合中一个元素，但不删除
6. scard  键                                   获取集合里面元素个数
7. sismember 键  值                    确定一个指定的值是否是集合中的元素
8. sdiff  集合1  集合2                   返回集合1与集合2的差集。以集合1为主
9. sdiffstore 新集合  集合1  集合2    返回集合1和集合2的差集，并把结果存入新集合
10. sinter  集合1  集合2                 获得两个集合的交集
11. sinterstore  新集合  集合1  集合2       获得集合1和集合2的交集，并把结果存入新集合
12. sunion  集合1  集合2               获得指定集合的并集
13. sunionstore  新集合  集合1  集合2      获得指定集合的并集，并把结果保存如新集合
14. smove  源集合  目标集合  值      将指定的值从源集合移动到目标集合

###  Sorted sets

1. zadd  键  分数1  值1  [分数2  值2…]     该命令添加指定的成员到key对应的有序集合中，每个成员都有一个分数
2. zrange  集合  起始下标  截止下标  [withscores]    返回有序集合中，指定区间内的成员
3. zrevrange  集合  起始下标  截止下标  [withscores]    返回有序集合中，指定区间的成员
4. zrangebyscore 集合  起始分数  截止分数  withscores    返回有序集合中score（分数）在指定区间的值
5. zrem  集合  值1  [值2…]                          删除有序集合中指定的值
6. zincrby  集合  增量  值                            给有序集合中指定值的成员的分数（score）值加上增量（increment）
7. zrank  集合  值                                        返回有序集合中指定值的下标，值按照score从小到大排序
8. zrevrank  集合  值                                   返回有序集合中指定值的下标，值按照score从大到小排序
9. zcount  集合  起始分数  截止分数          返回有序集合中，score值在起始分数与截止分数之间的个数
10. zcard  集合                                               返回有序集合元素的个数
11. zremrangebyrank  集合  起始下标  结束下标          删除有序集合中，下标在指定区间的元素
12. zremrangebyscore  集合  起始分数  截止分数         删除有序集合中，分数在指定区间的元素
13. zinterstore  新集合  取交集的集合个数  集合1 集合2      取集合1和集合2的交集，并把结果保存到新集合中
14. zunionstore   新集合  取并集的集合个数  集合1 集合2      取集合1和集合2的并集，并把结果保存到新集合中



Hash类型：适合做数据缓存

List类型：适合做数组搜索

集合类型：适合做好友推送

有序集合类型：适合商品排序



### 键值相关命令

1. keys  键名                                                   按照键名查找指定的键。支持通配符
2. exists  键名                                                 确认一个键是否存在
3. del  键名                                                     删除一个键
4. expire  键  秒                                             设置一个键的过期时间，如果键已经过期，将会被自动删除
5. ttl  键                                                           以秒为单位，返回键的剩余生存时间
6. select  数据库号                                         选择一个数据库
7. move  键  数据库号                                   将当前数据库的键移动到指定的数据空中
8. randomkey                                                从当前数据库返回一个随机的键。如果当前库没有任何键，则返回nil
9. rename  旧名  新名                                  重命名键
10. type  键                                                      返回键类型

### 服务器相关命令

1. ping                                                           测试服务器是否可以连接
2. echo  字符串                                            在命令行输出字符串
3. quit                                                           退出redis数据库
4. save                                                          保存所有的数据
5. dbsize                                                       返回当前库中键的数量
6. info                                                           获取服务器的详细信息
7. config get 参数                                        获取redis服务器配置文件中的参数。支持通配符
8. flushdb                                                     删除当前数据库中所有的数据
9. flushall                                                      删除所有数据库中所有的数据