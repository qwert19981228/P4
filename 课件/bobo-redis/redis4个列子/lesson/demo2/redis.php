<?php
	header("content-type:text/html;charset=utf-8");

	function redisLink() {
	    $redis = new Redis();
	    //连接服务器
	    $redis->connect("127.0.0.1");
	    //授权
		$redis->auth("123456");
		return $redis;
	}


	function showPages($pn,$ps,$pc) {
		$prePage = (($pn - 1) <= 1) ?1:($pn - 1);
		$nextPage = (($pn+1)>=$pc)?$pc:($pn+1);

		$pages = '<nav aria-label="Page navigation">
		  <ul class="pagination">
		    <li>
		      <a href="?p='.$prePage.'" aria-label="Previous">
		        <span aria-hidden="true">&laquo;</span>
		      </a>
		    </li>';

		for($i = 1; $i<=$pc; $i++) {
			$pages .='<li><a href="?p='.$i.'">'.$i.'</a></li>';
		}

		$pages .= '
			<li>
		      <a href="?p='.$nextPage.'" aria-label="Next">
		        <span aria-hidden="true">&raquo;</span>
		      </a>
		    </li>
		  </ul>
		</nav>';

		return $pages;
	}

