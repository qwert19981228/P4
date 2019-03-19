from urllib import request

# get  参数铭文显示
# www.baidu.com/?name=zhansgan&age=18

base_url = 'https://movie.douban.com/typerank?type_name=%E7%88%B1%E6%83%85%E7%89%87&type=13&interval_id=100:90&action='

# 发送请求
response = request.urlopen(base_url)

# 处理响应
print(response.read().decode('utf-8'))