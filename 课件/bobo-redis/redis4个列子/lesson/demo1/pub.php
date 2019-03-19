<?php

	require './redis.php';

	$redis->publish('tv1_2', $_POST['content']);
	//$redis->publish('tv1_2', 'testname');

	