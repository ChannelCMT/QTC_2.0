#-*-coding:utf-8-*-
# from lxml import etree

# import json
# import requests
# import itchat
# import random
# import json
# url="http://www.tuling123.com/openapi/api"
# APIKEY="dbafb0a6c63f42c88440842716fb9d69"
# def get_response(msg):
#     apiUrl = 'http://www.tuling123.com/openapi/api'
#     data = {
#         'key': APIKEY,
#         'info': msg,
#         'userid': 'wechat-robot',
#     }
#     try:
#         r = requests.post(apiUrl, data=data).json()
#         return r.get('text')
#     except:
#         return
# # @itchat.msg_register(itchat.content.PICTURE)
# # def return_picture(msg):
# #     r=requests.get("https://img02.sogoucdn.com/app/a/100520021/D8A980A5483F32EBF8CB122C0E1F55F1")
# #     with open("1.png","wb") as f:
# #         f.write(r.content)
# #     itchat.send_image("1.png", toUserName=msg['FromUserName'])
# #     return None
# # itchat.auto_login()
# # itchat.run()
# def get_random_picture():
#     r=requests.get("https://pic.sogou.com/pic/emo/groupDetail.jsp?id=3558&from=emo_classify_title")
#     r=etree.HTML(r.text)
#     img=r.xpath("*//img")
#     length=img.__len__()
#     flag=True
#     while flag:
#         a = random.randint(1, length)
#         ran_img_href=r.xpath("*//img[%d]/@rsrc"%(a))
#         href_length=len(ran_img_href)
#         if href_length >0:
#             b=random.randint(1,href_length)
#             flag=False
#             # print(ran_img_href[b])
#             ran_img=requests.get(ran_img_href[b]).content
#             return ran_img
# def search(question):
#     url = "https://www.baidu.com/s?wd=%s" % (question)
#     headers = {"Host": "sp0.baidu.com",
#                "Cookie": "BDUSS=sxfjBQZ2RDbjFjQ25NYU5VajVjc35QR21WVjhSSlc5RS1reXNBUkljSnoxM1phQVFBQUFBJCQAAAAAAAAAAAEAAAD5cRGevsbX7cjLsrvX1NftAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHNKT1pzSk9aQW; BAIDUID=3F50035AAA689B4F646729842B13E216:FG=1; BIDUPSID=9F12AB144CF4A5003F269F5A2545A028; PSTM=1515328250; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=1430_21126_17001_20719; PSINO=7",
#                "Cache-Control": "no-cache", "Accept": "*/*",
#                "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
#                "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:57.0) Gecko/20100101 Firefox/57.0",
#                "Pragma": "no-cache", "Accept-Encoding": "gzip, deflate, br", "Connection": "keep-alive"}
#     r = requests.get(url, headers=headers)
#     r.encoding = "utf-8"
#     bsObj = BeautifulSoup(r.text, "lxml")
#
#     bsObjs = bsObj.findAll("div", {"id": "content_left"})[0].findAll("a")
#     i = 0
#     result = ""
#     for bsObj in bsObjs:
#         try:
#             if question.encode("utf-8") in bsObj.text.encode("utf-8"):
#                 result += bsObj.text + " " + bsObj["href"]
#                 i = i + 1
#             if i >= 10:
#                 break
#         except Exception as e:
#             continue
#     return result
# import re
# compile2=re.compile("search(.*)")
# print(seek.group(1))
# proxy={
#     "http":"http://2016124941:260038@203.110.166.130:443",
#     "https":"http://2016124941:260038@203.110.166.130:443"
# }
# import requests
# r=requests.get("http://library.lixin.edu.cn",proxies=proxy)

# print(r.text)
# import requests
# try:
#     r = requests.get("http://newjw.lixin.edu.cn/sso/login?local=1")
# except requests.Timeout:
#     print(1)
import datetime
import requests
from bs4 import BeautifulSoup

# def grade(account, passwd):
#     current_hour = int(datetime.datetime.now().strftime("%H"))
#     if current_hour >= 22 or current_hour < 8:
#     try:
#         r = requests.get("http://newjw.lixin.edu.cn/sso/login?local=1",timeout=3)
#     except requests.Timeout:
#     i = 0
#     while i < 5:
#         i = i + 1
#         try:
#             Session = requests.session()
#             r = Session.post("http://newjw.lixin.edu.cn/sso/login", data={"username": account, "password": passwd},timeout=3)
#             print(r)
#             print(list(r.cookies))
# r = Session.get("http://newjw.lixin.edu.cn/home/",timeout=3)
# print(r.text)
# r.encoding = "utf-8"
# print(r.text)
# print(r.text)
# r = Session.get("http://newjw.lixin.edu.cn/webapp/std/edu/grade/",timeout=3)
# r = Session.get("http://newjw.lixin.edu.cn/webapp/std/edu/grade/home.action",timeout=3)
# r = Session.get(
#     "http://newjw.lixin.edu.cn/sso/login?service=http://newjw.lixin.edu.cn/webapp/std/edu/grade/home.action",timeout=3)
#
# print(r.text)
# r = Session.get("http://newjw.lixin.edu.cn/webapp/std/edu/grade/home!childmenus.action?menu.id=323",timeout=3)
# r = Session.get("http://newjw.lixin.edu.cn/webapp/std/edu/grade/course!innerIndex.action?projectId=5",timeout=3)
# print(r.cookies["JSESSIONID"])
# print(r.text)
# print(list(r.cookies))
# "ST-131629-JaDjjxigGjBCCa9buBadFPtgcGIXuKnbla2769964"
# r=Session.get("http://newjw.lixin.edu.cn/webapp/std/edu/grade/course!innerIndex.action;jsessionid=DC3DD0FA50EEC92513388D9273017CB0?ticket=ST-130155-g3gBgd9jGHktSOWbg5BjA5BbaY1Rr1wfmWv653845")
# bsObj = BeautifulSoup(r.text, "lxml")
# bsObj = bsObj.findAll("table")[2].findAll("tbody")[0].findAll("tr")
# result = ""
# for trs in bsObj:
#     course = trs.findAll("td")[2].text
#     result += course + " "
#     score = trs.findAll("td")[-2].text
#     result += score + "\n"
# with open("1.txt") as f:
#     f.write(result)
# return result
# except requests.Timeout:
# except Exception as e:
#     continue
# else:
# print(grade("2016142115","270029"))
# Session = requests.session()
# r = Session.post(
#     "http://sso.lixin.edu.cn/authorize.php?client_id=ufsso_longmeng_portal_index&redirect_uri=http%3A%2F%2Fsso.lixin.edu.cn%2Findex.html&response_type=token&state=1q2w3e",
#     data={"username": "2016124941", "password": "l1o2V3E4"})
# r = Session.get("http://ldap.lixin.edu.cn/index.html")
# r = Session.post("http://ldap.lixin.edu.cn/server/ChangePassword.php",
#                  data={"pass": "w1y2s3E4S5T6", "pass-cfrm": "w1y2s3E4S5T6", "ext-gen1065": ""})
# r = Session.get("http://ldap.lixin.edu.cn/server/Login.php?service=logoff&logoffsso=1")
# r = Session.get(
#     "http://sso.lixin.edu.cn/logout.php?access_token=a6a4aa1c73158b290df5d0d8a829c2d0&redirect_uri=http://ldap.lixin.edu.cn/server/Login.php")
# r = Session.get("http://ldap.lixin.edu.cn/server/Login.php?success=1")
#
# r.encoding = "utf-8"
# print(r.text)
#

import requests
from bs4 import BeautifulSoup
def translation(query):
    r=requests.get("https://translate.google.cn/#en/zh-CN/%s"%(query))
    r.encoding="GB2312"
    bsObj=BeautifulSoup(r.text,"lxml")
    bsObj=bsObj.findAll("div",{"id":"result_box"})[0]

    js="""var tx = function (a, b, c) {
	var d = COMMUNITY_CARD_TASK_TYPE, e = COMMUNITY_CARD_EXPANDED;
	this.a = b;
	this.m = c;
	this.o = this.j = "";
	this.B = d;
	this.g = new hx;
	this.b = new mx(a, z(this.c, this));
	px(this.b, e)
}, wx = function (a) {
	var b = ux(a.a);
	a = vx(a.a);
	return b == Lb && "es" == a || "es" == b && a == Lb ? !0 : !1
};
tx.prototype.reset = function () {
	this.m();
	px(this.b, !0)
};
tx.prototype.setVisible = function (a) {
	a ? (a = this.j != ux(this.a) || this.o != vx(this.a), this.b.setVisible(!0), a && this.c()) : (this.g.abort(), this.b.setVisible(!1))
};
tx.prototype.c = function () {
	var a = ux(this.a), b = vx(this.a), c = this.g, d = this.B, e = z(this.v, this, a, b);
	a = "/community_v2/as?client=t" + ix() + "&sl=" + a + "&tl=" + b + "&surt=" + d;
	(b = qp(new cp(window.location.href, !0), "e")) && (a += "&e=" + b);
	c.$ && c.$.abort();
	c.$ = Mm(a, z(c.b, c, e), Ka, c.a ? c.a.toString() : void 0)
};
tx.prototype.v = function (a, b, c) {
	if (c) {
		this.j = a;
		this.o = b;
		var d = this.a.J(a), e = this.a.Ua(b), f = this.b;
		f.c = c;
		f.b = 0;
		!f.c.activities || f.b >= f.c.activities.length ? vl(f.C) : (f.m = a, f.v = b, f.A = d, f.G = e, f.g = f.c.metadata.evaluation_type, a = {}, a.expanded = f.j ? "1" : "0", f.c.error && (a.error = f.c.error.error_type), Ro(f.F, "t", xb, "update", a), f.j ? nx(f) : ox(f))
	}
};
    """
    print bsObj.prettify()
translation(u"Excellent strategic communication, which is what Discovery excels at, isn’t always backed up by excellent information. If you think that this doesn’t have harmful consequences, think again. According to the Pew Research Center, 33 percent of U.S. adults are incorrectly convinced that “humans existed in present form since the beginning of time.”Alberto Cairo. The Truthful Art: Data, Charts, and Maps for Communication (Kindle 位置 499-501). Pearson Education. Kindle 版本. ".encode("utf-8"))
