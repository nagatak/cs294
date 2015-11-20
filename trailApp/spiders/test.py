# -*- coding: utf-8 -*-
import scrapy
import json
from trailApp.items import TrailappItem

class HavoSpider(scrapy.Spider):
    name = "test"
    #allowed_domains = ["*"]
    start_urls = (
        #'http://www.nps.gov/havo/nps-alerts-havo.json?tmsp=',
        'file:////Users//Mac//Desktop//cs294//scrapy//trailApp//havoAlert.json',
    )

    def parse(self, response):
        items = []
        jsonresponse = json.loads(response.body_as_unicode())
        for sel in jsonresponse["CEDATA"]:
            item = TrailappItem()
            item["title"] =  sel["FIC_title"]
            item["description"] = sel["FIC_description"]
            items.append(item)

        yield item
   # def parse(self, response):
   #     filename = 'test.html'
   #     with open(filename, 'wb') as f:
   #         f.write(response.body)
