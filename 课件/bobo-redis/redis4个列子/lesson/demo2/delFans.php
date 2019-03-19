<?php
    require("redis.php");
	//被取消关注ID
    $id = $_GET['id'];
    //自己的ID
    $uid = $_GET['uid'];

    $redis = redisLink();
    //我关注的
    $redis->srem("user:".$uid.":following",$id);
    //被关注者的粉丝
    $redis->srem("user:".$id.":follower",$uid);
    header("location:list.php");