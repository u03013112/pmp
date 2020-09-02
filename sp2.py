# encoding:utf-8
import requests
from sign import Sign
import random

class SP2:
    def __init__(self,comic_id,chapter_id):
        # print('爬取一本书内容的类')
        self.url = 'http://j.jinkongjianshe.com/api/comic/read_chapter?comic_id=%d&chapter_id=%d' % (comic_id,chapter_id)
        self.ua = 'baipiaoshiwokuaile'
    def sp(self):
        for retry in range(10):
            try:
                headers = {'User-Agent': self.ua}
                r = requests.get(self.url,headers=headers)
                data = r.json()['data']
                canRead = data['can_read']
                if canRead != True:
                    Sign(self.randomUA()).sp()
                    continue
                # print(data)
                self.data = data
                return data
            except Exception as e:
                print(e)
        return None
        
    def randomUA(self):
        self.ua = str(random.random())
        return self.ua

if __name__=='__main__':  
    s = SP2(234,8420)
    print(s.sp())