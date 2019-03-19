import pymysql

class Mydb:
    def __init__(self,host='127.0.0.1',user='root',port=3306,password=None,database=None):
        try:
            self.db = pymysql.connect(host=host,user=user,password=password,port=port,database=database,cursorclass=pymysql.cursors.DictCursor)
            self.cursor=self.db.cursor()
        except:
            print('连接失败')

    # 查询
    def query(self,sql):
        try:
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            return res
        except:
            print('查询失败',sql)
    # 操作
    def excute(self,sql):
        # try:
        res = self.cursor.execute(sql)
        self.db.commit()
        return res
        # except:
        #     print('操作失败', sql)

    def __del__(self):
        self.db.close()
