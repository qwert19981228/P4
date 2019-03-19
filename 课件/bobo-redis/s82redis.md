# redis是什么

3个名字


# redis 特点

安全  持久  花样多



1. 基于内存的数据库
2. 数据存放在内存,但是可以 持久化操作把数据写入磁盘
3. 数据结构类型多
4. 支持安全备份

# redis场景

秒杀    ==== 高并发
定时器     ===== 过期时间的key
排行榜    ======  zset  /  list
计数器   ======= incr  /  decr

好友粉丝 关注   =====   集合的操作



# 在php中如何使用

安装 phpredis 扩展

直接new 一个 redis 即可   使用 new之后的对象 下的属性   就是 你的命令

例子:
<code>
	

	$redis = new redis();  
	$result = $redis->connect('127.0.0.1', 6379);  
	var_dump($result); //结果：bool(true)  

</code>








# 如何CURD

1. str

set name chunchun

setnx

get name

del





2. hash

hset

hget

hdel




3. list

lpush

lrem

lrange




4. set

sadd
spop
smembers

5. zset

zadd

zrem

zrank   byscore



6. 集合操作

set

sinter  sunion  sdiff

记得操作加store



zset

带个帽子就好了


# php-redis  实例


##1. redis 用户管理

user   CURD  登陆  注册

0. 用户表的设计
mysql
id  name  pwd  


redis   注意 用户名唯一. 因为这是作为key存储

存储用户信息: hash:   hmset user1  id  1  name chunchun  pwd 123456

还需要用户列表清单:
zset   zadd userlist user1 100
list   lpush userlist user1
set	  sadd userlsit user1 

第二次进来,你怎么知道人家是第几个?
1. 可以查询 list  set  zset 长度有多少个
2. 计数器   incr decr         set userlength 0    当你注册 incr userlength  删除  desc userlength


三要素: 用户信息存储  用户列表清单  用户id计数














1. 注册  以 list 为例子

public function register()
{
	$_POST()
	正则数据验证后 
	得到data
	// mysql 的话 insert
	
	// redis  存入redis
	
	// 存储用户信息  hash
	判断 是否是第一次
	$ul = $redis->get(userlegth) 
	if(empty($ul)){
		// 设置用户长度  没有user的时候  长度设置为1
		$redis->setnx(userlength,1) 
		

	}else{
		$redis->incr(userlength)
		
	}

	$id = $redis->get(userlength)  // 得到加1 之后id
	$redis->hmset('user'.$data['name'],$data);// user拼接 是为了生成hash的key  拼接name 是为了方便登陆的 查询  key支持查询 支持通配符

	// 存储用户list  值存入的是hash的key
	lpush('user'.$id)


}


2. 登陆
public function login()
{
	$_POST

	数据验证


	$name
	$pwd

	// 第一步: 查询key  
	hmget(user.$name)


	pwd匹配成功则: 登陆成功

	否则 提醒相关错误信息  比如: 密码错误



	






}






##2. 微博




