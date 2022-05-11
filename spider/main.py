from sp0 import SP0
from sp1 import SP1

import os
import requests

# 需要爬的名字写在这
name = 'r402'

if __name__ == '__main__':
    # 建立目录
    path='/src/spider/downloads/'+name
    if not os.path.exists(path):
        os.makedirs(path)
    chapters = SP0(name).sp()
    for chapter in chapters:
        # 为每一章建立一个目录
        path='/src/spider/downloads/'+name+'/'+chapter['title']
        if not os.path.exists(path):
            os.makedirs(path)
        pics = SP1(chapter['url']).sp()
        for i in range(len(pics)):
            filename = path + '/' + str(i) + '.jpg'
            response = requests.get(pics[i],verify=False)
            with open(filename,'wb') as f:
                for data in response.iter_content(1024):
                    f.write(data)

        