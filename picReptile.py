#-*-coding:utf8-*-
#下载get-pip.py后执行下面两行命令，出错的话sudo
#python get-pip.py
#pip install requests

#导入re 和requests库
import re
import requests

#获取网页的源代码
html = requests.get('http://www.vip.com/1208?tagId=dress&f=nav_right_31').text

#网页源码中  "new_brand_image":"http:\/\/c.vpimg1.com\/upcb\/2015\/11\/26\/85\/23083556.jpg"

#查找所有的图片地址，将其保存在pic_url中，'"pic" src="(.*?)"'表示我们查找的图片地址在代码中前面是"new_brand_image":"，后面是"
pic_url = re.findall('"new_brand_image":"(.*?)"',html,re.S)

i = 0 
for each in pic_url:
    url =   each
    reobj = re.compile("\\\/");
    res = reobj.sub("/",url);
    print('now downloading:' + res)
    #从url图片地址下载到pic中
    pic = requests.get(res)
    #将下载得到的pic图片内容写到文件中，并将其保存在pic文件夹中
    fp = open('pic//' + str(i) + '.jpg','wb')
    fp.write(pic.content)
    fp.close()
    i += 1
