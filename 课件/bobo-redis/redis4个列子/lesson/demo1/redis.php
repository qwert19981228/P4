<?php

	header("content-type:text/html;charset=utf-8");

	//apache 链接时长不失效
	ini_set('default_socket_timeout',-1);
	
	$redis = new Redis();

	//使用pconnect 长连接
	$redis->pconnect('127.0.0.1', 6379);

	//认证
	$redis->auth('123456');
