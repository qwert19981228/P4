<?php
	//被关注ID
    $id = $_GET['id'];
    //自己的ID
    $uid = $_GET['uid'];

    require("redis.php");

    $redis = redisLink();
    //我关注的
    $redis->sadd("user:".$uid.":following",$id);
    //被关注者的粉丝
    $redis->sadd("user:".$id.":follower",$uid);

    header("location:list.php");