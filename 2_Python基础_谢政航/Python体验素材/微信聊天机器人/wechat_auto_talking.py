import itchat
import requests
import json
import random
from lxml import etree
#from voice_return import return_vedio
from get_expression_img import get_img_href
url="http://www.tuling123.com/openapi/api"
APIKEY="aff4d1e9138d4ec99251a36e074d9cb0"
#获得随机表情包的链接
def get_random_picture_url():
    headers = {"Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
               "Upgrade-Insecure-Requests": "1",
               "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:57.0) Gecko/20100101 Firefox/57.0",
               "Connection": "keep-alive",
               "Cookie": "IPLOC=CN3100; SUV=00A74931B4A0DB6659C75BA6E1AB0304; CXID=C59AE49D0DE0EBEFCDE6D2A031794450; ad=xZllllllll2BiZ@8lllllVoJ7D1lllllH3j1WZllll9lllllRqxlw@@@@@@@@@@@; SUID=5FB3A6B73865860A59B4BB840004E7DF; wuid=AAHUO2QdHAAAAAqLFD2awQIAGwY=; JSESSIONID=aaaTWsodqyAt4ewiDAP-v; ABTEST=1|1511528360|v1",
               "Host": "pic.sogou.com", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
               "Accept-Encoding": "gzip, deflate, br"}
    cookies = {"IPLOC": "CN3100", "ABTEST": "1|1511528360|v1", "CXID": "C59AE49D0DE0EBEFCDE6D2A031794450",
               "wuid": "AAHUO2QdHAAAAAqLFD2awQIAGwY=", "SUV": "00A74931B4A0DB6659C75BA6E1AB0304",
               "ad": "xZllllllll2BiZ@8lllllVoJ7D1lllllH3j1WZllll9lllllRqxlw@@@@@@@@@@@",
               "JSESSIONID": "aaaTWsodqyAt4ewiDAP-v", "SUID": "5FB3A6B73865860A59B4BB840004E7DF"}
    r = requests.get("https://pic.sogou.com/pic/emo/groupDetail.jsp?id=3558&from=emo_classify_title", headers=headers,
                     cookies=cookies)
    r=etree.HTML(r.text)
    img=r.xpath("*//img")
    length=img.__len__()
    flag=True
    while flag:
        a = random.randint(1, length)
        ran_img_href=r.xpath("*//img[%d]/@rsrc"%(a))
        href_length=len(ran_img_href)
        if href_length >0:
            b=random.randint(1,href_length)
            flag=False
            # print(ran_img_href[b])
            return ran_img_href[b]
#获得图灵机器人的智能回复
def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key': APIKEY,
        'info': msg,
        'userid': 'wechat-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        return r.get('text')
    except:
        return
#获得该用户机器人的使用状态
def loading(filename,flag1):
    with open(filename, "r") as f:
        flag = json.load(f)
        flag["status"] = flag1
    with open(filename, "w") as f:
        json.dump(flag, f)
name_list=[]
#回复文字
@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    if msg["User"]["NickName"] in name_list:
        index = str(name_list.index(msg["User"]["NickName"]))
        if msg['Text']=="启动":
            loading(index+".json",True)
        if msg['Text']=="关闭":
            loading(index+".json",False)
        if msg["Text"]=="移除":
            name_list.remove(msg["User"]["NickName"])
            return None
        with open(index+".json","r") as f:
            flag=json.load(f)
            if flag["status"]:
                defaultReply = 'I received: ' + msg['Text']
                reply = get_response(msg['Text'])
                return reply or defaultReply
    elif msg["Text"]=="加入" :
            name_list.append(msg["User"]["NickName"])
            index=str(name_list.index(msg["User"]["NickName"]))
            with open(index+".json","w") as f:
                dictation={"status":False}
                json.dump(dictation,f)
#回复图片
@itchat.msg_register(itchat.content.PICTURE)
def return_picture(msg):
    # r=requests.get("https://img02.sogoucdn.com/app/a/100520021/D8A980A5483F32EBF8CB122C0E1F55F1")
    # itchat.send_image("%s"%(r.content), toUserName=msg['FromUserName'])
    if msg["User"]["NickName"] in name_list:
        index = str(name_list.index(msg["User"]["NickName"]))
        with open(index + ".json", "r") as f:
            flag = json.load(f)
            if flag["status"]:
                # random_picture_url=get_random_picture_url()
                # r=requests.get(random_picture_url)
                url_list=get_img_href(5)
                random_url=url_list[random.randint(0,len(url_list)-1)]
                r=requests.get(random_url)
                with open("1.jpg","wb") as f:
                    f.write(r.content)
                itchat.send_image("1.jpg",toUserName=msg['FromUserName'])
                return None
#回复语音
@itchat.msg_register(itchat.content.VOICE)
def get_voice(msg):
    if msg["User"]["NickName"] in name_list:
        index = str(name_list.index(msg["User"]["NickName"]))
        with open(index + ".json", "r") as f:
            flag = json.load(f)
            if flag["status"]:
                f1=msg['Text']
                content=f1()
                with open("1.mp3","wb") as f_voice:
                    f_voice.write(content)
                text=return_vedio()
                return get_response(text)
itchat.auto_login(enableCmdQR=True)
itchat.run()
