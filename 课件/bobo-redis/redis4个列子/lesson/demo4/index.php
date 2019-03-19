<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>电影列表</title>
	<style type="text/css">
		.moves img{width: 200px;}
		.moves th{width: 150px;}
	</style>
</head>
<body>
	<center>
		<h3><a href="">今日放映</a></h3>
		<hr>
		<br>
		<table border="1" width="">
			<tr>
				<th>影片</th>
				<th>影片名称</th>
				<th>导演</th>
				<th>主演</th>
				<th>放映信息</th>
				<th>时长</th>
				<th>票价</th>
				<th>操作</th>
			</tr>
		<?php
			//显示当前排片的电影信息
			$sql = 'select m.m_name,m.m_price,m.actor,m.m_director,m.m_time,m.content,m.picurl,r.m_id from relss as r left join movie as m on m.id = r.m_id group by r.m_id';
			require './class/Model.class.php';
			$obj = new Model();
			$data = $obj->get($sql);

			foreach ($data as $k => $v) {
		 ?>
			<tr class="moves">
				<th><img src="<?php echo './public'.$v['picurl']; ?>" alt=""></th>
				<th><?php echo $v['m_name']; ?></th>
				<th><?php echo $v['m_director']; ?></th>
				<th><?php echo $v['actor']; ?></th>
				<th style="width:250px"><?php echo mb_substr($v['content'],0,30).'...'; ?></th>
				<th style="width:100px"><?php echo $v['m_time']; ?>分钟</th>
				<th style="width:100px"><?php echo $v['m_price']; ?></th>
				<th style="width:100px"><a href="./mvinfo.php?mid=<?php echo $v['m_id']; ?>">查看详情</a></th>
			</tr>
		<?php 

			}
		 ?>
			
		</table>
	</center>
</body>
</html>