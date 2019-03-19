<?php 


	$redis = new Redis;
	$redis->connect('localhost', 6379);
	$redis->select(2);

	$key = 'list-gongdan';

	//将数据压入到链表中
	$res = $redis->lpush($key, serialize($_POST));

	if($res) {
		echo '问题提交成功';
	}else{
		echo '提交失败!!!';
	}




 ?>