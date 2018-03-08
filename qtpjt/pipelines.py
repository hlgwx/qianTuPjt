# -*- coding: utf-8 -*-
import urllib.request
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class QtpjtPipeline(object):
    def process_item(self, item, spider):
        for i in range(0,len(item["picurl"])):
            trueurl=item["picurl"]
            localpath="G:/qtpic/"+item["picid"]
            urllib.request.urlretrieve(trueurl,filename=localpath)
        return item
