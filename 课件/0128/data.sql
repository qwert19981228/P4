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

insert into `user`(`nickname`, `pwd`, `tel`, `sex`, `birthday`, `address`, `status`, `regtime`) values
('小王', md5('123456'), '15000000001', 1, '2002-12-03', '青花楼老宋床底下', 1, '1548384200'),
('亚瑟', md5('123456'), '15000000002', 1, '1970-10-01', '召唤师峡谷', 1, '1548384200'),
('钟馗', md5('123456'), '15000000003', 1, '1995-11-11', '召唤师峡谷', 2, '1548382600'),
('老宋', md5('123456'), '15000000004', 1, '2006-07-18', '宝马车上',   1, '1548382537'),
('貂蝉', md5('123456'), '15000000005', 2, '2017-02-13', '吕布or董卓别墅',   1, '1548384240'),
('本伟', md5('123456'), '17000000001', 1, '1990-10-10', '绝地海岛监狱', 1, '1548384200'),
('无名', md5('123456'), '17000000002', 2, '1941-05-27', null,   2, '1548380735'),
('路飞', md5('123456'), '17000000003', 1, '1999-09-01', '海贼王岛',   1, '1548384270'),
('鸣人', md5('123456'), '17000000004', 1, '1985-12-13', '木叶忍者村', 1, '1548384200'),
('奥九马', md5('123456'), '17000000005', 1, '1957-11-25', '黑宫顶层', 1, '1548384204'),
('晋四', md5('123456'), '17000000006', 1, '2015-06-06', null, 2, '1548384213'),
('星爷', md5('123456'), '17000000007', 1, '1962-10-10', '太师华府', 1, '1548381853'),
('波老师', md5('123456'), '13000000001', 2, '2000-01-01', '老王隔壁', 1, '1548384200'),
('苍老师', md5('123456'), '13000000002', 2, '2001-10-01', '老王隔壁', 1, '1548384259'),
('小泽', md5('123456'), '13000000003', 2, '2002-06-01', '老王隔壁', 1, '1548384200'),
('小飞飞', md5('123456'), '13000000004', 1, '2009-09-09', '老王下面', 1, '1548384200');






create table if not exists `salary`(
	`id` 	int 		auto_increment 	primary key,
	`uid` 	int 		comment 'user表中的用户id',
	`dep` 	varchar(10) 	not null comment '部门',
	`money` 	decimal(10,2) 	not null comment '工资'
)engine=myisam default charset=utf8;

insert into `salary`(`uid`, `dep`, `money`) values
(5, '技术部', 50000),
(11, '技术部', 5888),
(12, '技术部', 88888),
(1, '公关部', 9000),
(13, '公关部', 11000),
(14, '公关部', 15000),
(15, '公关部', 10000),
(2, '保安部', 6000),
(3, '保安部', 51000),
(8, '保安部', 30000),
(4, '销售部', 3000),
(6, '销售部', 5000),
(7, '销售部', 100000),
(9, '保洁部', 8000),
(10, '财务部', 12000),
(16, '财务部', 9000);