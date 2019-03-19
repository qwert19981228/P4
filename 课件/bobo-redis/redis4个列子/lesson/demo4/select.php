<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>选择座位</title>
	<style type="text/css">

		#movie{width: 800px;margin: 0 auto;}
		#m_info{width: 349px;float: left;border-right:1px solid #333;}
		#m_order{width: 400px;height: 200px;float: left;margin-left: 50px;}
		p{text-align:left;color: #777;}
		p span{font-size:18px;color:#333;}
		#code{width: 900px;margin: 0 auto;overflow-x: scroll;}
		 .seatCharts{width:35px;height: 35px;border-radius:5px;margin: 2px;float: left;}
		 .available{background-color: #b9dea0;}
		 .selected{background-color: #e6cac4;}
		 .available:hover{background-color: #76b474;}
		 .clear{clear:both;}
		#seat-map{ border-right: 1px dotted #adadad;
				    list-style: outside none none;
				  /*  max-height: 1000px;*/
				    overflow-x: auto;
				    padding: 20px;
				    width: 1200px;}
	</style>
</head>
<body>
	<?php 
		//查询当前场次信息
		$sql = 'select m_price,m_name,m_time,h_name,time,start_time,end_time,seating,id,h_id from relss where id = '.$_GET['rid'];
		require './class/Model.class.php';
		$obj = new Model();
		$res = $obj->get($sql)[0];

		//查询放映厅座位
		$sql = 'select HallLayout from hall where id = '.$_GET['hid'];
		$data = $obj->get($sql)[0];

		//查看当前场次已售座位
		$redis = new Redis();
		$redis->connect('127.0.0.1', 6379);
		$redis->auth('123456');
		// smembers myset 
		$omap = $redis->smembers('omap:'.$_GET['rid']);		
	 ?>
	
	<form action="./order.php" method="post">
	<div id="movie">
		<div id="m_info">
			<p>影片名称:&nbsp;&nbsp;&nbsp;<span ><?php echo $res['m_name']; ?></span></p>
			<p>放映厅:&nbsp;&nbsp;&nbsp;<span ><?php echo $res['h_name']; ?></span></p>
			<p>影片时长:&nbsp;&nbsp;&nbsp;<span ><?php echo $res['m_time']; ?>分钟</span></p>
			<p>时间:&nbsp;&nbsp;&nbsp;<span ><?php echo $res['time'].$res['start_time'].'-----'.$res['end_time']; ?></span></p>
		</div>
		<div id="m_order">
			<br>
			<br>
			<br>
			<p>手机号:&nbsp;&nbsp;&nbsp;<span ><input type="text" name="phone"></span></p>
			<input type="hidden" name="r_id" value="<?php echo $_GET['rid']; ?>">
			<p><span ><input type="submit" value="购买"></span></p>
			<div class="available" style="width: 70px;height: 30px;border-radius:5px;text-align:center;line-height:30px;float:left">可选</div>
			<div class="selected" style="width: 70px;height: 30px;border-radius:5px;text-align:center;line-height:30px;float:left">已售</div>
		</div>
		<div style="clear:both"></div>
		<hr>
	</div>
	<center>
		<div id="code">
			<div id="seat-map">
				<div class="clear seatCharts">1</div>
				<?php 
				for ($i=0,$j=0,$k=1; $i < strlen($data['HallLayout']); $i++) {
					//此处没座
					if($data['HallLayout'][$i] == '_'){
						echo '<div class="seatCharts"></div>';
					//此处有座，座位数累计
					}else if($data['HallLayout'][$i] == 'e'){
						$j++;
						//拼接座位号 排_号
						$s = $k.'_'.$j;
						if(in_array($s,$omap)){
							echo '<div class="selected seatCharts">'.$j.'</div>';
						}else{
							echo '<div class="available seatCharts"><input type="checkbox" name="s_code[]" value="'.$k.'_'.$j.'">'.$j.'</div>';
						}
					}else if($data['HallLayout'][$i] == ','){
						$j = 0;
						$k++;
						echo '<div class="clear seatCharts">'.$k.'</div>';
					}
				}

		 		?>
			</div>
			
		</div>
	</center>
	</form>
	<div style="width: 100%;height: 100px;clear:both"></div>
</body>
</html>