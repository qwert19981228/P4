from multiprocessing import Pool,Manager
import requests,time
from lxml import etree
from urllib import request

headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
}

def tu(url,q):
    url1=url+'/'
    print('开始%s!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'%url1)
    res=requests.get(url1,headers=headers)
    ser=res.text
    print(res.status_code)
    if res.status_code==200:
        html=etree.HTML(ser)
        vga=html.xpath('//div[@class="postlist"]//li/a/img/@data-original')
        print(vga)
        for i in vga:
            q.put(i)
            print(i,'1111')
            tuname=i.split('/')[-1]
            header = {
                "referer": "https://www.mzitu.com/xinggan/",
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36"
            }
            # request.urlretrieve(i,'./meizi/'+tuname)
            img = requests.get(i,headers=header)
            print(img.status_code)
            with open('./text','w',encoding='utf-8') as f:
                f.write('111')

    else:
        print('出错')
    print('结束%s!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'%url1)

if __name__ == '__main__':
    start=time.time()
    #建立进程池
    po=Pool(1)
    #创建Queue
    q=Manager().Queue()
    base_url='https://www.mzitu.com/page/%d'
    new_url=[base_url%i for i in range(1,3)]

    for url in new_url:
        po.apply_async(func=tu,args=(url,q))
    po.close()
    po.join()
    while not q.empty():
        # print(q.get())
        q.get()
    end=time.time()-start
    print('花费时间%s'%end)
