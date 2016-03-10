# -*- coding:utf-8 -*-
import urllib2
import urllib
import re
import sys
import os
import cookielib

from qsbk import QSBK
from bdtb import BDTB
from taobao import TaobaoMM

reload(sys)
sys.setdefaultencoding('utf8') 

      
def QSBKTest():
    qsbk = QSBK(1)
    qsbk.start()
    
def BDTBTest():
    bdtb = BDTB('http://tieba.baidu.com/p/3138733512', 1)
    bdtb.start()
    
def TBTest():
    taobao = TaobaoMM(1, "tbmm")
    taobao.start()
     
if __name__ == '__main__':
    TBTest()
