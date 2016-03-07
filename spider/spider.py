# -*- coding:utf-8 -*-
import urllib2
import re

class QXBK:
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
            

qsbk = QXBK(1)
qsbk.start()