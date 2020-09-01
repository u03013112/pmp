# encoding:utf-8
import requests

class SP2:
    def __init__(self,comic_id,chapter_id):
        print('爬取一本书内容的类')
        self.url = 'http://j.jinkongjianshe.com/api/comic/read_chapter?comic_id=%d&chapter_id=%d' % (comic_id,chapter_id)
    def sp(self):
        try:
            r = requests.get(self.url)
            data = r.json()['data']['images']
            # print(data)
            self.data = data
            return data
        except requests.exceptions.RequestException as e:
            print(e)

if __name__=='__main__':  
    s = SP2(234,8415)
    s.sp()