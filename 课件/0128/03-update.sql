--  更新数据 

-- 全部更新
-- update `表名` set `字段名1`="值1", `字段名2`="值2", ...
update `user` set `sex` = 2, `status` = 2


-- 局部更新 (带条件更新)
-- update `表名` set `字段名1`="值1", `字段名2`="值2", ... where 条件
update `user` set `sex` = 2, `status` = 2 where `birthday` < '1990-01-01'



