<?php
	//注册页
    require("redis.php");

    if(empty($_POST['username']) || empty($_POST['password'])){
        header("location:reg.php");
    }

    //获取表单数据
    $username = $_POST['username'];
    $password = md5($_POST['password']);
    $age = $_POST['age'];

    //链接Redis服务
    $redis = redisLink();
    //模拟自增ID
    $userId = $redis->incr("nextUserId");
    //将一个用户的信息存入hash 模拟行数据
    $redis->hmset("user:".$userId,array("id"=>$userId,"username"=>$username,"password"=>$password,"age"=>$age));
    //用户ID组成list链表，未来用于分页
    $redis->rpush("userIdList",$userId);
    //准备一个用户名的字符串存ID用户快速登录
    $redis->set("username:".$username.":id",$userId);

    header("location:list.php");