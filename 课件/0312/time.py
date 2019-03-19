import datetime
from datetime import timedelta
def process_date(self ,value):

    if '天前' in value:
        res = self.num_pattern.search(value).group()
        date_pub = (datetime.datetime.now() - timedelta(days=int(res))).strftime('%Y-%m-%d')
    else:
        date_pub = datetime.datetime.now().strftime('%Y-%m-%d')
    return date_pub
# print(datetime.datetime.now() - timedelta(days=3))

