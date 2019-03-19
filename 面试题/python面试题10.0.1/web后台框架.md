### web后台框架

#### 理论简单题

```python
1. Django 、Flask、Tornado的对比
答案:
    1.Django走的是大而全的方向,开发效率高。它的MTV框架,自带的ORM,admin后台管理,自带的sqlite数据库和开发测试用的服务器
    给开发者提高了超高的开发效率
    2.Flask是轻量级的框架,自由,灵活,可扩展性很强,核心基于Werkzeug WSGI工具和jinja2模板引擎
    3.Tornado走的是少而精的方向,性能优越。它最出名的是异步非阻塞的设计方式
    Tornado的两大核心模块：
        1.iostraem：对非阻塞式的socket进行简单的封装
        2.ioloop：对I/O多路复用的封装，它实现了一个单例
```

```python
2.简述MVC和MTV
答案:
    MVC软件系统分为三个基本部分：模型(Model)、视图(View)和控制器(Controller)
    Model：负责业务对象与数据库的映射(ORM)
    View：负责与用户的交互
    Control：接受用户的输入调用模型和视图完成用户的请求
    Django框架的MTV设计模式借鉴了MVC框架的思想,三部分为：Model、Template和View
    Model(模型)：负责业务对象与数据库的对象(ORM)
    Template(模版)：负责如何把页面展示给用户
    View(视图)：负责业务逻辑，并在适当的时候调用Model和Template
    此外,Django还有一个urls分发器,
    它将一个个URL的页面请求分发给不同的view处理,view再调用相应的Model和Template
```

```python
3.Django中如何读取和保存session，整个session的运行机制是什么?
答案:
    说到session的运行机制，就一定要先说一下cookie这一段信息。一般情况下cookies都是我们的浏览器生成的（显然可以人为修改），用于服务器对户进行筛选和维		护，但是这个听上去很好吃的东西，能存的东西有点少而且容易被别人利用。这时候基于cookies的session的意义就比较明显了，在客户端的cookies中我们只保		存session id，而将完整信息以加密信息的形式保存到服务器端，这样服务器可以根据session id相对安全的在数据库中查询用户的更细致的信息和状态。
    在Django中session和cookies的操作方法一样，如下：
    # 保存session
    request.session['order_id'] = order_id
    # 删除session
    del request.session['order_id']
    # 读取session
    session.get('order_id', False)
```

```python
4. cookie和session的区别： 
答案:
    1.cookie:
        cookie是保存在浏览器端的键值对,可以用来做用户认证
    2.session：
       将用户的会话信息保存在服务端,key值是随机产生的自符串,value值时session的内容
        依赖于cookie将每个用户的随机字符串保存到用户浏览器上
    Django中session默认保存在数据库中：django_session表
    flask,session默认将加密的数据写在用户的cookie中
```

```python
6.请简要的说明Django框架中视图的作用?

答案:
	在Django框架中视图是:定义完成各类对象所需功能的函数,接收请求,处理业务逻辑,返回结果.
```

```python
7.简述Django对http请求的执行流程?

答案:
    一个 HTTP 请求，首先被转化成一个 HttpRequest 对象，然后该对象被传递给 Request 中间件处理，如果该中间件返回了Response，则直接传递给 Response 中间	   件做收尾处理。否则的话 Request 中间件将访问 URL 配置，确定哪个 view 来处理，在确定了哪个 view 要执行，但是还没有执行该 view 的时候，系统会把 		request 传递给 View 中间件处理器进行处理，如果该中间件返回了Response，那么该Response 直接被传递给 Response 中间件进行后续处理，否则将执行确定的 	 View 函数处理并返回 Response，在这个过程中如果引发了异常并抛出，会被 Exception 中间件处理器进行处理。
```

```python
8.Django和Flask有什么区别？

答案示例:
	Flask
    ·轻量级web框架，默认依赖两个外部库：jinja2和Werkzeug WSGI工具
    ·适用于做小型网站以及web服务的API，开发大型网站无压力，但架构需要自己设计
    ·与关系型数据库的结合不弱于Django，而与非关系型数据库的结合远远优于Django
	Django
    ·重量级web框架，功能齐全，提供一站式解决的思路，能让开发者不用在选择上花费大量时间。
    ·自带ORM(Object-Relational Mapping 对象关系映射)和模板引擎，支持jinja等非官方模板引擎。
    ·自带ORM使Django和关系型数据库耦合度高，如果要使用非关系型数据库，需要使用第三方库
    ·自带数据库管理app
    ·成熟，稳定，开发效率高，相对于Flask，Django的整体封闭性比较好，适合做企业级网站的开发。
    ·python web框架的先驱，第三方库丰富
```

###### 

```python
9.ession和cookie的联系与区别；session为什么说是安全的
    key就是sessionid,需要存储在客户端的cookie中
    而value值会被记录在服务器端(如数据库,内存,文件登陆)
    每一次用户请求时,会在cookie中携带sessionid与服务器中存储的session进行对应
    因此.session和cookie的区别在于,session存在服务器端,cookie存在客户端,而session的存储与操作需要依赖客户端的cookie,而由于session数据存储在服务端, 	  不会轻易被获取,因此说session是安全的

    HTTP协议是无状态的：
    •	每次请求都是一次新的请求，不会记得之前通信的状态
    •	客户端与服务器端的一次通信，就是一次会话
    •	实现状态保持的方式：在客户端或服务器端存储与会话有关的数据
    •	状态保持的目的是在一段时间内跟踪请求者的状态，可以实现跨页面访问当前请求者的数据
    •	注意：不同的请求者之间不会共享这个数据，与请求者一一对应
    Cookie
    •	 存储在用户的浏览器中,
    •	 不要存储敏感信息,不安全
    •	 内容有限,格式有限,
    Session
    •	存储在服务器(文件,数据库,缓存|内存)
    •	每一个数据产生一个key session_id 就存储在浏览器的cookie
    •	数据存在服务器,不容易被暴露信息
```

```python
10.Django中如何读取和保存session
    #session设置
     request.session[key] = value
    #session获取
     request.session.get(key,default=Node)
    #session删除
    # 删除单个key 不存在时报错
     del request.session['a'] 
    #清除所有会话,但不会删除数据
     request.session.clear() 
    #删除当前的会话数据
     request.session.flush()
 
```

```python
11.Django中查询queryset时什么情况下用Q?
    关键字参数查询 - 输入filter()等 - 是“AND”编辑在一起。如果需要执行更复杂的查询（例如，带OR语句的查询），则可以使用。Q objects
    例如需要进行复合条件的查询的SQL语句如下：
    select * from goods where name like '%好看%' or title like '%好看%'; 

    使用Q就可以写成：
    from django.db.models import Q
    obs = Goods.objects.filter(Q(name__contains='好看')|Q(title__contains='好看'))
```

```python
12.Django中的Q对象还有哪些用法?
    Q对象不止用于 or,还能把and和or的语句联合在一起使用
    例如以下sql语句:
    SELECT * from polls WHERE question LIKE 'Who%'
        AND (pub_date = '2005-05-02' OR pub_date = '2005-05-06')
    使用Q对象同样可以
    Poll.objects.get(
        Q(question__startswith='Who'),
        Q(pub_date=date(2005, 5, 2)) | Q(pub_date=date(2005, 5, 6))
    )
```

```python
13.Django框架的优缺点
    •	被官方定义为完美主义者框架,提供一站式的解决方案
    •	从模板、视图,模型ORM、Session等等都分配好了
    •	提供了admin自动后台管理,测试,表单等功能
    •	作为web框架太重了，很多不用的组件和应用也都之间在框架中安装了
    •	能开发小应用，但总会有“杀鸡焉用牛刀”的感觉
    •	框架中的组件之间耦合度过高,不易拆分使用(例如数据验证需要表单配合...)
```

```python
14.Flask框架的优缺点
    •	Flask只提供了一些核心功能，非常简洁优雅.被称为python中的'微'框架
    •	自由、灵活，可扩展性强.入门简单,
    •	非常适用于开发web服务的API
    •	使用BluePrint架构开发大型网站无压力
    •	第三方库的选择面广，开发时可以结合自己最喜欢用的轮子，也能结合最流行最强大的Python库
```

```python
15.请描述 MVC和MVT
    MVC:
    •	M全拼为Model，主要封装对数据库层的访问，对数据库中的数据进行增、删、改、查操作。
    •	V全拼为View，用于封装结果，生成页面展示的html内容。
    •	C全拼为Controller，用于接收请求，处理业务逻辑，与Model和View交互，返回结果。
    MVT:
    •	M全拼为Model，与MVC中的M功能相同，负责和数据库交互，进行数据处理。
    •	V全拼为View，与MVC中的C功能相同，接收请求，进行业务处理，返回应答。
    •	T全拼为Template，与MVC中的V功能相同，负责封装构造要返回的html。
```

```python
16.MVC的核心思想
	程序解耦，让不同的代码块之间降低耦合，增强代码的可扩展和可移植性，实现向后兼容。
```
```python
17.简述Django请求生命周期
答案:
    一般是用户通过浏览器向我们的服务器发起一个请求(request)，这个请求回去访问视图函数，（如果不涉及到数据调用，那么这个时候视图函数返回一个模板也就是一     个网页给用户），
    视图函数调用模型，模型去数据库查找数据，然后逐级返回，视图函数把返回的数据填充到模板中空格中，最后返回网页给用户。
    1.wsgi,请求封装后交给web框架 （Flask、Django）     
    2.中间件，对请求进行校验或在请求对象中添加其他相关数据，例如：csrf、request.session - 
    3.路由匹配 根据浏览器发送的不同url去匹配不同的视图函数    
    4.视图函数，在视图函数中进行业务逻辑的处理，可能涉及到：orm、templates => 渲染 - 
    5.中间件，对响应的数据进行处理。 
    6.wsgi,将响应的内容发送给浏览器。
```

```python
18.Django中想验证表单提交是否格式正确需要用到Form中的哪个函数？
答案:
	is_valid()
```

```python
19.Flask-WTF是什么，有什么特点？
答案:
    Flask-wtf是一个用于表单处理,校验并提供csrf验证的功能的扩展库
    Flask-wtf能把正表单免受CSRF<跨站请求伪造>的攻击 
```

```python
20.Django 作为一个 Web 开发框架，它包括哪些基本组成部分：
答案：
    HTTP 请求处理与响应
    URL 映射
    视图控制
    模板系统
    数据库操作模型
```

```python
21.django路由系统中name的作用：
答案：
	用于反向解析路由,相当于给url取个别名，只要这个名字不变,即使对应的url改变，通过该名字也能找到该条url。
```

```python
22.什么是中间件并简述其作用?
    中间件是一个用来处理Django的请求和响应的框架级别的钩子。它是一个轻量、低级别的插件系统，用于在全局范围内改变Django的输入和输出。每个中间件组件都负     责做一些特定的功能。
    中间件是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变django的输入与输出。
```

```python
23.命令migrate 和makemigrations的差别?
    生成迁移文件
    执行迁移
```

```python
24.django有哪几个组成部分?
	urls.py,
	views.py,
	models.py,
	forms.py,
	templates,
	admin.py,
	settings.py
```

```python
25.列举django的内置组件？
    1.Admin是对model中对应的数据表进行增删改查提供的组件
    2.model组件：负责操作数据库
    3.form组件：1.生成HTML代码2.数据有效性校验3校验信息返回并展示
    4.ModelForm组件即用于数据库操作,也可用于用户请求的验证
```

```python
26.什么是wsgi,uwsgi,uWSGI？
答案：
    WSGI:
        web服务器网关接口,是一套协议。用于接收用户请求并将请求进行初次封装，然后将请求交给web框架
        实现wsgi协议的模块：
            1.wsgiref,本质上就是编写一个socket服务端，用于接收用户请求(django)
            2.werkzeug,本质上就是编写一个socket服务端，用于接收用户请求(flask)
    uwsgi:
        与WSGI一样是一种通信协议，它是uWSGI服务器的独占协议,用于定义传输信息的类型
    uWSGI:
        是一个web服务器,实现了WSGI协议,uWSGI协议,http协议,
```

```python
27.简述什么是FBV和CBV？
答案：
    FBV和CBV本质是一样的
    基于函数的视图叫做FBV，基于类的视图叫做CBV
    在python中使用CBV的优点：
    1.提高了代码的复用性，可以使用面向对象的技术，比如Mixin（多继承）
    2.可以用不同的函数针对不同的HTTP方法处理，而不是通过很多if判断，提高代码可读性
```

```python
28.django中csrf的实现机制
    第一步：django第一次响应来自某个客户端的请求时,后端随机产生一个token值，把这个token保存在SESSION状态中;同时,后端把这个token放到cookie中交给前端	  页面；
    第二步：下次前端需要发起请求（比如发帖）的时候把这个token值加入到请求数据或者头信息中,一起传给后端；Cookies:{csrftoken:xxxxx}
    第三步：后端校验前端请求带过来的token和SESSION里的token是否一致。
```
```python
29.基于django使用ajax发送post请求时，都可以使用哪种方法携带csrf token？
    1.后端将csrftoken传到前端，发送post请求时携带这个值发送
    data: {
            csrfmiddlewaretoken: '{{ csrf_token }}'
      },
    2.获取form中隐藏标签的csrftoken值，加入到请求数据中传给后端
    data: {
              csrfmiddlewaretoken:$('[name="csrfmiddlewaretoken"]').val()
         },
    3.cookie中存在csrftoken,将csrftoken值放到请求头中
    headers:{ "X-CSRFtoken":$.cookie("csrftoken")}
```

```python
30.说一下Django，middlewares中间件的作用？
答：
	中间件是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变django的输入与输出。
```