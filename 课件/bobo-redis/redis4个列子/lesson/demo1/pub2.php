<?php

	require './redis.php';

	$redis->publish('tv2_1', $_POST['content']);

	