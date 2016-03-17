# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class QsbkPipeline(object):
    def process_item(self, item, spider):
        print 'author: ', item['author']
        print 'content: ', item['content']
