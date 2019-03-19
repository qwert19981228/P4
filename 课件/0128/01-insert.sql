-- 插入数据 (增)

-- 1. 插入一条 完整的数据
-- insert into `表名` values(值1, 值2, ...)
INSERT INTO `user` VALUES(null, '小王', md5('123456'), '15000000000', default, '2019-01-28', '老宋隔壁', 2, unix_timestamp() );

-- 注意:
--  	1. 插入所有的字段值
--  	2. 带有 auto_increment属性的字段, 可以用null 代替
--  	3. 带有 default 属性的字段, 可以用 default 代替
--  	4. 带有 unique 属性的字段, 避免重复

-- 2. 插入一条 部分字段的数据
-- insert into `表名`(字段名1, 字段名2, ...)  values(值1, 值2, ...)

INSERT INTO `user`(`tel`, `pwd`, `nickname`) VALUES('15000000001', MD5('123456'), '亚瑟');
INSERT INTO `user`(`tel`, `pwd`, `nickname`) VALUES('15000000001', MD5('123456'), '亚瑟2号');

-- 注意:
--  	1. 前面有多少字段名, 后面就得有多少字段值
--  	2. 含有 not null 属性的字段名, 必须插入
--  	3. 带有 unique 属性的字段, 避免重复


-- 3. 插入多条 完整的数据
-- insert into `表名` values(值1, 值2, ...), (值1, 值2, ...), (值1, 值2, ...), ...


-- 4. 插入多条 部分字段的数据
-- insert into `表名`(字段名1, 字段名2, ...)  values(值1, 值2, ...), (值1, 值2, ...), ...

