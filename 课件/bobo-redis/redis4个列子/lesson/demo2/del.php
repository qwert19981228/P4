<?php
	require("redis.php");
	$redis = redisLink();

	$uid = $_GET['id'];
	//快速获取ID的key
	$username = $redis->hget('user:'.$uid,'username');
	$redis->del('username:'.$username.':id');
	//删除hash
	$redis->del("user:".$uid);
	//删除分页链
	$redis->lrem("userIdList",$uid);

	//删除关注关系
	$redis->del('user:'.$uid.':following');
	$redis->del('user:'.$uid.':follower');

	$ids =  $redis->lrange("userIdList", 0, -1);

    foreach($ids as $v){
        $redis->srem("user:".$v.":following", $uid);
        $redis->srem("user:".$v.":follower", $uid);
    }

	header("location:list.php");