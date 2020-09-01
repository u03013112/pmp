# encoding:utf-8
import requests

class SP1:
    def __init__(self):
        print('爬取一本书目录的类')
        self.url = 'http://j.jinkongjianshe.com/api/comic/rank?page=1&limit=1000&sort=popularity'
    def sp(self):
        try:
            r = requests.get(self.url)
            data = r.json()['data']['data']
            # print(data)
            self.data = data
            return data
        except requests.exceptions.RequestException as e:
            print(e)

if __name__=='__main__':  
    s = SP0()
    s.sp()