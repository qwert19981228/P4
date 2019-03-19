<?php
    require("redis.php");

    var_dump($_POST);

    if(empty($_POST['username']) || empty($_POST['password'])) {
        header("location:login.php");
        exit;
    }

    $username = $_POST['username'];
    $password = $_POST['password'];

    $redis = redisLink();
    //根据用户名获取userid
    $userId = $redis->get("username:".$username.":id");
    //验证id是否存在
    if(!$userId) {
        header("location:login.php");
        exit;
    }
    $realpassword = $redis->hget("user:".$userId,"password");
    //验证密码是否一致
    if(md5($password) != $realpassword) {
        header("location:login.php");
        exit;
    }
    
    $auth = md5(time().$username.rand());
    $redis->set("auth:".$auth, $userId);
    setcookie("auth",$auth,time()+86400);
    header("location:list.php");