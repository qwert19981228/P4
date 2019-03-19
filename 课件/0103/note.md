web发展

    web 1.0 

    web 2.0 

    web 3.0  人-网络-人
        






表单

    什么是表单
        用户和网站  交互的地方
        就是用户给网站留下数据的地方
        是在网页中 提供输入数据的界面

    什么地方用到了表单
        
        

    表单能做什么
        收集数据
        

    如何定义表单

<form></form>    定义 表单域
    页面中可以有多个表单
    不能嵌套使用
    所有的表单内容 都出现在 该标签内
    [action]    指定 接收数据的 脚本文本
    [method]    规定 如何发送表单数据
        get    默认值, 使用URL传参
        post   使用HTTP post 方式传参(隐蔽传参)


<input>    输入框标签
    用于定义一个输入的区域
    
    [type]    规定输入域的功能
        text        文本输入框(默认)
        password    密码输入框
            密码输入框中的字符 都会被显示为 * 或 圆点
        radio      单选按钮
            [checked]  默认选中的状态,值为checked
        checkbox   多选按钮
            [checked]  默认选中的状态,值为checked
        file       文件上传域
            上传文件必须使用post方式
            file  不能使用value属性
            [enctype]    规定表单 在发送到服务器之前 应该如何对数据进行编码
                application/x-www-form-urlencoded
                multipart/form-data   文件上传专用
        hidden     隐藏域

        submit     提交按钮
        reset      重置按钮
        button     普通按钮

        number  限定为数值的值
            [max] 输入范围限定
            [min] 输入范围限定
        time   限制时间
        email  限制邮箱


    [name]    给表单项 设定一个数据标识
        一定要设置 输入框的name值
        只有设置了此值,那么在提交时 数据才能被传递
    
    [value]    为input元素设定值
        text / password  / hidden
            定义输入输入框的初始值
        radio / checkbox
            定义与输入框相关的值
        submit / reset / button
            定义按钮的功能文本
    
    [maxlength]    输入字符的最大长度,单位字符个数
    [minlength]    输入字符的最小长度,单位字符个数
    [size]    宽度,单位字符
    [placeholder]    提供可描述的提示信息(HTML5)
        输入框为空时 才会显示
    [readonly]    只读
        可看到,亦可提交
    [disabled]    禁用此元素
        被禁用的元素 是无法提交到后端的


<label></label>    为input元素 定义标注(标记)
    多用于 单选/多选时  与input 组合使用
    当用户选择该标签时,浏览器就会自动将焦点 转到和该标签相绑定的元素身上

<select></select>  下拉框
    [name]  不可缺少
<option></option>  下拉选项
    需要写在 select 的内部
    [value]  设定初始值
    [selected]  默认选中状态
    [size]   显示下拉个数
    [multiple] 拉下多选

<textarea></textarea>   多行文本域
    [name]   标识
    [rows]   设置该文本域的行数(宽度)
    [cols]   设置该文本域的列数(高度)
    [placeholder]    提供可描述的提示信息(HTML5)
    [maxlength]    输入字符的最大长度,单位字符个数
    

<button></button>   普通的按钮
    需要设不同的type值 来实现不同的功能



PS. 扩展部分

GET 与 POST 的区别
    1.get会把所有数据显示到浏览器地址栏上,post是通过HTTP post机制，所以不会显示。
    2.get传送数据量较小，一般不能大于2KB，post传送的数据量较大，理论上不受限制。
    3.post比get相对安全一些，
    4.get通常传递不太重要的小量信息

HTTP请求
    HTTP协议是无状态协议,无状态是指浏览器和Web服务器之间不需要建立持久的连接，这意味着当一个客户端向服务器端发出请求，然后Web服务器返回响应，连接就被关闭了，在服务器端不保留连接的有关信息.
    建立TCP连接---发送请求命令---浏览器发送请求头信息---服务器应答---服务器发送应答头信息---服务器向浏览器发送数据---服务器关闭TCP连接
    如何查看HTTP请求
    浏览器F12---network---重载页面即可查看到请求信息



---------------------------------

分帧
    就是把浏览器 分成多个窗口来显示 不同的网页

    <frameset></frameset>
    <frame>
    <iframe></iframe>




----------------------------------

head 内的功能标签
