<?php 
	//判断数据是否完整
	if(empty($_POST['phone']) || empty($_POST['s_code'])){
		// header('location:'.$_SERVER['HTTP_REFERER']);
		$str = '<script type="text/javascript">
			alert("请填写您的手机号,并选中您所要购买的座位");
			location.href="'.$_SERVER['HTTP_REFERER'].'";
		</script>';
		echo $str;die;
	}
	
	//拼接订单morder数据  :开头是为了符合PDO预处理数据格式
	$data[':order_code'] = uniqid();//订单id
	$data[':r_id'] = $_POST['r_id'];//对应场次
	$data[':m_id'] = $_POST['r_id'];//对应电影
	$data[':num'] = count($_POST['s_code']);//数量
	$data[':s_code'] = implode(',',$_POST['s_code']);//座位号
	$data[':phone'] = $_POST['phone'];//手机号
	$data[':static'] = 1;//状态,0已支付,1未支付,2取消
	$data[':order_time'] = time();//下单时间

	$redis = new Redis();
	$redis->connect('127.0.0.1', 6379);
	$redis->auth('123456');

	//锁定座位
	//单独将当前场地的座位存储  $_POST['s_code']
	foreach ($_POST['s_code'] as $k => $v) {
		$arr[] = $v;
		$res = $redis->sadd('omap:'.$data[':r_id'],$v);	//成功返回1，失败(重复)返回0
		//如果订单中已存在该座位调用delmap函数
		if(!$res){
			delmap($redis,$arr);
			break;
		}
	}

	function delmap($redis,$arr)
	{
		echo '<script type="text/javascript">
			alert("您所选中的座位,已经被锁定,请更换");
			location.href="'.$_SERVER['HTTP_REFERER'].'";
		</script>';
		die;
	}

	$pdo = new PDO('mysql:host=127.0.0.1;dbname=dy;charset=utf8;port=3306','root','123456');
	$sql = 'insert into morder(order_code,r_id,m_id,num,s_code,phone,static,order_time) values(:order_code,:r_id,:m_id,:num,:s_code,:phone,:static,:order_time)';
	$stmt = $pdo->prepare($sql);
	//执行
	$stmt->execute($data);
	//受影响行数
	$num = $stmt->rowCount();

	if($num){
		//最后插入id
		$id = $pdo->lastInsertId();
		//添加交易记录
		$redis->hset('buying:'.$data[':r_id'],'order_id:'.$id,json_encode($data));
		// 跳转页面
		header('location:./buy.php?order_id='.$id);
	}else{
		die('下单失败');
	}
