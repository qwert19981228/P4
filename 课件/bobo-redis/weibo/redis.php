<?php
	header("content-type:text/html;charset=utf-8");
    //实例化
    $redis = new Redis();
    //连接服务器
    $redis->pconnect("localhost");
    //授权
	$redis->auth("123");

	
