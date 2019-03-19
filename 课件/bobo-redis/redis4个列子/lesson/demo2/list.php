<?php
    require("redis.php");  
    $redis = redisLink();
?>
<!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- 上述3个meta标签*必须*放在最前面，任何其他内容都*必须*跟随其后！ -->
    <title>登陆页</title>
    <!-- Bootstrap -->
    <link href="./dist/css/bootstrap.min.css" rel="stylesheet">
  </head>
  <body>
    <h1>用户列表</h1>
    <a class="btn btn-primary" href="reg.php">注册</a>
<?php 
     if(!empty($_COOKIE['auth'])){ 
        $id = $redis->get("auth:".$_COOKIE['auth']);
        $username = $redis->hget("user:".$id,"username");
        echo "欢迎您,".$username."  <a class='btn btn-danger' href='logout.php'>退出</a>";
    } else {
        echo '<a class="btn btn-info" href="login.php">登陆</a>';
    }

    $redis = redisLink();

    //用户总数
    $count = $redis->lsize("userIdList");
    
    //页大小
    $ps = 3;
    
    //当前页码
    $pn = (!empty($_GET['p']))?$_GET['p']:1;
    
    //页总数
    $pc = ceil($count/$ps);
    
    $ids = $redis->lrange("userIdList",($pn-1)*$ps,(($pn-1)*$ps+$ps-1));
    
    foreach($ids as $v){
        $data[] = $redis->hmget("user:".$v,array('id', 'username', 'age'));
    }

    if(empty($data)){
        die('暂无好友！');
    }

?>
    <hr>
    <div class="container">
        <div class="row">
            <div class="col-md-6">
                <table class="table table-striped">
                    <tr>
                        <th>ID</th>
                        <th>姓名</th>
                        <th>年龄</th>
                        <th>操作</th>
                    <tr>
            <?php 
                foreach($data as $v) {
                    echo "<tr>";
                    echo "<td>{$v['id']}</td>";
                    echo "<td>{$v['username']}</td>";
                    echo "<td>{$v['age']}</td>";
                    echo "<td><a class='btn btn-danger' href='del.php?id={$v['id']}'>删除</a> <a class='btn btn-warning' href='mod.php?id={$v['id']}'>编辑</a>  ";
                    
                    if(!empty($_COOKIE['auth']) && $id!=$v['id']) {
                        if(!$redis->sismember('user:'.$id.':following',$v['id'])) {
                            echo "<a class='btn btn-primary' href='addFans.php?id={$v['id']}&uid={$id}'>加关注</a></td>"; 
                        } else {
                            echo "<a class='btn btn-info' href='delFans.php?id={$v['id']}&uid={$id}'>取消关注</a></td>"; 
                        }   
                    }
                    echo "</tr>";
                    //显示分页 
                }?>
                    <tr>
                        <td colspan="4">
                            <?=(showPages($pn,$ps,$pc))?>
                        </td>
                    </tr>
                </table>
            </div>
            <?php
                
                if(!isset($id)){
                    exit;
                }

                $followingNums = $redis->scard("user:".$id.":following");
                $followerNums = $redis->scard("user:".$id.":follower");
            ?>
            <div class="col-md-3">
                <h3>关注：<?=($followingNums)?></h3>
                <ul>
                <?php

                    $data = $redis->smembers("user:".$id.":following");
                    foreach($data as $v){
                        $row = $redis->hgetall("user:".$v);
                        echo "<li>".$row['username']."</li>";
                    }
                ?>
                </ul>
            </div>
            <div class="col-md-3">
                <h3>粉丝：<?=($followerNums)?></h3>
                <ul>
                    <?php

                        $data = $redis->smembers("user:".$id.":follower");
                        foreach($data as $v){
                            $row = $redis->hgetall("user:".$v);
                            echo "<li>".$row['username']."</li>";
                        }
                    ?>
                </ul>                
            </div>
        </div>
    </div>
   <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="./dist/js/jquery.js"></script>
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <script src="./dist/js/bootstrap.min.js"></script>
</body>
</html>