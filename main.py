# encoding:utf-8
import os, sys

from sp0 import SP0
from sp1 import SP1
from sp2 import SP2

# 由于爬虫实在太费时间，简单的先写个下载脚本
if __name__=='__main__':
    prefix = 'http://ac.wet8955.cn'
    root = 'script'

    try:
        os.makedirs(root)
    except OSError as e:        
        pass
    
    menu0 = SP0().sp()

    for menu1 in menu0:
        dir0 = menu1['name']
        filename = "%s/%s.sh" % (root,dir0)
        fo = open(filename, "w",encoding='utf-8')
        fo.write( "#!/bin/sh\n")
        fo.write( "mkdir -p %s\n" % dir0 )
        fo.write( "curl -o %s/cover.jpg %s/%s\n" % (dir0,prefix,menu1['cover']))
        id = menu1['id']
        menu2 = SP1(id).sp()
        for chapter in menu2:
            dir1 = chapter['name']
            fo.write( "mkdir -p %s/%s\n" % (dir0,dir1) )
            fo.write( "curl -o %s/%s/cover.jpg %s/%s\n" % (dir0,dir1,prefix,chapter['cover']))
            comic_id = chapter['comic_id']
            chapter_id = chapter['chapter_id']
            data = SP2(comic_id,chapter_id).sp()
            images = data['images']
            for i in range(len(images)):
                fo.write( "curl -o %s/%s/%d.jpg %s/%s\n" % (dir0,dir1,i,prefix,images[i]))
            print(dir0,dir1,'ok')
        fo.close()
