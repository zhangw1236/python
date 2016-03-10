# -*- coding:utf-8 -*-
import urllib2
import re
from tool import Tool

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