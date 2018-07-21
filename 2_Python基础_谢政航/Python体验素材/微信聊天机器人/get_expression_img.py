# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import json
import requests
from lxml import etree
import re
#f=open("serverList.xlsx")
#files={"field1":("service.xlsx",f)}
#for i in range(4):
#    r=requests.post("http://iguihuo.com/server/upload.html",data=files)
import random
#获得第一面和第n面的表情包
def get_img_href(n):
    data={'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
    a=input()
    url="https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1511601652481_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word={0}".format(a)
    session=requests.Session()
    r=session.get(url,headers=data)
    compiler=re.compile("\"thumbURL\":\"(https://(.|\n)*?\.jpg)\"")
    urls=re.findall(compiler,r.text)
    url_list=[]
    for url in urls:
        url_list.append(url[0].replace('\n',''))
    # def get_next_url(url,session,pn='30',gsm='3c'):
    #     url_temp=url.format(pn,gsm)
    #     r=session.get(url_temp)
    #     receive=json.loads(r.text)
    #     gsm=receive['gsm']
    #     pn=str(int(pn)+30)
    #     return url.format(pn,gsm),pn,gsm


    url= "https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=表情包&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word=表情包&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&pn={0}&rn=30&gsm={1}&1511624511221="
    gsm='3c'
    pn='30'
    def get_page(n):
        for i in range(n):
            try:
                r=session.get(url.format(pn,gsm))
                receive=json.loads(r.text)
                datas=receive['data']
                gsm=receive['gsm']
                pn=str(int(pn)+30)
                for data in datas:
                    url_list.append(data["thumbURL"])
            except:
                continue
    get_page(n)
    return url_list

# i=0
# for url in url_list:
    # i+=1
    # r=requests.get(url)
    # with open(str(i)+'.jpg',"wb") as f:
    #     f.write(r.content)
#response=etree.HTML(r.text)
#response=response.xpath("*/div[@id='imgid']")
#print(response)
#print("1234")
#imgs=response.xpath('.//li')
#length=len(imgs)
#random_length=random.randint(0,length)
#random_img_url=response.xpath('./div/li[%d]/div/ul/a/img/@data-imgurl'%(random_length))
#r=requests.get(random_img_url)
#with open("1.jpg","wb") as f:
#    f.write(r.content)