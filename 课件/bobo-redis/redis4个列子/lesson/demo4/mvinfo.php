<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>选择场次</title>
	<style type="text/css">
		.moves img{width: 200px;}
		.moves th{width: 150px;}
		#movie{margin: 0 auto;}
		#m_pic{width: 1000px;}
		#m_info{width: 1000px;text-align:left;color: #777;}
		#m_info p span{font-size:18px;color:#333;}
	</style>
</head>
 <body>
 	<center>
	
		<?php
			//获取某一个电影的详情
			$sql = 'select m_name,m_type,m_time,actor,m_director,content,picurl,country_area from movie where id = '.$_GET['mid'];
			require './class/Model.class.php';
			$obj = new Model();
			$data = $obj->get($sql);
			$res = $data[0];
		 ?>
		<div id="movie">
			<div id="m_pic"><img width="100%" src="./public<?php echo $res['picurl']?>" alt=""></div>
			<div id="m_info">
				<p>影片名称:&nbsp;&nbsp;&nbsp;<span ><?php echo $res['m_name']; ?></span></p>
				<p>影片类型:&nbsp;&nbsp;&nbsp;<span ><?php echo $res['m_type']; ?></span></p>
				<p>影片地区:&nbsp;&nbsp;&nbsp;<span ><?php echo $res['country_area']; ?></span></p>
				<p>影片时长:&nbsp;&nbsp;&nbsp;<span ><?php echo $res['m_time']; ?></span></p>
				<p>影片导演:&nbsp;&nbsp;&nbsp;<span ><?php echo $res['m_director']; ?></span></p>
				<p>影片主演:&nbsp;&nbsp;&nbsp;<span ><?php echo $res['actor']; ?></span></p>
				<p>影片剧情:&nbsp;&nbsp;&nbsp;<span ><?php echo $res['content']; ?></span></p>
			</div>
			<h3><a href="">场次列表</a></h3>
			<hr>
			<br>
			<table border="1" width="">
				<tr>
				
					<th>放映厅</th>
					<th>开场时间</th>
					<th>结束时间</th>
					<th>票价</th>
					<th>座位数</th>
					<th>已售</th>
					<th>操作</th>
				</tr>
			<?php
				//获取某一个电影的排片情况
				$sql = 'select r.id,r.m_price,r.h_name,r.start_time,r.end_time,r.seating,r.h_id,o.num from relss r LEFT JOIN morder o on o.r_id = r.id where r.m_id = '.$_GET['mid'];
				$data = $obj->get($sql);

				$redis = new Redis();
				$redis->connect('127.0.0.1', 6379);	

				foreach ($data as $k => $v) {
					$num = count($redis->smembers('omap:'.$v['id']));	
			 ?>
				<tr class="moves">
					<th><?php echo $v['h_name']; ?></th>
					<th><?php echo $v['start_time']; ?></th>
					<th><?php echo $v['end_time']; ?></th>
					<th><?php echo $v['m_price']; ?></th>
					<th><?php echo $v['seating']; ?></th>
					<th><?php echo $num; ?></th>
					<th style="width:100px"><a href="./select.php?rid=<?php echo $v['id']; ?>&hid=<?php echo $v['h_id']; ?>">去选座</a></th>
				</tr>
			<?php 

				}
			 ?>
				
			</table>
		</div>
	</center>
	<div style="width: 100%;height: 100px;"></div>
 </body>
 </html>