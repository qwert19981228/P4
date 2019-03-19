-- 完整语句
SELECT   ALL|DISTINCT    * | 字段名 | 表名.字段名 | 字段名 as 别名 | 函数
[ FROM 表名1 | 表名1 as 别名1 |表名1, 表名2, ... ]
[ WHERE 条件 ]
[ GROUP BY 分组依据] 
[ HAVING 筛选条件]
[ ORDER BY 排序依据 ] 
[ LIMIT 键,行 ]




-- group by 分组操作


-- 查询salary表中每个部门 各有多少人
SELECT dep, count(id) 
FROM salary
GROUP BY dep

-- 查询user表中 男女生各多少人
SELECT sex, count(id)
FROM user
GROUP BY sex


-- having 筛选操作
-- 配合group by 使用


-- 查询salary表中人数超过2个的 部门
SELECT dep, count(id)
FROM salary
GROUP BY dep
HAVING count(id) > 2


-- 查询salary表中, 人数超过2个, 工资超过9999 的部门
SELECT dep
FROM salary
WHERE `money` > 9999
GROUP BY dep
HAVING count(id) > 2;


#--------------------------------------------------


-- 查询salary表中每个部门的最高工资
SELECT dep, max(`money`)
FROM salary
GROUP BY dep


-- 查询salary表中每个部门最高工资的那个uid
SELECT uid
FROM salary
WHERE money in (51000, 8000, 15000, 88888, 12000, 100000)	


-- 嵌套查询
SELECT uid
FROM salary
WHERE money in (SELECT max(`money`) FROM salary GROUP BY dep)	



-- 多表查询
SELECT 字段 
FROM 表名1, 表名2, ...
WHERE 关系声明

# from 表名可以有多个
# selec 可查询的字段 是所有表的字段总和
# where 必须写, 必须声明表与表之间的关系
#  		关系个数最少是:  表个数 - 1 



-- 查询所有的人的昵称, 电话, 部门, 工资
SELECT nickname, tel, dep, money
FROM user, salary
WHERE user.id = salary.uid


-- 当查询多表中, 重复的字段时??
-- 查询所有的人的用户id, 昵称, 电话, 部门, 工资
SELECT user.id, nickname, tel, dep, money
FROM user, salary
WHERE user.id = salary.uid


-- 别名 as
--  	as 写在表名 或 字段名的 后面. 有时可省略, 用 空格隔开
SELECT u.id, nickname, tel, dep, money
FROM user as u, salary as s
WHERE u.id = s.uid

SELECT count(ID) as total
FROM user

SELECT count(ID) total
FROM user



create table  `test`(
	`dep` 		varchar(20),
	`money` 		decimal(10,2)
)engine=myisam default charset=utf8



-- 查询每个部门最高工资的人的uid
SELECT s.uid
FROM  salary as s, test as t
WHERE s.dep = t.dep and s.money = t.money


-- 查询每个部门的最高工资
SELECT dep, max(`money`) as money
FROM salary
GROUP BY dep


SELECT s.uid
FROM  salary as s, (SELECT dep, max(`money`) as money FROM salary GROUP BY dep) as t
WHERE s.dep = t.dep and s.money = t.money



-- 查询每个部门最高工资的那个人的昵称, 部门, 电话, 工资, 用户id
SELECT u.id, nickname, s.dep, tel, s.money
FROM  salary as s, user as u, (SELECT dep, max(`money`) as money FROM salary GROUP BY dep) as t
WHERE s.dep = t.dep and s.money = t.money and s.uid = u.id




-- order 排序
-- 按照 工资由高到低 排序, 查看昵称, 部门, 工资

SELECT nickname, dep, money
FROM salary s, user u
WHERE u.id = s.uid
ORDER BY money desc

SELECT nickname, dep, money
FROM salary s, user u
WHERE u.id = s.uid
ORDER BY money asc

SELECT nickname, dep, money
FROM salary s, user u
WHERE u.id = s.uid
ORDER BY money 



-- limit 分页
--  limit key,rows

SELECT id, nickname
from user
limit 5


SELECT id, nickname
from user
limit 0,5

SELECT id, nickname
from user
limit 5,5



-- 取消重复
-- 
-- 查询该公司 一共有哪些部门
select distinct dep
from salary



