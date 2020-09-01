# encoding:utf-8
import requests

class SP0:
    def __init__(self):
        print('爬取目录的类')
        # 一下拿1000个，爬完再说
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