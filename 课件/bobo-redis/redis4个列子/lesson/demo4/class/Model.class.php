<?php
	class Model
	{
		public $pdo;		//PDO对象
		public $redis;		//Redis对象
		public $sql;		//SQL语句
		public $key;		//SQL生成的KEY

		public function __construct()
		{
			$this->redis = new Redis();
			$this->redis->connect('127.0.0.1', 6379);
			$this->redis->auth('123456');
		}

		public function get($sql)
		{
			//根据SQL生成KEY
			$this->sql = $sql;
			$this->key = md5($sql);
			//尝试获取KEY
			$data = json_decode($this->redis->get($this->key),true);
			if(!$data){
				//不存在则执行sql查询
				$this->pdo = new PDO('mysql:host=127.0.0.1;dbname=dy;charset=utf8;port=3306','root','123456');
				$stmt = $this->pdo->query($this->sql);
				$data = $stmt->fetchAll(PDO::FETCH_ASSOC);
				//写入
				$this->redis->set($this->key,json_encode($data));
			}
			return $data;
		}

	}
