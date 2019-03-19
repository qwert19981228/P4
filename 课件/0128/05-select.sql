-- 查询数据


-- 完整语句格式
-- select  	字段名, 字段名, ...
-- [ from 表名 ]
-- [ where ]
-- [ group by ]
-- [ having ]
-- [ order by ]
-- [ limit ]


-- 1. 查询函数
select now(); 	# 当前时间
select unix_timestamp(); # 当前时间戳
select version(); # 当前版本
select md5('123456'); # md5加密


-- 2. 算术运算
select 10 + 20;
select 10 % 20;


-- 3. 查询user表中的 所有数据
--  select * from 表名
select * from user;

/*
	* : 代表所有的字段, 你需要的和不需要的 都查出来, 影响的效率. 建议少用
*/


-- 4. 查询user表中 的 部分字段数据
-- select 字段名1, 字段名2, ....  from 表名
select id, nickname, tel from user;


-- 5. 条件查询
-- 5.1 精确查询
-- 	字段名 = 值
select nickname, tel, sex
from user
where sex = 2


-- 5.2 空查询
--  is null
--  is not null
select nickname
from user
where address is null;


select nickname
from user
where address is not null;

-- 5.3 区间查询
--  	between A and B
--  	not between A and B
select nickname, birthday
from user
where birthday between '1990-01-01' and '1999-12-31';


select nickname, birthday
from user
where birthday not between '1990-01-01' and '1999-12-31';

-- 5.4 模糊查询
--  字段名 like "%值%"
--  字段名 like "值%"
--  字段名 like "%值"


-- % : 匹配0个, 1个 或多个字符  
-- _ 下划线: 只匹配 1个字符

select nickname
from user
where nickname like "%老师%"


select nickname
from user
where nickname like "小%"


select nickname
from user
where nickname like "小__"


-- 5.5 in 操作

-- 查询 address 是 "召唤师峡谷" 或 "老王隔壁"的所有昵称
select nickname, address
from user
where address in ('召唤师峡谷', '老王隔壁');

-- 5.6 逻辑运算
-- 	逻辑与: and 		
--  逻辑或: or
--  逻辑非: not
--  逻辑异或: xor 	相异为真, 相同为假

-- 查询所有 00后男生的昵称
select nickname
from user
where sex = 1 and birthday >= '2000-01-01';

-- 查询所有 00后状态为激活的男生的昵称
select nickname
from user
where sex = 1 and birthday >= '2000-01-01' and status = 1;

/*
	运算符:
		算术: + - * / % 
		比较: 
			= != 
			< <=
			> >=
			is null
			is not null
			between A and B 
			not between A and B 
			like 
			not like 
			in
		逻辑:
			and
			or
			not
			xor
 */








