<?php 

	// $res = file_get_contents('http://www.xiaohigh.com/mail/index.php?to=779498590@qq.com&code=987489');
	// file_put_contents("log.php", $res."\r\n");die;

	//从链表的末端获取元素信息, 将信息存入到数据库中
	
	$redis = new Redis;
	$redis->connect('localhost', 6379);
	$redis->select(2);

	$key = 'list-gongdan';

	//弹出一个元素
	

	while(1) {
		$len = $redis->lsize($key);
		//有活的时候
		if($len >= 1) {
			$info = $redis->rpop($key);

			//将字符串转为数组
			$data = unserialize($info);

			//将数据存入到数据库中
			// var_dump($data);
			$pdo = new PDO('mysql:host=localhost;dbname=lamp179;charset=utf8','root','123456');

			$stmt = $pdo -> prepare('insert into gongdans (name,phone,content,addtime) values(?,?,?,?)');

			//绑定
			$arr = [
				$data['name'], 
				$data['phone'],
				$data['content'],
				time()
				];

			$stmt->execute($arr);
			//请求
			// http://www.xiaohigh.com/mail/index.php?to=779498590@qq.com&code=987489
			// http://www.xiaohigh.com/message/index.php?to=18311422275&class=123456&web=lamp117&code=123456

		}else{
			//没活的时候
			sleep(30);
		}
	}

