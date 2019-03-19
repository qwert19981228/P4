# 导包
from urllib import request,parse
import json

# url地址
base_url = 'https://fanyi.baidu.com/sug'
def fanyi(msg):
    # 数据格式化
    data = {
        'kw':msg
    }
    newdata = parse.urlencode(data)

    # 发送请求
    response = request.urlopen(url=base_url,data=bytes(newdata,encoding='utf-8'))

    # 处理响应
    jsondata = response.read().decode('utf-8')
    # 将json字符串 转换成字典
    jsondict = json.loads(jsondata)
    # print(type(jsondict))
    # print(jsondict)

    for item in jsondict['data']:
        print(item['v'])

if __name__ == "__main__":
    while True:
        msg = input('请输入要翻译的内容：')
        if msg == 'q':
            break
        fanyi(msg)




# 格式化字典 将字典转成json的数据 b并格式化输出
# jsonstr = json.dumps(jsondict,indent=4,ensure_ascii=False)
# print(jsonstr,type(jsonstr))
