# encoding:utf-8
import requests

class Sign:
    def __init__(self,ua):
        # print('爬取签到的类')
        self.url = 'http://j.jinkongjianshe.com/api/user/sign_in'
        self.ua = ua
    def sp(self):
        try:
            headers = {'User-Agent': self.ua}
            r = requests.post(self.url,headers=headers,timeout=10)
            # data = r.json()['code']
            # data = r.text
            # print(data)
            # self.data = data
            # return data
        except Exception as e:
            print(e)

if __name__=='__main__':  
    s = Sign("1a")
    s.sp()