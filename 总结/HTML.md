[TOC]



# HTML



## 网页基础布局

### HTML5 声明头

​	`!DOCTYPE html`

### 开始结束标记

​	`<html> / </html>`

### 头标签

​	`<head>`设置标题/引入脚本/加载样式表css/提供元信息

### 元信息标签

​	设置网页字符集为utf-8

​	`<meta charset='utf-8'>`

### 网站标题

​	`<title></title>`

### 页面主体

​	`<body></body>`

### 注释

​	HTML注释的内容，注释不能嵌套使用

​	`<!-- -->`



## HTML语法

1. HTML 不区分大小写，**推荐小写**
2. HTML**标签及标签中的内容**组成一个**HTML元素**
3. HTML属性写在标签里面，用来**描述**该**元素的特征或特点**
4. 属性名 = "属性值"，不区分大小写，**建议双引号，且小写**
5. 多个属性之间用空格隔开，多个属性值之间也使用空格隔开
6. 标签之间的多个空格 或 换行，都**会被解析为一个空格**



## 功能标签

### 段落标签

**作用**

​	每个段落标签之间都会有一个空行

**标签名**:**p**



### 换行标签

**作用**

​	就是换行的

**标签名**:**br**



### 水平分割线标签

**标签名:hr**

**标签属性**

- **[size]** 粗细 **单位 px** 像素(pixel)
- **[width]** **宽度 px/%**
- **[align]** **水平位置** left/center/right
- **[color]** 颜色 
  - 英文 blue red green yellow 
  - RGB #000 #fff
  - rgb(255,255,255)



### 居中标签

**作用**

​	居中的

**标签名**:**center**



### 格式化输出标签

**作用**

​	原样输出

**标签名:pre**



### 列表标签

#### 有序列表

**标签名:ol**

**标签属性**

- **[type]** 1 a A i I
- **[start]** 列表起始数字
- **[reversed]** 升序/降序



#### 无序列表

**标签名:ul**

**标签属性**

- **[type]** circle disc square



#### 列表项

**标签名**:**li**

**标签属性**

- **[value]** 值



### 定义列表

#### dl

**作用** 

​	定义列表标签

#### dt

**作用**

​	定义列表标题

#### dd 

**作用**

​	定义列表详情



### 标题标签

**作用**

​	文字大小随数字大小递减，所有标签都有加粗功能

**标签名**:**h1~h6**

​		



### biu标签

- **b**    加粗
- **i**     倾斜
- **u**   下划线  



### 标记标签

- **sup上标**
- **sub下标**



### 字体标签

**作用**

​	定义字体用的

**标签名**:**font**



### 图片标签

**作用**

​	定义图片

**标签名**:**img**

**标签属性**

- **[src]** source 指定图片资源的地址(url)
- **[alt]** 图片加载失败时显示的问题
- **[width]** 宽度
- **[height]** 高度
- **[title]** 鼠标悬停时显示的提示文字



### 超链接

**作用**

​	用于页面之间的跳转

**标签名**:**a**

**标签属性**

- **[href]**	跳转地址，灵魂属性

- **[target]**	以什么窗口进行跳转

  - **_blank**	在新窗口打开链接
  - **_self**	在本窗口打开链接,默认

  - **_top**	在顶级窗口打开链接

  - **name**	在自定义窗口打开连接



1. 不带 **href**  的 a标签

   ```html
   <a>百度一下,你就知道</a>
   ```

2. 带有 空**href** 的 a标签,默认跳转到本页面

   ```html
   <a href="">百度一下,你就知道</a>
   ```

3. 带有  **href** 值的 a标签

   ```html
   <a href="http://www.mi.com">小米官方</a>
   ```

4. 在新窗口打开链接

   ```html
   <a href="http://www.mi.com" target="_blank">小米官方</a>
   ```



## URL地址

> 俗称:网址

```html 
http://www.baidu.com:80/video/python/plane.mp4?name=MH370&num=30#xxoo
```

1. 协议	http
2. 域名	www.baidu.com => IP地址
3. 端口        80             访问的默认端口就是80
4. 目录        video/python
5. 文件名    plane.mp4
6. 参数       name=MH730&num=30
7. 锚点       xxoo

**注意**:

1. 域名的本质就是IP,作用:好记
2. 任何网址 最终都是指向文件名
3. 参数是有特殊需求时才会需要

**锚点的实现**:

- 步骤1:准备锚点,在开始标签中,通过id="锚点名" 的形式来准备
- 步骤2:跳转至锚点,在需要点击的链接中,通过href="url#锚点名" 来跳转



## 实体符号

**实体符号格式**:	&**实体代码**;

- 小于:`&lt;`
- 大于:`&gt;`
- 空格:`&nbsp;`
- 版权:`&copy;`
- 人民币:`&yen;`





## 多媒体之音频

**标签名**:**audio**

**标签属性:**

- **[src]**	   音频来源地址
- **[controls]** 控制器
- **[autoplay]**自动播放
- **[loop]**        循环播放



## 多媒体之视频

**标签名**: **vedio**

**标签属性:**

- **[src]**	   视频来源地址
- **[controls]** 控制器
- **[autoplay]**自动播放
- **[loop]**        循环播放



## 表格

**表格标签**

- table	声明
- caption  表格标题
  - tr	表行
  - th    表头
  - td    普通单元格

**表格属性**

- border           边框
- cellspacing    外边距:单元格与单元格之间的距离
- cellpadding   内边距:单元格与内容之间的距离
- width             宽度
- height            高度
- rowspan        行合并
- colspan          列合并
- align               水平对齐方式  left  center   right
- valign             垂直对齐方式  top   middle  bottom
- bgcolor          背景颜色
- background  背景图片



## 表单

#### form

- 页面中可以有多个表单
- 不能嵌套使用
- 所有的表单内容都出现在该标签内
  - [action]		指定接受数据的脚本文本
  - [method]       规定如何发送表单数据
    - get		默认值,使用URL传参
    - post        使用HTTP  post方式传参(隐蔽传参)



**GET  与   POST的区别**

1. get会把所有数据显示到浏览器地址栏上,post是通过HTTP  post机制,所以不会显示
2. get传送数据量较小,一般不能大于2KB,post传送的数据量较大,理论上不少限制
3. post比get相对安全一些
4. get通常传递不太重要的小量信息

**HTTP请求**

- HTTP协议是无状协议,无状态是指浏览器和Web服务器之间不需要建立持久的连接，这意味着当一个客户端向服务器端发出请求，然后Web服务器返回响应，连接就被关闭了，在服务器端不保留连接的有关信息.

- 建立TCP连接---发送请求命令---浏览器发送请求头信息---服务器应答---服务器发送应答头信息---服务器向浏览器发送数据---服务器关闭TCP连接
- 如何查看HTTP请求
- 浏览器F12---network---重载页面即可查看到请求信息



#### input

> 输入框标签
>
> 用于定义一个输入的区域

- **type**  规定输入域的功能

  - **text**                文本输入框(默认)

  - **password**     密码输入框

    密码输入框中的字符都会被显示为 * 或圆点

  - **radio**             单选按钮

    - **checked**         默认选中的状态,值为**checked**

  - **checkbox**     多选按钮

    - **checked**         默认选中的状态,值为**checked**

  - **file**                  文件上传域

    上传文件必须使用post方式

    file     不能使用value属性

    - **enctype**          规定表单 在发送到服务器之前应该如何对数据进行编码

      application/x-www-form-urlencoded

      multipart/form-data    文件上传专用

  - **hidden**             隐藏域

  - **submit**             提交按钮

  - **reset**                 重置按钮

  - **button**             普通按钮

  - **number**           限定为数值的值

    - **max**                输入范围限定
    - **min**                 输入范围限定

  - **time**                 限制时间

  - **email**               限制邮箱

- **name**   给表单项 设定一个数据标识

  一定要设置,输入框的name值

  只有设置了此值,那么在提交时,数据才能被传递

- **value**    为input元素设定值

  - **text** / **password** / **hidden**

    定义输入框的初始值

  - **radio** / **checkbox**

    定义与输入框相关的值

  - **submit** / **reset** / **button**

    定义按钮的功能文本

- **maxlength**  输入字符的最大长度,单位字符个数
- **minlength**   输入字符的最小长度,单位字符个数
- **size**   宽度,单位字符

- **placeholder**  提供可描述的提示信息(HTML5)

  输入框为空时,才会显示

- **readonly**   只读

  可看到,亦可提交

- **disabled**   禁用此元素

  被禁用的元素,是无法提交到后端的



#### label

​	为**input**元素  定义标注(标记)

​	多用于 **单选** / **多选时**,与**input**组合使用

#### select/

​	下拉框

- **name** 不可缺少

#### option

​	下拉选项

​	需要写在**select**的内部

- **value**  设定初始值
- **selected** 默认选中状态
- **size**  显示下拉个数
- **multiple**  拉下多选

#### textarea

​	多行文本域

- **name** 标识
- **rows** 设置该文本域的行数(宽度)

- **cols**   设置该文本域的列数(高度)

- **placeholder** 提供可描述的提示信息(**HTML5**)
- **maxlength**   输入字符的最大长度,单位:字符个数

#### button

​	普通的按钮

​	需要设定不同的**type**值,来实现不同的功能



## 分帧

> 就是把浏览器 分成多个窗口来显示 不同的网页

#### frameset 

​	框架结构标签

​	该标签不能与body同时出现 

- **[cols]**   按列划分
- **[rows]**   按行划分
  - 像素, % .  *

#### frame

​	框架标签

- **[src] **   加载指定的url的网页
- **[name] ** 窗口的标识
- **[frameborder]**  0/1  是否显示边框
- **[noresize]**   设置无法调整框架大小  ="noresize"
- **[scrolling]**  是否显示滚动条  yes/no/auto	

#### iframe

​	该标签可以与body同时出现

- **[name]**    标识
- **[src]**     加载指定的url的网页
- **[frameborder]**  0/1  是否显示边框
- **[scrolling]**是否显示滚动条  yes/no/auto
- **[width]**   宽度
- **[height]**  高度	



## head内的功能标签

#### title

​	网页标题

#### base

​	基底网址标签

- **[href] **  指定以社么网址去跳转
- **[target] **	

#### meta

​	元信息标签

- 定义与文档相关联的数据
- 字符集     charset
- 简介描述   description
- 关键字     keywords
- 页面重定向  http-equiv('refresh') + content(Xs;url=" ")	

#### link

​	外链文件标签

- icon  图标	
- stylesheet  样式





# CSS

### 特点

1. 样式和内容相分离.
2. 提高页面浏览速度.(采用css的页面容量小)
3. 外部样式表可以极大提高工作效率,易于维护和改版.



### 语法

1. css规则由 ''选择器 ''和 ''声明 ''两部分组成
   ​    选择器 用于指定 要修改样式的元素
   ​    声明 用于定义 元素的样式
2. 声明部分以  属性:属性值;  的形式组成.
3. 可以有一条或多条声明,每条声明之间 用分号隔开
4. CSS不区分大小写.
   !(两个例外: id 和 class 选择器 对大小写敏感)
5. 选择器和声明一起使用时,需要将 声明部分 用{}包裹起来.
6. 只有一条声明 或 多条声明的最后一条,可以省略分号.(建议都写完整)
7. 建议每条声明独占一行,提高可读性,也利于排错



### 长度单位

- px    像素
- em    倍数
- %     百分比
- cm/mm 厘米/毫秒
- pt    点,印刷单位



### 颜色单位

#### 英文

​        	red green blue pink

#### 16进制

​		0123456789abcdef

​		#**rrggbb**

- 白色 #FFFFFF   #FFF
- 黑色 #000000   #000
- 红色 #FF0000   #f00
- 绿色 #00FF00   #0f0
- 蓝色 #0000FF   #00f	 

#### RGB形式

​		0 ~ 255  /  %
​        	rgb(0,0,0)
​        	rgb(255,0,0)
​    		rgba(255,0,0,0.5)   0完全透明 1为不透明



### CSS引入

> 内联式  >  嵌入式  > 外链式



## CSS选择器

### 通配符选择器

​		*{....}

​		选择所有的元素,一般用于全局初始化	

### 标签选择器

​		标签{...}

​		选择对应的标签	

### ID选择器

​		#ID{...}

​		[id] 设置标签的ID

​		       ID是唯一存在的

​		       ID区分大小写

​		      必须以字母开头

​	              其他部分由:(A-Za-z)(0-9)-_ 组成	

### CLASS选择器

​		.CLASS{...}

​		        [class] 设置标签的类名

​			类名可重复定义

​			区分大小写

​			必须以字母开头

​			其他部分由:(A-Za-z)(0-9)-_ 组成

### 关联选择器/后代选择器

​		选择器1   选择器2 {...}

​			使用空格 根据上下文 来选择元素

### 子元素选择器

​		选择器1 > 选择器2 {...}

### 相邻兄弟选择器

​		选择器1 + 选择器2 {...}

​			选择某个 同级相邻的元素

### 相邻兄弟们选择器

​		选择器1 ~ 选择器2 {...}

​			选择某个 所有同级相邻的元素

### 组合选择器/分组选择器

​		选择器1,选择器2,选择器3{...}

​			获取几个不同的元素

### 权重

​	ID > 类 > 伪类 > 属性选择器 > 标签选择器 > 伪对象 > 通配符*

​    1.id选择器 为a
​    2.类选择器/属性选择器/伪类 为b
​    3.类型选择器/伪类对象选择器 为c
​    4.* 忽略(最低)
​    5.权重相同,就近原则	

### !important

```html
p{
    color: red!important;
 }
```



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

#### ​	其他

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

#### ​	作用

​		应用于浮动技术上

#### ​	注意

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

​	back  ground: image color position/size repeat attachment

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

### 合并边框​	

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



## 运算符

### 算术运算符

`+` `-` `*` `/` `%` `++` `--`

`++` 	自增

​	`a++`		先返回a,再给a+1

​	`++a`		先给a+1,再返回a

`--`	自减

​	`a--`

​	`--a`



### 赋值运算符

`=`		将 = 右边的赋给左边的

`+=`		a += b ==>  a = a + b

`-=`

`*=`

`/=`

`%=`		a %= b ==> a = a % b



### 比较运算符

`> >=`	

`< >=`

` ==`		判断两边的值是否相等

`===`	判断两边的值是否相等且数据类型是否相等

`!=`		判断两边的值是否不等

`!==`	只有全等时为false,其余都是true



### 逻辑运算符

`&&`		与假前,与真后

`||`		或假后,或真前

`!`		真既是假,假即是真



### 三元运算符

条件 ? true环境: false环境

使用场景:简单条件判断,if else的简化版



## 流程控制

### 结构

1. 顺序结构: 代码从上往下依次执行
2. 分支结构: 通过if 和 switch 来进行分支选择
3. 循环结构: 通过for,while等重复执行某段代码(功能)

### if

#### 分支1

​	if (条件表达式) 代码块;

​	if 条件只能影响到紧跟在后面的一句话

#### 分支2

​	if (条件表达式){

​		代码块

​	}

​	if条件能影响{}内的所有代码

#### 分支3

​	if (条件表达式) {

​		true环境

​	}else{

​		false环境

​	}

#### 分支4

​	if (条件表达式1){

​		true环境1

​	}else if (条件表达式){

​		true环境2

​	}else if (条件表达式3){

​		true环境3

​	}....

#### 分支5

​	if(条件表达式1){

​		if(条件表达式2){

​			if(条件表达式3){

​				代码块

​			}

​		}			

​	}

### switch

switch (标志){

​	case 标志1:代码块;

​		break;

​	case 标志2:代码块;

​		break;

​		 .  .  . 

​	case 标志N:代码块;

​		break;

​	default:

​		代码块



注意点

​	默认情况下,每执行一个case,默认会自动向下执行

​	若只执行一个case,需要在每个case的最后面,补上break

​	当匹配不到标志时,默认default

适用场景

​	if 适用于范围判断 和定值判断

​	switch 只适用于定值判断



### while

#### while 循环

​	while (条件表达式1){

​		代码块2

​	}

​	条件为真,则执行代码块

​	条件为假,则不执行代码块

#### do while 循环

​	do{

​		代码块

​	}while (条件表达式)

​	与while的区别

- while先判断条件,再决定是否执行代码块
- do while先执行1次代码块,再判断条件是否成立,最后决定是否执行第2次代码块
- do while无论条件是否成立,都至少会执行一次代码块

### for

#### for循环

​	for(初始值1; 条件表达式2; 增量3){

​		代码块4

​	}

​	执行顺序: 1 243 243 243 243 . . .

​	当条件表达式2不成立时,则结束for循环



#### for in 循环

​	for (键/索引 in 数组){

​		代码块

​	}

​	键 只能获取到当前的索引/键

​	获取值: 通过变量名[索引]来访问



### 特殊流程控制符

#### break

​	立马结束当前循环/分支,准备循环外的代码

#### continue

​	立马结束当前一轮循环,准备下一轮循环



## 函数

### 定义函数

#### ​	函数声明

​		function 函数名(参数. . .){

​			代码块	

​		}

#### ​	函数表达式

​		var 变量名 = function(参数 . . .){代码块}

#### ​	函数构造

​		var 变量名 = new Function('参数1','参数2', . . . , '代码块' )

​		注意点:

​			参数 和代码块 都必须要用引号包起来

​			Function 首字母需要大写





## 函数引用

1. 函数名 () 调用

   带小括号,立马执行函数

2. 函数名    引用

   不带小括号,且没有执行函数

3. (函数)()    自动执行函数,匿名函数

   一旦执行该行时,立马执行该函数



## 函数分类

形参 ： 在定义函数时，给的参数

实参 ： 在调用函数时，给的参数

实参个数 = 形参个数       完美

实参个数 > 形参个数       将多余的实参 全部抛弃

实参个数 < 形参个数        少的实参会是undefined或者报错 取决于作用域

实参个数不确定时		arguments 会接收到所有的实参



## 作用域

1. 全局变量

   在函数外部通过var 声明的变量

   在函数 内/外 ，不用var 定义的变量

2. 局部变量

   在函数内部通过var声明的变量



## 作用域链

1. 作用域链的特性

   对上封闭 ： 上面的不能用下面的

   对下透明 ：  下面的能用上面的

   访问顺序 ： 

   ​	优先 当前作用域

   ​	其次 上一级作用域 ，以此类推

   ​	最终 都找不到就报错

2. 定义

   作用域是在函数声明定义的 ， 不是在调用的时候定义的

   意味着：在函数声明时，局部的变量都已经声明好的，只是暂时未定义（没做赋值，相当于undefined）



## 获取标签对象

1. 通过id获取标签对象

   document.getElementById(id名)

2. 通过标签对象来获取html属性

   标签对象.html名

   注意:不是所有的属性都这么获取,需要特殊手段

3. 给标签设置/获取 style属性

   标签对象.style.属性名 = 属性值

4. 设置/获取标签的正文内容

   标签对象.innerHTML = 正文内容



## 动态改变标签属性

点击事件: 当点击某对象时,触发JS 

​		onclick = "js代码"



## 定时器

定时器:在指定时间之后,会执行某些事情

1. setTimeout(代码,时间)

   功能: 

   ​	在指定时间之后,执行一次代码功能

   ​	俗称: "俗称倒计定时器"

   参数:

   ​	代码: 可写功能字符串,函数名或'函数名( )'

   ​	时间: 毫秒

2. clearTimeout(定时器)

   功能:

   ​	清除定时器

3. setInterval(代码,时间)

   功能:

   ​	每隔一段时间,执行一次代码功能

   参数:

   ​	同setTimeout

4. clearInterval(定时器)

   功能:

   ​	清除定时器



## 对象

### 创建对象

1. 构造方式

   var 变量名/对象名 = new Object();

2. JSON方式

   var 变量名/对象名 = {

   ​	属性名1:属性值1,

   ​	属性名2:属性值2,

   ​	. . .

   ​	属性名N:属性值N,

   ​	方法名: function(){

   ​		代码块

   ​	},

   ​	. . .

   }

3. 自定义构造函数

   function 函数名(){

   ​	this.属性名1 = 属性值1;

   ​	this.属性名2 = 属性值2;

   ​	 . . .

   ​	this.属性名N = 属性值N;

   ​	this.方法名 = function(){

   ​		代码块

   ​	}

   ​	. . .

   }

4. 匿名构造函数

   var 变量名/对象名 = new function(){

   ​	this.属性名1 = 属性值1;

   ​	this.属性名2 = 属性值2;

   ​	. . .

   ​	this.属性名N = 属性值N;

   ​	this.方法名 = function(){

   ​		代码块

   ​	}

   ​	. . .

   }



## 创建对象的对象

Python中 有祖宗类 Object

Js中查询父级对象

对象.constructor



## Js原型

> 原型就是Python的类属性 类方法

1. 设置属性和方法
   - 独享设置
     - 对象名.属性名 = 属性值
     - 对象名.方法名 = function(){代码块}
   - 共享设置
     - 对象名.prototype.属性名 = 属性值
     - 对象名.prototype.方法名 = function(){代码块}
2. 删除对象
   - 关键字: delete
   - 格式:
     - delete 对象.属性名
     - delete 对象.方法名
   - delete 删除属性后,再次使用该属性时,则变为undefined
   - delete 删除方法后,方法则不存在,再次使用报错
   - delete 实例化后不能使用
   - delete 自带属性和方法可以使用



## 数组

1. 创建数组
   - 构造创建
     - var 数组名 = new Array(值1,值2,值3, . . .)
   - JSON创建
     - var 数组名 = [值1,值2,值3 , . . . ]
2. 多维数组
   - 数组中嵌套数组



## 数组操作

1. 新增数组/修改数组

   数组名[键] = 值

   键不存在,则为新增

   键已存在,则为修改

   键为Number,会计入length

   键为string,不会计入length

2. 访问数组

   格式: 数组名[键]

   ​	如果键不存在,则返回undefined



## 遍历数组

通过循环一个一个获取数组中的值

```html
<script>
	var list = [ '熊初墨', '王根基', '倪霸霸', '于伟文', '黄阿玛' ];
	console.log( list, typeof(list));
	console.log( list.length );
    for(var i = 0, j = list.length; i < j; i++){
		document.write(i + ' ====> ' + list[i] + '<br />');
	}
</script>
```



## 遍历元素集合

```html
<ul id="nav">
   <li>小米</li>
   <li>红米</li>
   <li>笔记本</li>
   <li>路由器</li>
</ul>
<script>
	var nav = document.getElementById('nav');
    // 获取 htmlCollection集合对象
	var li = nav.getElementsByTagName('li');  
	console.log(nav);
	console.log(li);
	// 遍历 li
	// 	需求1: 字体设置为 red
	// 	需求2: 原有内容基础上加 序号
	for(var i = 0; i < li.length; i++){
		li[i].style.color = 'red';
		li[i].innerHTML += i;
	}
</script>
```



## 内置对象-Array

#### 不会改变原数组的方法

- concat() 合并数组
- join() 数组转为字符串
- slice(x,y) 截取数组 [x,y)

#### 会改变原数组的方法

- push() 在末尾插入一个值
- pop() 删除末尾值
- unshift() 在开头插入一个值
- shift() 删除开头值
- reverse() 反转数组
- sort() 按照 ASCII 排序





## 事件event

#### 事件绑定1

​	<开始标签 事件  = "js代码">

#### 事件绑定2

​	元素对象.事件 = function(){代码块}

​	元素对象.事件 = 函数名    没有小括号

#### 事件监听

​	标准: 元素对象.addEventListener(事件,函数,bool)

​	IE: 元素对象.addachEvent(事件,函数)

​	bool:

​		true:事件捕获 -->先触发父级,再触发子集

​		false:事件冒泡,默认 --> 先触发子集,再触发父级

#### 解除绑定

​	元素对象.事件 = null

​	元素对象.事件 = function(){} 空函数

#### 解除监听

​	元素对象.removeEventListener(事件,函数,bool)

​	元素对象.detachEvent(事件,函数)



## 绑定一组元素与this的使用

1. 获取一组标签

   元素对象.getElementsByTagName('标签名')

   document:整个页面

   指定标签对象: 指定标签

2. this

   代表当前对象

   谁用this,this就代表谁



## 闭包

闭包:主要作用就是让数据持久化



## 常见鼠标事件

- onclick       		左击, 单击
- ondblclick     		双击
- oncontextmenu  	右击
- onmouseover    	划入  hover
- onmouseout     	划出
- onmousedown    	按下
- onmouseup     	松开
- onmousemove    	移动



## event事件

#### event 对象

​	代表事件的状态

​	例如: 

​		在事件中发生的 按键, 鼠标移动 等

#### 获取event对象

​	在事件触发时的函数形参处 赋予event

​	xxx.onclick = function( event ){}	

#### 注意点

​	通常事件 配合函数使用

​	window.event 主要兼容IE

​	event 名字可以变换

#### 常用event属性

- event.x       鼠标的x坐标
- event.y       鼠标的y坐标
- event.button   获取鼠标按键   左键0 / 右键2  / 中键1
- event.offsetX  鼠标相对于 触发事件的x坐标
- event.offsetY  鼠标相对于 触发事件的y坐标



## 键盘事件

onkeydown   按键按键触发

onkeyup    	松开按键触发

onkeypress 	按下并松开触发 (js高级事件)

​			并非所有按键都会触发

event属性

​	keyCode    当前按键的 Unicode编码



## 表单事件

onsubmit       表单提交时触发

onfocus       	表单获取到光标时触发

onblur           	表单失去光标时触发

onchange      改变表单的内容或状态时触发

oninput       	输入内容时触发

onselect      	内容框中时 触发



## 正则

> 用于搜索, 替换, 验证等功能

1. 语法

   格式:  / 正则表达式 /模式修正符

2. 原子

   可见原子:  键盘输出之后, 肉眼可见的字符  例如: 数字, 字母, 标点...

   不可见原子: 键盘输出之后, 肉眼看不见的字符 例如: 空格, 回车, 制表符     

   原子在正则中, 是最小单位

3. 元字符 

   [ ]       		匹配 []中任意一个原子

   [x-y]  		匹配 x-y 中的任意一个原子

   `[^ ]`		匹配 除了[ ] 外任意一个原子

   |     			匹配 竖线的左边 或 右边的整体

   ( )       		将( )内的原子当成一个整体, 看做是一个大原子

   (abc|xyz)  	匹配竖线左边的abc 或 右边的xyz

   .       		小数点, 匹配任意字符 (除了换行符)

   \d        		匹配任意一个数字  [0-9]

   \D    		`[^0-9]`

   \s        		匹配任意一个不可见原子  包含空格, 回车, 制表符..

   \S          		一个可见原子

   \w        		匹配任意一个 数字, 字母, 下划线

   \uxxxx  		查找十六进制规定的字符

   ​			xxxx : 4位十六进制数

   ​			\u 不变的, 固定的

   ​				汉字: \u4e00 ~ \u9fa5

   {n}    		连续匹配前面一个原子出现正好 n次

   {n,}   		连续匹配前面一个原子出现最少 n次

   {n,m}  		连续匹配前面一个原子出现最少 n次, 最多m次

   `*`			{0,}   最少0次

   `+`			{1,}   最少1次

   ?     			{0,1}  最少0次, 最多1次

   ^    			匹配字符串的开头

   $     			匹配字符串的结尾

4. 匹配函数

   match( 正则 )

   返回值: 匹配到的内容

   注意:

   ​	仅匹配一次

   ​	匹配不到, 则返回null

5. 替换函数

   replace( 正则, 替换值)

   返回值: 替换之后的内容

   注意:

   ​	仅替换一次

   ​	匹配不到, 则返回 原来的值

6. 模式修正符

   i  	不区分大小写

   g  	全部匹配

   正则默认严格区分大小写

   另类用法

   ​	在匹配发生歧义时???

   ​		贪婪: .*

   ​		懒惰: .*?

7. 后向引用

   ( )    		功能1: 将 ( ) 内的内容当成一个大原子

   ​		功能2: 将 ( ) 内的内容存入 子模式组

   ​			\1: \1引用第一个( )的值, 两处的值保持同步

   ​			\2: \2引用第二个( )的值, 两处的值保持同步
   ​			. . .

   ​			\n: \n引用第n个( )的值, 两处的值保持同步

   ​	条件:

   ​		必须要有 ( ),  \n 才能使用

   ​		在字符串中用 \n, 可以用 $n 代替

8. 取消子模式

   ​	(?:  )  该( ) 的值 不会送进子模式组

9. 正向预查

   ​	(?=  )        预先检查后面的值    向右

10. 负向预查

    ​	(?!  )        预先检查前面的值     向左



## 页面加载事件

- onload     			页面或图像加载成功时 触发

- onunload   			页面关闭时触发     IE

- onbeforeunload 		页面关闭时触发 非IE

  ​					浏览器阻止关闭前的弹窗, 需要return "string"

- onabort    			图片加载过程中 中断触发

- onerror    			图片加载出错时 触发

- onscroll   			元素滚动条在滚动时 触发



## 滚动事件

1. 当前位置

   对象.offsetTop      	距离 屏幕或祖辈定位的 最顶部的距离

   对象.offsetLeft     		距离 屏幕或祖辈定位的 最左侧的距离

   对象.offsetWidth        	对象本身的宽度

   对象.offsetHeight       	对象本身的高度

2. 滚动条

   滚动条距离顶部的距离

   ​	对象.scrollTop

   ​		document.documentElement.scrollTop || document.body.scrollTop || window.pageYOffset

   滚动条距离左侧的距离

   ​	对象.scrollLeft 

   条件限制:

   ​	必须要有溢出 才能滚动



## BOM

BOM 浏览器对象模型

​	能与浏览器窗口进行交互

​	核心对象: window

- window对象

  根对象, 描述整个窗口

  常用方法

  ​	alert( )   警告框, 无返回值

  ​	confirm( )  确认框, 返回值: bool

  ​	prompt( )   输入框, 返回值: 内容  

  ​				 取消:  null

  ​	setInterval( )

  ​	setTimeout( )

  ​	clearInterval( )

  ​	clearTimeout( )

- navigator对象

  包含了 浏览器相关的信息

  使用格式:  navgiator.属性名/方法名() 

  功能包含:

  ​	浏览器名

  ​	平台

  ​	版本

  ​	当前操作系统

  ​	是否脱机

  ​	User-agent头信息  (终端设备, 版本号)

- history对象

  包含了 历史记录

  使用格式:  history.属性名/方法名()

  功能包含: 

  ​	上一个访问地址

  ​	下一个访问地址

  ​	访问过多少地址

- Location对象

  包含了 当前URL信息

  使用格式: Location.属性名/方法名()

  功能包含:

  ​	当前url地址

  ​	当前端口

  ​	当前协议

  ​	当前参数

- Screen对象

  包含了 客户端屏幕的信息

  使用格式:  screen.属性名/方法名()

  功能包含:

  ​	屏幕宽度

  ​	屏幕高度

  ​	刷新率 

  ​	分辨率



## DOM

定义HTML 和 XML的访问标准

​	xml?

​		html 就是 标签属性, 显示数据

​			预定义好的

​		xml  就是 描述数据, 存储数据

​			自定义, 可以扩展



### DOM 节点

在html中所有的东西 都是节点

- 整个文档节点: document
- html元素节点: element
- html属性节点: attr
- html内容节点: text   (包含 空格)
- 注释节点: comment



### 节点关系

- 父节点
- 子节点
- 祖辈节点
- 后辈节点
- 同辈节点



### 节点访问

#### 方法

- getElementById( )
- getElementsByTagName( )
- getElementsByClassName( )
- getAttributeNode( )    获取属性节点
- getAttribute( )       获取属性值

#### 属性

- attributes    获取属性节点
- parentNode     获取父级节点
- childNodes     获取子级节点
- parentElement  获取父级元素
- children      获取子级元素



### 节点属性

#### nodeName

- 文档节点的 nodeName 始终都是 #document
- 元素节点的 nodeName 始终都是 标签名
- 属性节点的 nodeName 始终都是 属性名
- 内容节点的 nodeName 始终都是 #text

#### nodeValue

- 元素节点的 nodeValue 始终都是 null 就是 undefined
- 属性节点的 nodeValue 始终都是 属性值
- 内容节点的 nodeValue 始终都是 正文内容

#### nodeType

- document   	 9
- element          1
- attr                  2  
- text                  3
- comment        8



### 节点操作

#### 修改属性值

​	元素节点.setAttribute(属性名, 属性值)

​	元素节点.属性名 = '值'

#### 创建节点

​	属性: document.createAttribute('属性名');

​	元素: document.createElement('标签名');

#### 删除节点

​	属性:  removeAttribute() 

​		  或者 把值设置为null

​	元素:  removeChild(节点)   删除父节点的一个子节点

#### 替换节点

​	属性:  setAttribute(属性名, 属性值)

​	元素:  replaceChild(新节点,旧节点);

#### 插入节点

​	属性: setAttribute(属性名, 属性值)

​	元素: appendChild(node)            插入子节点

​		 insertBefore(新节点, 旧节点)   指定位置插入节点

#### 克隆节点

​	cloneNode()    

​		false(默认值)

​		true(全部复制)





## jQuery 框架

jQuery 只是JavaScript的一个轻量级框架

​	写得少, 干得多

优势:

- 开源
- 便捷的选择器
- 方便的DOM操作
- 动画操作
- 简化ajax
- 兼容性



### jQuery 安装

一般jq就两个版本

​	一个测试版, 用于测试, 有良好的代码排版

​	一个迷你版, 用于实际项目中, 已被精简和压缩

经典版本: jquery-1.8.3

最新版本: jquery-3.3.1 (至今 2019年1月)



### jQuery 基本语法

```
$(对象).操作(function(){
	代码块
})
```

### 简化写法

```
$(function(){
	代码块
});
```



## Ajax

> 简介:asyn javascript and xml   异步的 js 和 xml

同步: 发出一条指令后,在没得到结果前,就不能做其他事情 (事情一个一个做)

异步: 发出一条指令后,在没得到结果前,可以选做其他事     (事情分布式完成)

#### HTTP基本原理

##### ​	请求

​		客户端向服务器请求一个文件

##### ​	响应

​		服务器将文件内容返回给客户端,文件有了输出才算真正的响应

传统的请求 通过url地址栏 刷新请求

Ajax	    通过技术 偷偷的请求	

主要用于 在无刷新的情况下,局部改变数据

```html
$.ajax({
	url: 'py地址',
	type: '传输方式',
	data: {参数名1:参数值1,参数名2:参数值2,...},
	success:function(){
		响应成功后,功能代码块
	},
	error:function(){
		响应失败后,功能代码块
	}
})
```

#### 注意

​	url:ajax要传输的地址

​	type:默认get

​	data:常用json格式

​		也可以用"参数名1=参数值1&参数名2=参数值2& ..."

​	success:请求成功后的回调函数

​	error:请求失败后的回调函数

​	datatype:预期服务器返回的数据类型

#### 服务器

​	Apache

​	Nginx

​	IIS

​	Tomact

​	. . .

#### 常见状态码

​	200		成功响应

​	304		文件来自于缓存

​	404		文件不存在

​	500		服务器未知错误

​	503		服务器宕机(死机)或服务器不可用

​	2xx		成功...

​	4xx		客户端的问题

​	5xx		服务器的问题



## Bootstrap

1. 简介

   ​是一个前端框架

2. 作用

   常用于响应式布局,移动设备

3. 官方地址

   http://www.bootcss.com/

4. 下载安装

   https://v3.bootcss.com/getting-started/#download

5. BootStrap的结构

   css

   ​	bootstrap.css		学习版(良好的代码排版)

   ​	bootstrap.min.css	实际开发使用的版本,被压缩过的

   ​	bootstrap-theme.css	主题

   js	

   ​	基于jQ的js

   fonts 

   ​	字体图标

   免费主题模版

   ​	http://www.bootswatch.com



