# MySQL分区 #
>当MySQL中一个表的总记录数超过1000万条，性能会大幅下降么？

>在软件优化层面主要：系统配置、SQL语句优化、主从分离，当然还有拆表！

垂直分表

对于垂直分表，它将一个N1+N2个字段的表Tab拆分成N1字段的子表Tab1和(N2+1)字段的子表Tab2；其中子表Tab2包含了关于子表Tab1的主键信息，否则两个表的关联关系就会丢失。当然垂直分表会带来程序端SQL的修改，若是应用程序已经应用很长的一段时间，然后程序的升级将是耗时而且易出错的，即升级的代价将会很大。

![](http://i.imgur.com/lqzlzOU.png)

水平分表

水平分区技术将一个表拆成多个表，比较常用的方式是将表中的记录按照某种Hash算法进行拆分，简单的拆分方法如取模方式。同样，这种分区方法也必须对前端的应用程序中的SQL进行修改方可使用。而且对于一个SQL，它可能会修改两个表，那么你必须得写成2个SQL语句从而可以完成一个逻辑的事务，使得程序的判断逻辑越来越复杂，这样也会导致程序的维护代价高，也就失去了采用数据库的优势。因此，**分区技术可以有力地避免如上的弊端，成为解决海量数据存储的有力方法。**

![](http://i.imgur.com/Qvr8jcw.png)

>MySQL的分区技术文件部署上与水平分表相似，但逻辑上对于应用程序来说是一张表
主要有 4 种分区类型：

1. 	RANGE
2. 	LIST　　
3. 	HASH　
4. 	KEY

>**我们使用MySQL官网的音像店分区作为讲解实例！**

## RANGE分区 ##
>保存有20家音像店的职员记录表，如果你想将其分成4个小分区。

	mysql>CREATE TABLE employess(
			id INT NOT NULL,
			fname VARCHAR(30),
			lname VARCHAR(30),
			hired DATE NOT NULL DEFAULT '1997-01-01',
			separated DATE NOT NULL DEFAULT '9999-12-31',
			job_code INT NOT NULL,
			store_id INT NOT NULL
		)PARTITION BY RANGE(store_id)(
			PARTITION p0 VALUES LESS THAN(6),
			PARTITION p1 VALUES LESS THAN(11),
			PARTITION p2 VALUES LESS THAN(16),
			PARTITION p3 VALUES LESS THAN(21)
		);

>保存有20家音像店的职员记录表，把不同时期离职的员工进行分别存储。

	mysql>CREATE TABLE employess(
			id INT NOT NULL,
			fname VARCHAR(30),
			lname VARCHAR(30),
			hired DATE NOT NULL DEFAULT '1997-01-01',
			separated DATE NOT NULL DEFAULT '9999-12-31',
			job_code INT NOT NULL,
			store_id INT NOT NULL
		)PARTITION BY RANGE(YEAR(separated))(
			PARTITION p0 VALUES LESS THAN(1991),
			PARTITION p1 VALUES LESS THAN(1996),
			PARTITION p2 VALUES LESS THAN(2001),
			PARTITION p3 VALUES LESS THAN(MAXVALUE)
		);
	
请查看此时文件部署情况
	
## LIST分区 ##
>保存有20家音像店的职员记录表，分布在4个经销权地区。

![](http://i.imgur.com/y3PuF2g.png)

	mysql>CREATE TABLE employess(
			id INT NOT NULL,
			fname VARCHAR(30),
			lname VARCHAR(30),
			hired DATE NOT NULL DEFAULT '1997-01-01',
			separated DATE NOT NULL DEFAULT '9999-12-31',
			job_code INT NOT NULL,
			store_id INT NOT NULL
		)PARTITION BY LIST(store_id)(
			PARTITION pNorth VALUES IN (3,5,6,9,17),
			PARTITION pEast VALUES IN (1,2,10,11,19,20),
			PARTITION pWest VALUES IN (4,12,13,14,18),
			PARTITION pCentral VALUES IN (7,8,15,16)
		);

请查看此时文件部署情况

## HASH分区 ##
>HASH分区主要用来确保数据在预先确定数目的分区中平均分布。

>保存有20家音像店的职员记录表，把不同时期加入的员工进行分别存储，将日期字段hired（即入职时间）作为一个key。

	mysql>CREATE TABLE employess(
			id INT NOT NULL,
			fname VARCHAR(30),
			lname VARCHAR(30),
			hired DATE NOT NULL DEFAULT '1997-01-01',
			separated DATE NOT NULL DEFAULT '9999-12-31',
			job_code INT NOT NULL,
			store_id INT NOT NULL
		)PARTITION BY HASH(YEAR(hired)) PARTITIONS 4;

## KEY分区 ##
>与HASH分区类似，但Key可以不是整型，如字符串等字段。

## COMPOSITE分区 ##
>多种分区类型组合的模式，比如子分区

>子分区是针对RANGE/LIST类型的分区表中的每个分区再次分割，可以是HASH/KEY等类型。
	
>保存有20家音像店的职员记录表，如果你想将其分成4个小分区。

	mysql>CREATE TABLE employess(
			id INT NOT NULL,
			fname VARCHAR(30),
			lname VARCHAR(30),
			hired DATE NOT NULL DEFAULT '1997-01-01',
			separated DATE NOT NULL DEFAULT '9999-12-31',
			job_code INT NOT NULL,
			store_id INT NOT NULL
		)PARTITION BY RANGE(store_id) SUBPARTITION BY HASH(store_id) SUBPARTITIONS 2(
			PARTITION p0 VALUES LESS THAN(6),
			PARTITION p1 VALUES LESS THAN(11),
			PARTITION p2 VALUES LESS THAN(16),
			PARTITION p3 VALUES LESS THAN(21)
		);

## 分区管理 ##
### 1、删除分区 ###

	ALTER TABLE employess DROP PARTITION p0;

### 2、重建分区 ###

RANGE分区重建
	
	ALTER TABLE employess REORGANIZE PARTITION p0, p1 INTO(PARTITION p0 VALUES LESS THAN(1996));
将原来的0区和1区的数据合并放到0区

LIST分区重建
	
	ALTER TABLE employess REORGANIZE PARTITION pNorth, pEast INTO(PARTITION pNorth VALUES IN(1,2,3,5,6,9,10,11,17,19,20));
将原来的北区和东区的数据合并放到北区

HASH/KEY分区重建
	
	ALTER TABLE employess REORGANIZE PARTITION COALESCE PARTITION 2；	
	
用REORGANIZE方法重建分区数量变为2

### 3、新增分区 ###

新增RANGE分区
	
	ALTER TABLE employess ADD PARTITION (PARTITION p4 VALUE LESS THAN());
范围要合理，往后叠加范围在之前的以外。

新增LIST分区
	
	ALTER TABLE employess ADD PARTITION (PARTITION pSouth VALUE IN(21,22,23,24,25));

新增HASH/KEY分区
	
	ALTER TABLE employess ADD PARTITION PARTITIONS 6;
分区扩展到6个。

## 不同分区技术的优缺点 ##

| 分区类型        | 优点         | 缺点   |
| -------------  |:-------------|:----- |
| RANGE  | 适合日期，支持复合分区 | 有限的分区 |
| LIST  | 适合固定取值的列，支持复合分区 | 有限的分区，插入数据值不在范围内数据丢失 |
| HASH | 线性HASH是的增删合并等都很快捷 | 线性HASH数据分布不均匀，而一般HASH的数据分布较均匀 |
| KEY | 列可以为字符串等非整型 | 效率较之前的低，因为有复杂函数（SHA和MD5等） |

## InnoDB表的分区 ##
>只有独立表空间类型的innodb才支持分区，固要了解InnoDB表的存储方式：共享和独立。

- 共享表空间

	一个库所有的表数据、索引文件都放在一个文件中，默认文件名为 ibdata1 初始化大小10MB。

- 独立表空间

	每一个表都会生成独立的文件俺存储，一个 .frm 表描述文件，一个 .ibd 表数据索引文件。

查看当前innodb类型：
	
	mysql>show variables like "innodb_file_per_table";
	ON为独立   OFF为共享

设置独立表空间：
	
- 临时修改
	
	mysql>set innodb_file_per_table = 1;
- 永久修改
	
	my.ini
	添加
	innodb_file_per_table=1;
	重启服务

# MySQL分区实验 #
## 一、	准备 ##
1、	创建分区表（按日期的年份拆分）

	CREATE TABLE part_tab ( 
		c1 int default NULL, 
		c2 varchar(30) default NULL, 
		c3 date default NULL
	) engine=myisam 
	PARTITION BY RANGE (year(c3)) (
		PARTITION p0 VALUES LESS THAN (1995),
		PARTITION p1 VALUES LESS THAN (1996),
		PARTITION p2 VALUES LESS THAN (1997),
		PARTITION p3 VALUES LESS THAN (1998),
		PARTITION p4 VALUES LESS THAN (1999),
		PARTITION p5 VALUES LESS THAN (2000),
		PARTITION p6 VALUES LESS THAN (2001),
		PARTITION p7 VALUES LESS THAN (2002),
		PARTITION p8 VALUES LESS THAN (2003),
		PARTITION p9 VALUES LESS THAN (2004),
		PARTITION p10 VALUES LESS THAN (2010),
		PARTITION p11 VALUES LESS THAN MAXVALUE 
	);

注意最后一行，考虑到可能的最大值

2、	创建未分区表

	create table no_part_tab (
		c1 int(11) default NULL,
		c2 varchar(30) default NULL,
		c3 date default NULL
	) engine=myisam;

3、	插入测试数据
快速插入数据使用存储——通过存储创建800万条测试数据

	\d //
	create procedure load_part_tab()
	begin
	set @i=1;
	while @i < 8000001 do
	insert into part_tab
	values (@i,'test',adddate('1995-01-01',(rand(@i)*36520)mod 3652));
	set @i = @i + 1;
	end while;
	end //
	\d ;

4、	执行存储

	call load_part_tab();

5、	观察  watch -n 1 ls -lh /usr/local/mysql/data/test

6、	将分区表数据插入未分区表

	select * from part_tab into outfile '/tmp/part.txt';
	load data infile '/tmp/part.txt' into table no_part_tab;

## 二、	测试 ##
1、	对比两表查询性能

	select count(*) from part_tab where c3 > date '1995-01-01' and c3 < date '1995-12-31';
	
	select count(*) from no_part_tab where c3 > date '1995-01-01' and c3 < date '1995-12-31';
	
对比两表查询时间

2、	分析查询

	explain select count(*) from part_tab where c3 > date '1995-01-01' and c3 < date '1995-12-31'\G
	
	explain select count(*) from no_part_tab where c3 > date '1995-01-01' and c3 < date '1995-12-31'\G

对比两表rows行数

3、	创建索引

	create index idx_of_c3 on no_part_tab (c3);
	
	create index idx_of_c3 on part_tab (c3);

4、注意：添加主键
	
	alter table part_tab add primary key(c1);
	#报错 分区是针对c3的，你的主键一定要包含c3 	
	alter table part_tab add primary key(c1,c3);

## 分区实验总结 ##

1. 分区和未分区占用文件空间大致相同 （数据和索引文件）
1. 如果查询语句中有未建立索引字段，分区时间远远优于未分区时间
1. 如果查询语句中字段建立了索引，分区和未分区的差别缩小，分区略优于未分区。
1. 对于大数据量，建议使用分区功能。
