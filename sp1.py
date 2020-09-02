# encoding:utf-8
import requests

class SP1:
    def __init__(self,comic_id):
        # print('爬取一本书目录的类')
        self.url = 'http://j.jinkongjianshe.com/api/comic/comic_detail/?comic_id=%d'%(comic_id)
    def sp(self):
        for retry in range(10):
            try:
                r = requests.get(self.url)
                data = r.json()['data']['chapter_list']
                # print(data)
                self.data = data
                return data
            except Exception as e:
                print(e)
        return None

if __name__=='__main__':  
    s = SP1(234)
    print(s.sp())