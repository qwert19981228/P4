<?php
	require("redis.php");
	$redis -> del('auth:'.$_COOKIE['auth']);
    setcookie("auth","",time()-1);
    header("location:list.php");