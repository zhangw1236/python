# -*- coding:utf-8 -*-
import urllib2
import re
 
page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36"}
content = ""


try:
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    content = response.read().decode("utf-8")
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason
        

#([\s\S]*) 匹配包括换行符的任意字符
#(.*?)代表一个分组

pattern = re.compile('<div.*?author clearfix">[\s\S]*?<a[\s\S]*?<img.*?alt="(.*?)"/>[\s\S]*?<div.*?content">([\s\S]*?)<!--.*?>')

items = re.findall(pattern, content)
 
for item in items:
    print "author: " + item[0] + "\ncontent: " + item[1].strip('\n') + "\n"