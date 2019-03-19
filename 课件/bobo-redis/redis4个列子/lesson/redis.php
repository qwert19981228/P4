<?php

	//redis测试
	$redis = new Redis();
	
	//连接服务
	$redis->connect('127.0.0.1', 6379);
	
	//可选 验证
	$redis->auth('123456');
	
	//$redis->set('myName', 'jack');
	
	//echo $redis->get('myName');
	
	//设置多个值到hash中
	$redis->hmset('user:1', array('name'=>'tom', 'age'=>19, 'sex'=>1));
	//获取多个
	$user1 = $redis->hmget('user:1', array('name', 'sex'));
	
	var_dump($user1);
	
	$redis->close();
	
	