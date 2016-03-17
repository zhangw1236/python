import scrapy
import sys

from scrapyspider.items import QsbkItem

reload(sys)
sys.setdefaultencoding('utf8') 

class QsbkSpider(scrapy.spiders.Spider):
    name = "qsbk"
    
    def __init__(self, page=None):
        self.start_urls = ["http://www.qiushibaike.com/hot/page/%s" % page]
        
    def parse(self, response):
        for sel in response.xpath("//div[@class='article block untagged mb15']"):
            item = QsbkItem()
            authorSel = sel.xpath("./div[@class='author clearfix']/a/h2")
            item['author'] = authorSel.xpath("text()").extract()[0].decode("utf-8")
            contentSel = sel.xpath("./div[@class='content']")
            item['content'] = contentSel.xpath("text()").extract()[0].decode("utf-8")
            yield item
