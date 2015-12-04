from __future__ import absolute_import
import scrapy
import json

from trailApp.items import TrailappItem
from scrapy.crawler import CrawlerProcess


class HavoSpider(scrapy.Spider):
    name = "havo"
    allowed_domains = ["nps.gov"]
    start_urls = (
        'http://www.nps.gov/pwr/renderhandlers/cs_chooser/rh_alert_chooser_json.cfm?siteC    ode=havo&ts=',
        )

    def parse(self, response):
        items = []
        jsonresponse = json.loads(response.body_as_unicode())
        for sel in jsonresponse["items"]:
            item = TrailappItem()
            item["title"] = sel ["title"]
            item["description"] = sel ["description"]
            items.append(item)

class TestSpider(scrapy.Spider):
    name = "test"
    allowed_domains = ["nps.gov"]
    start = (
        'file:////Users//Mac//Desktop//cs294//scrapy//trailApp//havoAlert.json'
        )
    def parse(self, response):
        items = []
        jsonresponse = json.loads(response.body_as_unicode())
        for sel in jsonresponse["CEDATA"]:
            item = TrailappItem()
            item["title"] = sel["FIC_title"]
            item["description"] = sel["FIC_description"]
            items.append(item)


process = CrawlerProcess()
process.crawl(havo)
process.crawl(test)
process.start()
