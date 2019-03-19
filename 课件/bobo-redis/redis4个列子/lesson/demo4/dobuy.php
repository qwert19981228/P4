<?php 
	
	//根据order_id查询redis
	$redis = new Redis();
	$redis->connect('127.0.0.1', 6379);
	$redis->auth('123456');
	//获取
	$data = $redis->hget('buying:'.$_POST['r_id'],'order_id:'.$_POST['order_id']);
	$res = json_decode($data,true);
	$res[':static'] = 1;
	//支付时间
	$res[':buy_time'] = time();

	$pdo = new PDO('mysql:host=localhost;dbname=dy;charset=utf8;port=3306','root','123456');
	$sql = 'update morder set static = 0,buy_time='.$res[':buy_time'].' where id = '.$_POST['order_id'];
	$num = $pdo->exec($sql);
	if($num){
		redisset($redis,$pdo);
		//查询当前影片所有已售座位
		echo '付款成功,请到影厅后,根据手机订单号取票后观影';
	}else{
		echo '付款失败';
	}

	function redisset($redis,$pdo)
	{
		//删除购买状态 buying:id
		$redis->hdel('buying:'.$_POST['r_id'],'order_id:'.$_POST['order_id']); //true or false
		
		//完成后 查询所有已售座位 重新写入redis 以便在选座页显示售卖情况
		$sql = 'select s_code from morder where r_id = '.$_POST['r_id'];
		$stmt = $pdo->query($sql);
		$res = $stmt->fetchAll(PDO::FETCH_ASSOC);
		$a = '';
		foreach ($res as $k => $v) {
			$a .= $v['s_code'].',';
		}
		$arr = explode(',',trim($a,','));
		foreach ($arr as $k => $v) {
			$res = $redis->sadd('omap:'.$_POST['r_id'],$v);	//成功返回1，失败(重复)返回0
		}
	}
	

	



 ?>