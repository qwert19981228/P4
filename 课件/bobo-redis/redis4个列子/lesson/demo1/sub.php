<?php

	require './redis.php';

	$redis->subscribe(array('tv1_2', 'tv2_1'), 'callback');

	function callback($redis, $channel, $content){

		//echo "<pre>";
		//print_r(func_get_args());

		echo "频道名：".$channel."<br>";
		echo "内　容：".$content."<br>";	
		exit;
	}