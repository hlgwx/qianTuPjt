# -*- coding: utf-8 -*-
import scrapy
import re
from qtpjt.items import QtpjtItem
from scrapy.http import Request

class QtspdSpider(scrapy.Spider):
    name = 'qtspd'
    allowed_domains = ['58pic.com']
    start_urls = ['http://www.58pic.com/piccate/3-0-0-1.html']

    def parse(self, response):
        item=QtpjtItem()
        pat = 'http://pic.qiantucdn.com/58pic.*?\..*?g'
        pat2 = 'http://pic.qiantucdn.com/58pic(.*?)\.(.*?)$'
        pat3 = '.*?_PIC2018$'
        results = re.compile(pat).findall(str(response.body))
        for result in results:
            pic = re.compile(pat2).findall(result)
            picid = re.sub(r"/", "", pic[0][0])
            picname = picid + '.' + pic[0][1]
            print(picname)
            picid3 = re.compile(pat3).findall(picid)
            if (len(picid3) > 0):
                trueurl = "http://pic.qiantucdn.com/58pic" + pic[0][0] + "." + pic[0][1]
            else:
                trueurl = "http://pic.qiantucdn.com/58pic" + pic[0][0] + "_1024." + pic[0][1]
            item["picurl"]=trueurl
            item["picid"]=picname
            yield item
            for i in range(1,285):
                nexturl='http://www.58pic.com/piccate/3-0-0-'+str(i)+'.html'
                yield Request(nexturl,callback=self.parse)
