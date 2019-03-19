from urllib import request,parse
import os,re
# url地址
base_url = "https://tieba.baidu.com/f?"
# 数据格式化
def tieba(msg,head):
    data = {
        'kw':msg,
        'pn':(head-1)*50
    }
    newdata = parse.urlencode(data)
    #发送请求
    response = request.urlopen(url=base_url+newdata)
    # 处理响应
    jsondata = response.read().decode('utf-8','ignore')
    #创建路径
    targetPath = os.getcwd() + os.path.sep + msg+os.path.sep
    # 判断路径存不存在
    if not os.path.exists(targetPath):
        # 创建文件夹
        os.makedirs(targetPath)
    with open('./{msg}/{msg}第{head}页.html'.format(msg=msg,head=head),'w+',encoding='utf-8')as f:
        f.write(jsondata)
    print("第{}页成功".format(head))
    pat = re.compile(r'<a rel="noreferrer" href="/p/(.*?)" .*?>.*?</a>')
    res = pat.findall(jsondata)
    for i in res:
        tiezi = request.urlopen(url="https://tieba.baidu.com/p/" + i)
        tiezidata = tiezi.read().decode('utf-8')
        imgs = re.compile(r'<img class="BDE_Image" src="(.*?)".*?>')
        tu = imgs.findall(tiezidata)
        for item in tu:
            # 创建路径
            imgPath =targetPath + 'img' + os.path.sep
            # 判断路径存不存在
            if not os.path.exists(imgPath):
                # 创建文件夹
                os.makedirs(imgPath)
            fname = item.split('/')[-1]
            request.urlretrieve(item,imgPath+fname)
            print("下载成功")
if __name__ == '__main__':
    while True:
        msg = input("请输入贴吧名:")
        if msg == 'exit':
            break
        head = int(input('请输入开始页码:'))
        end = int(input('请输入结束页码:'))
        for i in range(head,(end+1)):
            tieba(msg,i)