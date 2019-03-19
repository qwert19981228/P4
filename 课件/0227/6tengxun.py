import requests
from bs4 import BeautifulSoup
import time

base_url = 'https://hr.tencent.com/position.php?&start=%d'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36"
}

def getinfo():
    for i in range(0,201,10):
        new_url = base_url % i

        response = requests.get(new_url,headers=headers)

        html = BeautifulSoup(response.text,'lxml')
        tr_list = html.select('table.tablelist tr')[1:-1]
        for tr in tr_list:
            td_list = tr.select('td')
            job_name = td_list[0].a.text
            job_type = td_list[1].text
            job_num = td_list[2].text
            print(job_name,job_type,job_num)

if __name__ == '__main__':
    start = time.time()
    getinfo()
    end = time.time()-start
    print(end)
