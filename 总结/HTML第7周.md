### 伪类选择器

​	s1 和 s2 代表基础选择器

#### 	s1:hover{. . .}

​		当鼠标悬停在s1上时,触发CSS

​			使用技巧:

​				s1:hover    s2{. . .}

​				s1:hover > s2{. . .}

​				s1:hover + s2{. . .}

​				s1:hover ~ s2{. . .}

#### 	s1:focus{. . .}

​		当s1获取到光标时,触发CSS

#### 	按照顺序查找标签

##### 		s1:first-child{. . .}

​			匹配s1父级里面的第一个元素s1

​				详细分析:

​					第一步:先找到s1的父级

​					第二步:找到父级里面的第一个儿子元素

​					第三步:第一个儿子元素,是不是s1

#### 	按照标签查询顺序

##### 		s1:first-of-type{. . .}

​			匹配s1父级里面所有s1中的第一个

​				详细分析:

​					第一步:先找到s1的父级

​					第二步:找到父级里面的所有s1

​					第三步:找到s1中的第一个

#### 	其他

##### 		s1:last-child{. . .}

​			匹配s1父级里面的最后一个元素s1

##### 		s1:last-of-type{. . .}

​			匹配s1父级里面所有s1中的最后一个

##### 		s1:nth-child(N){. . .}

​			匹配s1父级里面的第N个元素s1

##### 		s1:nth-of-type(N){. . .}

​			匹配s1父级里面所有s1中的第N个

​				N的写法:

​					数字

​					单词 odd奇数  even偶数

​					一元一次方程



### 伪对象选择器

#### 	s1: : before{. . .}

​		匹配s1里面的最前面

#### 	s1: : after{. . .}

​		匹配s1里面的最后面					

#### 	作用

​		应用于浮动技术上

#### 	注意

​		before 和 after 常用属性content

​		before 和 after 是用两个冒号



## 字体

### font-size

​	字体大小

### font-family

​	 字体家族	

### font-weight

​	 字体加粗        bold    normal

### font-style

​	字体风格         italic   normal

### line-height

​	行高

**简写**:

​	font:  weight  style  size/line-height family

**注意:**

​	各大浏览器因兼容性不同,所支持最小字体大小也不一样

​	建议尽量不要写 比最小字体还小的size

​	line-height 经常被用于做垂直居中,仅限于一行

​	weight 和 style 可以省略且顺序可颠倒

​	line-height 可以省略,只能写在size的后面,必须用/隔开

​	size必须在family的前面,且两个都不能少	



## 背景

### background-image

​	背景图片(url 图片地址)

### background-color

​	背景颜色

### background-repeat	

​	背景重复 (no-repeat)

### background-position

- 正数: 向右  向下
- 负数: 向左  向上

### background-size

​	背景大小,设定背景宽

### background-attachment

​	背景固定(fixed)

**简写:**

​	background: image color position/size repeat attachment

**注意:**

​	以上顺序随便颠倒

​	只有size是必须写在position的后面



## 边框

### 基本属性

​	color   width   style

### 基本方向

​	left    right   top   bottom

### 单边

​	boeder-方向-属性

### 单边简写

​	border-方向：color  width  style

### 四边

​	border-属性

### 四边简写

​	border： color  width  style

**注意：**

​	color  和   width  都有默认值，所以可省略

​	style 不能省略

​		style常用值:

​			solid  实线

​			none 取消边框

​			double  双线

​			dotted  点线

​			dashed  虚线

### 圆角

​	border-上下-左右-radius: %或px

### 圆角简写

​	border-radius:%或px

​	注意:如果需要最圆,建议用100%

### 合并边框	

​	border-collapse: collapse

### 轮廓

​	outline

​		常用none

​		常用于表单



## 文本

### text-align

​	水平对齐方式    left  center  right

### vertical-align

​	垂直对齐方式   top   middle  bottom

### text-indent

​	首行缩进

### text-decoration

​	划线

​	 	underline 	下划线

​		overline		上划线

​		line-through	删除线

​		none		不要线

### text-shadow

​	文字阴影

### text-overflow

​	文字溢出

​		ellipsis	将溢出的隐藏内容用. . .代替

​				仅限于一行

​				需要配合white-space和overflow

**注意:**

​	vertical-align默认对外对齐

​	如果需要对内对齐,配合display



## 盒子阴影

### box-shadow

​	box-shadow: 10px 20px 30px 40px #ccc inset;

​	10px: 水平对齐

​	20px: 垂直对齐

​	30px: 模糊度,不能为负数

​	40px: 阴影面积 默认为当前大小,可省略

​	#ccc: 阴影颜色

​	inset: 内阴影



## 溢出

### overflow

​	hidden		隐藏溢出的内容

​	visible		显示溢出的内容	默认值

​	auto		通过滚动条显示溢出的内容

​	overflow-x	hidden	|	visible	|	auto

​	overflow-y	hidden	|	visible	|	auto



## 平滑过渡

### transition

​	transition： 属性	过渡时间   过渡速率   延迟时间

​	属性：

​		过渡一个属性

​		过渡多个属性，每个属性之间有逗号隔开

​		过渡所有属性，all

​	过渡时间：

​		单位：s/ms

​	过渡速率：

​		linear		匀速

​		ease-in		加速

​		ease-out	减速

​		ease-in-out	先加速再减速

​		自定义速率

​	延迟时间：

​		单位：s/ms

​	注意：

​		过渡具有数值变化的属性，例如 width，height，color等

​		相反案例：text-align，border-style等



## 变形

### transform

​	none		不变形

​	rotate		旋转

​				单位：deg	角度

​	skew		扭曲

​				单位：deg	角度

​				注意：90 * 奇数倍   扭没了

​	scale		中心缩放

​				单位：倍数

​				基本倍数：1	代表本身

​				>1放大

​				<1缩小

​	translate	位移

​				单位：px



## 定位

### position

​	absolut	绝对定位

​	relative	相对定位

​	fixed	固定定位

1. 绝对定位

   位置：不保留原来的位置

   原点：基于第一页的四个角落

2. 相对定位

   位置：保留原来的位置

   原点：基于原来的位置

3. 固定定位

   位置：不保留原来的位置

   原点:   屏幕的四个原点

注意：任意定位都会脱离文档流，进入定位流



### 定位场景

​	当元素 发生重叠时，可以使用定位

问题：如何让后辈以祖辈的四个角落作为原点？？？

解决：

​	祖辈：相对定位

​	后辈：绝对定位



## 列表属性

### list-style

​	none	取消项目符号



## 鼠标样式

### cusor

​	pointer		手掌	频率使用较高

​	none		隐藏鼠标

​	text			文本

​	default		默认箭头

​	wait			等待

​	move		坐标移动



## 字体图标

长得像图片，但是用的是字体样式

所有的字体图片，都是矢量图

使用阿里巴巴的字体图片

1. 访问  https://www.iconfont.cn/
2. 搜罗 你需要的字体图标
3. 添加到项目再下载
4. 引入 iconfont.css
5. 打开demo_unicode.html
6. 查找你正要的字体图片，复制 &.....;
7. 粘贴到需要用的标签处
8. 给该标签赋予class名     iconfont



## 定位优先级

#### z-index

​	z-index:num数字

​		num数字越大,定位优先级越高

​	注意:

​		必须要配合position使用



## 盒子模型

盒子在不同的浏览器中,组成部分也不一样

IE浏览器:	内容(涵盖了内边距和边框)	(外边距)

非IE浏览器:	内容+内边距+边框			(外边距)



## 行块级元素

在html里面,所有标签都划分成两种类型:

​	块级元素:	block

​		div,p,h1~h6,ul,. . .

​		独占一行

​		宽度 默认与浏览器一致

​		高度 默认与内容一致

​		宽度,高度,行高,内外边距都是可以手动控制

​		容纳性:任意元素

​	行级元素:	inline

​		span,a,b,i,del, . . .

​		不会独占一行

​		宽度和高度都与内容一致

​		行高,水平内外边距 可以手动控制

​		容纳性:只能容纳行级元素

​		注意点:

​			多个超链接a标签不要嵌套使用





## 内外边距

### 外边距

​	外边距:标签与标签之间的距离

​	四边:

​		margin:?px                              	        上下左右均为?px

​		margin:?px ??px                         		上下? 左右??

​		margin:?px ??px ???px                   	上? 左右?? 下???

​		margin:?px ??px ???px ????px        	上? 右?? 下??? 左????

​	单边:

​		margin-方向

​	小技巧:

​		在父级元素内,水平居中

​		margin-left: auto

​		margin-right: auto

### 内边距

​	内边距:标签与内容之间的距离

​	四边:

​		padding:?px                              		上下左右均为?px

​		padding:?px ??px                         		上下? 左右??

​		padding:?px ??px ???px                   	上? 左右?? 下???

​		padding:?px ??px ???px ????px        	上? 右?? 下??? 左????

​	单边:

​		padding-方向



## 浮动

float: left | right | none

clear: left | right| both

注意:

​	不保留原来的位置,脱离文档流

​	文字会环绕浮动

​	块级元素会重叠浮动

​	浮动主要是针对块级元素,因为行级元素本身就横排的

​	清除浮动之后,元素将会保留原来的位置

清除浮动原理:

​	后面的兄弟元素 清除前面兄弟元素的浮动

​	清除浮动方法1:

​		利用原理,在浮动元素的最后面,加一个空标签,并赋予clear

​	清除浮动方法2:

​		在浮动元素的父级,添加overflow:hidden,形成BFC区域

​		BFC区域:暂时理解不会影响外界的区域

​	清除浮动方法3:

``` css
父级::after{
    content:'';
    display:block;
    clear:both;
}
```

 

## 元素显示

### display

​	block		转为块级元素

​	inline		转为行级元素

​	inline-block	转为内联-块元素

​	none		隐藏元素,不占位隐藏

​	table		转为块级表格

​	table-cell	转为td单元格

​	. . .

### visiblity

​	hidden		占位隐藏

​	visible		显示	



## CSS初始化

### 目的

​	因为各大浏览器的默认值都不一样,初始化为了解决这个问题,统一浏览器标准





## 网页布局

### 布局方法

- Div + CSS布局
- 弹性盒子布局
- 响应式布局



### 布局规则

​	先看行，再看列

​	从上向下依次排列

​	先铺大的，再铺小的



#  JavaScript



## JS简介	

#### JavaScript

​	简称JS

​	由Netscape公司最早推出

​	由于JS符合ECMA特效，因为又称之为ES

#### JS作用

​	JS常用于页面特效，数据验证等

#### JavaScript 和 Java的区别

​	雷峰塔 和 雷锋

#### JS的优点和局限

##### 优点

- JS是在客户端运行的，不会占用服务器资源
- JS支持跨平台
- JS属于OOP开发
- 对页面有很高的操控性

##### 局限

- 因为浏览器的标准不统一，导致JS兼容性有差异
- JS不能操作本地文件

#### JS的组成

- 核心	ECMAScript		JS的语法和基本对象
- 文档对象 DOM
- 浏览器对象 BOM

#### JS手册参考地址

http://www.w3school.com.cn/jsref/index.asp



## JS导入方式

### 常见导入方式

1. 外部导入

   通过 script标签的src属性来导入js文件`<script src="js文件地址"></script>`

2. 内部现写
    通过 script标签里面 直接写js代码
    `<script>js代码</script>`

3. 触发

   后期通过事件来触发js代码


注意事项
      1. 为了页面加载更快, 建议将js导入 和书写放在代码的最后面
      2. 外部导入时, 不能在script标签里面写js代码



## 基本语法

#### ​严格区分大小写

#### 注释

​	// 单行注释

​	/* 多行注释 */

#### 命令结束符

​	分号;    (不要使用 中文版的分号)

​		在js中, 一行只有一条命令, 可以省略分号

​		一行拥有多条命令, 必须以分号隔开

​		推荐, 每条命令都加上分号

​	换行     (只有一条命令时, 可以不加分号)



## 变量

### 变量格式

​	var 变量名        没有初始化, 默认为undefined

​	var 变量名 = 值

​	var 变量名1 = 值1, 变量名2 = 值2,  ...

​	var 变量名1 = 变量名2 = 变量名3 ... = 值

### 变量名规范

​	由数字, 字母, 下划线 和 $符 组成

​	不能以 数字开头

​	严格区分大小写

​	不允许包含空格和其他标点

​	不能使用关键字

### 常见关键字

​	break    case    catch   continue    default

​	delete   do      else    finally     for

​	function if      in      instanceof  new

​	return   switch  this    throw       try

​	typeof   var     void    while        with



## 数据类型

### 基本

​	Boolean, String, Number

### 复合

​	Array, Object

### 特殊

​	Null, undefined, function



## Boolean布尔

### 值的写法

​	true,false

### 严格区分大小写

### 作用

​	主要用于判断 状态, 真假



## String字符串

### 格式

​	单双引号 ''  ""

​	反引号 ``

### 引号区别

##### ​	单双引号

​		不能识别变量

​		解析转义字符

​		支持互插, 不支持自插

​		不能直接输入 回车

##### ​	反引号

​		识别变量

​		可以直接输入 回车

### 字符串操作

​	拼接  +



## Number数值

### 整数

​	范围: -2^53 ~ 2^53

​	超出范围的运算, 都不准确

### 浮点数

​	常规表达方式

​	科学计数法

​	正负无穷

​		Infinity

​		Inifinity

​	有效位数 17位

​	函数 isFinite()

​	方法 变量.toFixed( 位数 )



## Number中的特殊类型

> NaN:  Not a Number  不是一个数

### 作用 

​	用于表示不是一个数字值

### isNaN()

​	判断是否不是 一个数字值

​		true: 不是数字

​		false: 是数字

### 运算

​	NaN与任何数字运算, 结果都是NaN

### 比较

​	NaN与任何数字比较, 都不相等, 包括自己



## Null空

Null代表空

​	常用于清空值或占位 (初始化)

注意​

​	null 是关键字

​	null 不能作为变量名存在



## undefined

**undefined  纯小写**

**以下情况值为 undefined**

- 直接赋值

- 只定义变量, 没赋值

- 不存在的属性

- 未初始化的形参

- 没有返回值的函数 

**null 和 undefined**

​	null 和 undefined 等价的

​	null 是关键字

​	undefined 不是关键字

​	如果需要给变量 赋空值, 建议使用null



## 类型转换

### Bool 转换

​	Boolean( ) 函数

​	以下值 转为bool时为false

​		0 或 0.0

​		-0

​		''  空字符串

​		null

​		undefined

​		NaN



### String( )函数 



### Number( )函数



### parseInt( )

​	强制转为 Numer-int 整数

​		不带数字 直接NaN

​		二进制 -> 直接变0

​		八进制 -> 保留

​		十六进制 -> 解析,转为十进制



### parseFloat( )

​	强制转为Numer-float 浮点数

​		基本同上

​		只有一个小数点有效

​		二进制 和 十六进制  --> 直接变 0

​		八进制 --> 保留数字

​		支持科学计数法