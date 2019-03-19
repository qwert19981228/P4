from mydb import Mydb
import requests
class Pro():
    def __init__(self):
        self.db = Mydb('127.0.0.1','root','123456','p4')
        sql = 'select * from proxy'
        # 获取数据
        self.res = self.db.query(sql)

    # 发送请求 并过滤
    def send(self):
        base_url = 'http://www.baidu.com'
        for i in self.res:
            # 组装数据
            proxy = {
                'http':'http://' + str(i['ip']) + ':' + str(i['port'])
            }

            try:
                response = requests.get(url=base_url,proxies=proxy,timeout=3)
            except:
                print('代理不可用删除库中的数据',i)
                self.del_ip(i)
            else:
                if not 200 == response.status_code :
                    self.del_ip(i)
                    print('不可用',i)

    def del_ip(self,host):
        sql = 'delete from proxy where id=%s'%host['id']
        self.db.execute(sql)

# 判断是否能用
while True:
    data = Pro()
    data.send()