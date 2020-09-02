# encoding:utf-8
import requests

class SP0:
    def __init__(self):
        # print('爬取目录的类')
        self.url = 'http://j.jinkongjianshe.com/api/comic/rank?page=1&limit=1000&sort=popularity'
    def sp(self):
        for retry in range(10):
            try:
                r = requests.get(self.url)
                data = r.json()['data']['data']
                # print(data)
                self.data = data
                return data
            except Exception as e:
                print(e)
        return None

if __name__=='__main__':  
    s = SP0()
    s.sp()