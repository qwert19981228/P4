<?php
	include './redis.php';

	$redis -> subscribe(array('tv1','tv2'),'callback');
	
	function callback($redis,$channel,$contect){
		/*echo "<pre>";
		var_dump(func_get_args());
		echo "</pre>";*/

		echo $channel;
		echo ":";
		echo $contect;
		echo "<br/>";
		exit();
	}