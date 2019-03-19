<?php
	include './redis.php';

	$redis -> publish('tv2',$_POST['content']);
