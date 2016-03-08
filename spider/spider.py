# -*- coding:utf-8 -*-
import urllib2
import re
import sys

reload(sys)   
sys.setdefaultencoding('utf8') 

class Tool:
    #去除img标签,7位长空格
    removeImg = re.compile('<img.*?>| {7}|')
    #删除超链接标签
    removeAddr = re.compile('<a.*?>|</a>')
    #把换行的标签换为\n
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    #将表格制表<td>替换为\t
    replaceTD= re.compile('<td>')
    #把段落开头换为\n加空两格
    replacePara = re.compile('<p.*?>')
    #将换行符或双换行符替换为\n
    replaceBR = re.compile('<br><br>|<br>')
    #将其余标签剔除
    removeExtraTag = re.compile('<.*?>')
    
    def replace(self,x):
        x = re.sub(self.removeImg, "", x)
        x = re.sub(self.removeAddr, "", x)
        x = re.sub(self.replaceLine, "\n", x)
        x = re.sub(self.replaceTD, "\t", x)
        x = re.sub(self.replacePara, "\n", x)
        x = re.sub(self.replaceBR, "\n", x)
        x = re.sub(self.removeExtraTag, "", x)
        #strip()将前后多余内容删除
        return x.strip()
    
class QSBK:
    def __init__(self, page):
        self.page = page
        self.url = 'http://www.qiushibaike.com/hot/page/' + str(self.page)
        self.headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36"}
        self.content = ""

    def getPageContent(self):
        try:
            request = urllib2.Request(self.url, headers=self.headers)
            response = urllib2.urlopen(request)
            content = response.read().decode("utf-8")
        except urllib2.URLError, e:
            if hasattr(e,"code"):
                print e.code
            if hasattr(e,"reason"):
                print e.reason
            return None
    
        #([\s\S]*) 匹配包括换行符的任意字符
        #(.*?)代表一个分组
        
        pattern = re.compile('<div.*?author clearfix">[\s\S]*?<a[\s\S]*?<img.*?alt="(.*?)"/>[\s\S]*?<div.*?content">([\s\S]*?)<!--.*?>')
        
        items = re.findall(pattern, content)
        
        results= []
        for item in items:
            results.append("author: " + item[0] + "\ncontent: " + item[1].strip('\n') + "\n")
            
        return results
        
    def start(self):
        result = self.getPageContent()
        if result == None:
            return
        
        for item in result:
            print item
            

class BDTB:
    def __init__(self, url, seeLz):
        self.baseUrl = url
        self.seeLz = '?see_lz='+str(seeLz)
        self.headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36"}
        self.content = ""
        self.tool = Tool()
        self.file = open("result.txt","w+")
        
    def getPage(self,pageNum):
        try:
            url = self.baseUrl+ self.seeLz + '&pn=' + str(pageNum)
            request = urllib2.Request(url, headers=self.headers)
            response = urllib2.urlopen(request)
            self.content = response.read().decode("utf-8")
        except urllib2.URLError, e:
            if hasattr(e,"code"):
                print e.code
            if hasattr(e,"reason"):
                print e.reason

    def getTitle(self):
        pattern = re.compile("'threadTitle'.*?'(.*?)'")
        result = re.search(pattern, self.content)
        self.writeData(result.group(1).strip())
    
    
    def getPageNum(self):
        pattern = re.compile("l_reply_num.*?<span.*?>(.*?)</span>", re.S)
        result = re.search(pattern, self.content)
        self.writeData(result.group(1).strip())

    def getContent(self):
        pattern = re.compile('<div id="post_content_.*?>(.*?)</div>')
        items = re.findall(pattern, self.content)
        floor = 1
        for item in items:
            self.writeData(str(floor) + u"楼--------------------------------------------------------------------------------")
            self.writeData(self.tool.replace(item))
            floor += 1

    def writeData(self,contents):
        self.file.write(contents+"\n")
        
    def start(self):
         self.getPage(1)
         self.getTitle()
         self.getPageNum()
         self.getContent()
        
def QSBKTest():
    qsbk = QSBK(1)
    qsbk.start()
    
def BDTBTest():
    bdtb = BDTB('http://tieba.baidu.com/p/3138733512', 1)
    bdtb.start()
    
if __name__ == '__main__':
    BDTBTest()
