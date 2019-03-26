# Django搭建一个B2C 商城

## 项目简介


## 项目模块


## 项目技术


## 安装说明

## 联系我们


## 赞赏


## 项目QA

###1. 模板样式 不显示
- staic 配置
- 注意你的路径问题!

###2. url匹配规则 为什么要加myadmin
例子: 127.0.0.1:8000/myadmin/index

127.0.0.1:8000    当前py运行的项目地址

/myadmin          去访问 myadmin 应用下的 urls

/index            在 myadmin/ulrs 匹配  /index

###3. 不要自己创造标签
{%  %}   √
{ % % }  ×

###4. urls partterns

记住 匹配路由 末尾 , 加  '$'
例子: url(r'^user/add/$',views.useradd,name="myadmin_user_add"),




