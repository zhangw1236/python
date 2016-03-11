# -*- coding:utf-8 -*-
import urllib2
import urllib
import re
import sys
import os
import cookielib

class TaobaoMM:
    #初始化方法
    def __init__(self, pageIndex, dir):
        #登录的URL
        self.loginURL = "https://login.taobao.com/member/login.jhtml"
        #代理IP地址，防止自己的IP被封禁
        self.proxyURL = 'http://120.193.146.97:843'
        #登录POST数据时发送的头部信息
        self.loginHeaders =  {
            'Host':'login.taobao.com',
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
            'Referer' : 'https://login.taobao.com/member/login.jhtml',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Connection' : 'Keep-Alive'
        }
        #用户名
        self.username = '13917928362'
        #ua字符串，经过淘宝ua算法计算得出，包含了时间戳,浏览器,屏幕分辨率,随机数,鼠标移动,鼠标点击,其实还有键盘输入记录,鼠标移动的记录、点击的记录等等的信息
        self.ua = '013#JxEAUAAjA9EAAAAAANefAAYBABnDwsHAv4RKHUwHWShGNkYyXi9KFiRTM0EzBgEAGcPCwcC/h3wvfjFvHnwIdARsGXwkEmEBcwEGAQAZw8LBwL+Hs+a1+KjXt8W3wa/cv+HRoP6O/gYBABnDwsHAv4a057b5p9a0wMy81KHEnKrZucu5BgEAGcPCwcC/iDptPHcpWDZGNkIuXzpmVCNDMUMGAQAZw8LBwL+KUwZVGEg3VyVXIU88XwExQF4uXgYBABnDwsHAv4qn8qHstMOj0aPVu8ij/c282qraBgEAGcPCwcC/jSdyIWw0QyNRI1U7SCN9TTxaKloGAQAZw8LBwL+MWg1cF0k4ViZWIk4/WgY0QyNRIxYBAATNzMvKBgEAGcPCwcC/jMaRwPOt3LrKus6i07bq2KfHtccGAQAZw8LBwL+PMHsqZTtKKFQgaAh1EFB+DW0fbRYBAATNzMvKBAEAD8vKIB4A//7tndaKz6HSvAQBAAnNzf78zs3M2/EEAQAPy8uOjLe2taSu57n+kuOPAwEAKM3My8rJyMfGxcTCjo2MiUpJSEEA//7+eXh3cC8uLS9ycXBvbm1sa2oTAQAMz87JyMDLo82igaiODAEAN/vL/sjw2u7V4dbg6tjn3L6I49vsiLKBsJ6ryf/HpcCPv4mx1OKD5tbi0une5NWwzanJ/s6syv4XAQAEzczKyRQBAAbNzY2SGMsBAQAIzczKmse1VFwCAQAGz87Pz/rBCwEAws2Tks6l0LvKuoOtg+6C5ozlyr3ds9Cuwu+N44+hzanFpsDN447ihuyFqsOq3bHc5JH1kOaX85HktueqlPuO+Yj01ufT4aGFtoBNCiwZLR5bLVstAnUVexh2GjdVO1dzQAo7fBNmEWAsET8RfBR0GndYI0MtTixEbQ9hDSNPK0ckRjcZdBx8En9QJUw/Uz4CcxdyGGUBYxZAbSAiSTxPPk5oVWFTEzcENgdAGisfLG0bbRs0RydJKkgoCWsFaU1+SHUyFgEABM3My8oNAQAbx8bLnfWa/ZPll7aEs+Wt4sHywJOijbyXp56vBAEAD8vLwcHo5+b1p+y09ZvoigQBAA/LygMDFhUUA43Gmt+xwqwFAQAaw8Kko1ZVVFNScr696Lf6ptW1x7XDrd6559cHAQAUw8PCweMEVwZJF2YEcBxsBHEUTHoGAQAZw8LBwL+PnM+e0Y/+nOiU5Iz5nMTygeGT4RYBAATNzMvKFgEABM3My8oGAQAZw8LBwL+L47blqPiH55Xnkf+M77GB8I7+jgYBABnDwsHAv4mz5rX4qNe3xbfBr9y/4dGg/o7+'
        #密码，在这里不能输入真实密码，淘宝对此密码进行了加密处理，256位，此处为加密后的密码
        self.password2 = '6da4bcde181b7cf6aa602bbee04c4e23d08d0412b74c25ba2e471e70a425256bf94247eff207d4443c7421855df93756c18bec0ee439e660f9187bf7aa23d9fede7cf8f5e62e730254ce2577a431c6005ed8dd85be1a0e80bbc0f20af2b70d3ac5858ad3839e3b5906efbeac37b16b3dc7d0bf9482872c99a621bf1fda0f7883'
        self.post = post = {
            'ua':self.ua,
            'TPL_checkcode':'',
            'CtrlVersion': '1,0,0,7',
            'TPL_password':'',
            'TPL_redirect_url':'http://i.taobao.com/my_taobao.htm?nekot=udm8087E1424147022443',
            'TPL_username':self.username,
            'loginsite':'0',
            'newlogin':'0',
            'from':'tb',
            'fc':'default',
            'style':'default',
            'css_style':'',
            'tid':'XOR_1_000000000000000000000000000000_625C4720470A0A050976770A',
            'support':'000001',
            'loginType':'4',
            'minititle':'',
            'minipara':'',
            'umto':'NaN',
            'pstrong':'3',
            'llnick':'',
            'sign':'',
            'need_sign':'',
            'isIgnore':'',
            'full_redirect':'',
            'popid':'',
            'callback':'',
            'guf':'',
            'not_duplite_str':'',
            'need_user_id':'',
            'poy':'',
            'gvfdcname':'10',
            'gvfdcre':'',
            'from_encoding ':'',
            'sub':'',
            'TPL_password_2':self.password2,
            'loginASR':'1',
            'loginASRSuc':'1',
            'allp':'',
            'oslanguage':'zh-CN',
            'sr':'1366*768',
            'osVer':'windows|6.1',
            'naviVer':'firefox|35'
        }
        #将POST的数据进行编码转换
        self.postData = urllib.urlencode(self.post)
        #设置代理
        self.proxy = urllib2.ProxyHandler({'http':self.proxyURL})
        #设置cookie
        self.cookie = cookielib.LWPCookieJar()
        #设置cookie处理器
        self.cookieHandler = urllib2.HTTPCookieProcessor(self.cookie)
        #设置登录时用到的opener，它的open方法相当于urllib2.urlopen
        self.opener = urllib2.build_opener(self.cookieHandler,self.proxy,urllib2.HTTPHandler)
        
        #登录成功时，需要新的Cookie
        self.newCookie = cookielib.CookieJar()
        #登陆成功时，需要的一个新的opener
        self.newOpener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.newCookie))
 
        self.url = 'http://mm.taobao.com/json/request_top_list.htm'
        self.pageIndex = pageIndex
        self.resultDir = dir
        
    #得到是否需要输入验证码，这次请求的相应有时会不同，有时需要验证有时不需要
    def needIdenCode(self):
        #第一次登录获取验证码尝试，构建request
        request = urllib2.Request(self.loginURL,self.postData,self.loginHeaders)
        #得到第一次登录尝试的相应
        response = self.opener.open(request)
        #获取其中的内容
        content = response.read().decode('gbk')
        #获取状态吗
        status = response.getcode()
        #状态码为200，获取成功
        if status == 200:
            print u"获取请求成功"
            #\u8bf7\u8f93\u5165\u9a8c\u8bc1\u7801这六个字是请输入验证码的utf-8编码
            pattern = re.compile(u'\u8bf7\u8f93\u5165\u9a8c\u8bc1\u7801',re.S)
            result = re.search(pattern, content)
            #如果找到该字符，代表需要输入验证码
            if result:
                print u"此次安全验证异常，您需要输入验证码"
                return content
            #否则不需要
            else:
                tokenPattern = re.compile('id="J_HToken" value="(.*?)"')
                tokenMatch = re.search(tokenPattern, content)
                if tokenMatch:
                    self.J_HToken = tokenMatch.group(1)
                    print u"此次安全验证通过，您这次不需要输入验证码"
                    print 'token is: ', self.J_HToken
                    return False
        else:
            print u"获取请求失败"
 
    #得到验证码图片
    def getIdenCode(self,page):
        #得到验证码的图片
        pattern = re.compile('<img id="J_StandardCode_m.*?data-src="(.*?)"',re.S)
        #匹配的结果
        matchResult = re.search(pattern,page)
        #已经匹配得到内容，并且验证码图片链接不为空
        if matchResult and matchResult.group(1):
            print matchResult.group(1)
            return matchResult.group(1)
        else:
            print u"没有找到验证码内容"
            return False
 
    def getSTbyToken(self, token):
        tokenURL = 'https://passport.alipay.com/mini_apply_st.js?site=0&token=%s&callback=stCallback6' % token
        request = urllib2.Request(tokenURL)
        response = urllib2.urlopen(request)
        #处理st，获得用户淘宝主页的登录地址
        pattern = re.compile('{"st":"(.*?)"}',re.S)
        result = re.search(pattern,response.read())
        #如果成功匹配
        if result:
            print u"成功获取st码"
            #获取st的值
            st = result.group(1)
            return st
        else:
            print u"未匹配到st"
            return False
    
    def doLogin(self, st):
        stURL = 'https://login.taobao.com/member/vst.htm?st=%s&TPL_username=%s' % (st, self.username)
        headers = {
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
            'Host':'login.taobao.com',
            'Connection' : 'Keep-Alive'
        }
        request = urllib2.Request(stURL, headers = headers)
        response = self.newOpener.open(request)
        content =  response.read().decode('gbk')
        #print content
        #检测结果，看是否登录成功
        pattern = re.compile('top.location.href = "(.*?)"',re.S)
        match = re.search(pattern,content)
        if match:
            print u"登录网址成功"
            location = match.group(1)
            return True
        else:
            print "登录失败"
            return False
        
    #登录
    def login(self):
        #是否需要验证码，是则得到页面内容，不是则返回False
        needResult = self.needIdenCode()
        if not needResult == False:
            print u"您需要手动输入验证码"
            idenCode = self.getIdenCode(needResult)
            #得到了验证码的链接
            if not idenCode == False:
                print u"验证码获取成功"
                print u"请在浏览器中输入您看到的验证码"
                webbrowser.open_new_tab(idenCode)
            #验证码链接为空，无效验证码
            else:
                print u"验证码获取失败，请重试"
        else:
            print u"不需要输入验证码"
 
        st = self.getSTbyToken(self.J_HToken)
        
        if not st == False:
            print 'st is: ', st
            self.doLogin(st)
            '''
            for item in self.newCookie:
                print 'Name = '+item.name
                print 'Value = '+item.value
            '''
            
    def getPage(self):
        try:
            url = self.url + "?page=" + str(self.pageIndex)
            request = urllib2.Request(url)
            response = self.newOpener.open(request)
            self.content = response.read().decode('gbk')
        except urllib2.URLError, e:
            if hasattr(e,"code"):
                print e.code
            if hasattr(e,"reason"):
                print e.reason
    
    def getAllImg(self, page):
        pattern = re.compile('<div class="mm-aixiu-content".*?>(.*?)<!--',re.S)
        #个人信息页面所有代码
        content = re.search(pattern, page)
        #从代码中提取图片
        patternImg = re.compile('<img.*?src="(.*?)"',re.S)
        images = re.findall(patternImg, content.group(1))
        return images
    
    def getContent(self):
        pattern = re.compile('<div class="personal-info[\s\S]*?<a href="(.*?)"[\s\S]*?<a class="lady-name".*?>(.*?)</a>[\s\S]*?<strong>(.*?)</strong>[\s\S]*?<span>(.*?)</span>')
        items = re.findall(pattern, self.content)
        result = []
        for item in items:
            result.append(["https:" + item[0], item[1], item[2], item[3]])
        return result

    #传入图片地址，文件名，保存单张图片
    def saveImg(self, imageURL, fileName):
         u = urllib.urlopen(imageURL)
         data = u.read()
         f = open(fileName, 'wb')
         f.write(data)
         f.close()
         
    def saveImgs(self, images, name):
        number = 1
        print u"发现", name, u"共有", len(images), u"张照片"
        for imageURL in images:
            splitPath = imageURL.split('.')
            fTail = splitPath.pop()
            if len(fTail) > 3:
                fTail = "jpg"
            fileName = name + "/" + str(number) + "." + fTail
            print u"正在保存%s的第%s张图片" % (name, str(number))
            self.saveImg("https:" + imageURL, fileName)
            number += 1

    def getDetail(self, item):
        path = self.resultDir + "/" + item[1] + '_' + item[2] + '_' + item[3]
        self.mkdir(path)
        
        #创建请求的request
        req = urllib2.Request(item[0])
        response = self.newOpener.open(req)
        
        images = self.getAllImg(response.read().decode('gbk'))
        self.saveImgs(images, path)
    
    def mkdir(self, path):
        isExists=os.path.exists(path)
        # 判断结果
        if not isExists:
            os.makedirs(path)
            
    def start(self):
        self.login()
        self.mkdir(self.resultDir)
        self.getPage()
        items = self.getContent()
        for item in items:
            self.getDetail(item)
  