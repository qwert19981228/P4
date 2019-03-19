-- 聚合函数
-- count() 		统计
select count(`id`) from `user`;

-- sum() 		求和
select sum(`id`) from `user`;


-- avg() 		平均值
select avg(`id`) from `user`;


-- max()		最大值
-- min()		最小值
select max(`id`) from `user`;



-- 字符串拼接函数
-- concat( 字符串 或 字段名,   字符串 或 字段名, ...  )
select concat(`nickname`, '----', `tel`, '---', `sex` ) from `user`;

