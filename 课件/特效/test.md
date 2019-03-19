1.自定义一个求和函数 (使用JS实现)

```
    function sum(){
        var sum = 0;//从0开始
        //遍历 相加
        for(var i=0; i<arguments.length; i++){
            sum += arguments[i];
        }
        return sum;//返回结果
    }
    console.log(sum(1,2,3));
```

2.自定义函数求数组 [-1,-2,1,10,4,5,8] 中的最大值？

```
 	var arr = [-1, -2, 1, 10, 4, 5, 8];
    function myarr(arr){
        var max = -Infinity;
    　　for (var i = 0; i < arr.length; i++) {
        　　if (max < arr[i]) {
        　　  max = arr[i];
        　　}
    　　}
    　　return max;
    }
    console.log(myarr(arr));
```

3.在JavaScript中，关于document对象的方法下列就法正确的是（ ）。

```
A. getElementById()是通过元素Id获取元素对象的方法，其返回值为单个对象  
B. getElementByNames()是通过元素name获取元素对象的方法，其返回值为单个对象 
C. getElementbyId()是通过元素Id获取元素对象的方法，其返回值为单个对象  
D. getElementbyNames()是通过元素name获取元素对象的方法，其返回值为对象组

答案：A
```

4.下面的代码会在 console 输出什么？

```
(function(){
 var a = b = 3;
})();

console.log("a defined? " + (typeof a !== 'undefined')); 
console.log("b defined? " + (typeof b !== 'undefined'));

答案：a defined? false
     b defined? true
```

5.下面的代码会输出 ( b )

```
    var  s="abcdefg";
    alert(s.substring(1,2));
```

6.请提取下面页面里所有 a 标签的 href 里的连接地址

```
<html>
        <head>
        </head>
        <body>
            <div id="box">
                <a href="www.itxdl.cn">兄弟连</a>
                <a href="www.qq.com">腾讯</a>
                <a href="www.163.com">网易</a>
                <a href="www.1688.com">阿里</a>
                <a href="www.jd.com">京东</a>
                
            </div>
        </body>
        <script src="./JQ03/jquery-1.8.3.min.js" charset="utf-8"></script>
        <script>
            $('a').each(function(){
               console.log($(this).attr('href'));
            });
            //或者
            var list = document.getElementsByTagName('a');
            for (var i = 0; i < list.length; i++) {
                  console.log(list[i].href);
            }
        </script>
    </html>
```

7.在下面的HTML文档中，编写函数test() ,实现如下功能： 
（1）当多行文本框中的字符数超过20个，截取至20个  
（2）在id为number的td中（第一行第二列）显示文本框的字符个数

![1](./1.png)

```
<table> 
	<tr> 
	<td> 留言 </td> 
	<td id="number"> 0 </td> 
	</tr> 
	<tr> 
	<td colspan=2><textarea rows=6 id="area"></textarea></td> 
	</tr> 
</table> 
	
<script> 
	var area = document.getElementById('area'); 
	var number = document.getElementById('number'); 
	area.oninput = function(){ 
	var num = this.value.length; 
	if(num>20){ 
	this.value = this.value.substr(0,20); 
	} 
	number.innerHTML = this.value.length; 
	} 
</script> 

```

