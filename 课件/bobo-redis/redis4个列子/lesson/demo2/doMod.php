<?php
    require("redis.php");

    $redis = redisLink();

    $id = $_POST['id'];
    $username = $_POST['username'];
    $age = $_POST['age'];
    $a = $redis->hmset("user:".$id,array("username"=>$username,"age"=>$age));
    if($a){
        header("location:list.php");
    }else{
        header("location:mod.php?id=".$id);
    }