# -*- coding: utf-8 -*-
import scrapy
import json
from trailApp.items import TrailappItem

class HavoSpider(scrapy.Spider):
    name = "test"
    allowed_domains = ["nps.gov"]
    start_urls = (
    'http://www.nps.gov/pwr/renderhandlers/cs_chooser/rh_alert_chooser_json.cfm?siteCode=havo&ts=',
    )

    def parse(self, response):
        items = []
        jsonresponse = json.loads(response.body_as_unicode())
        for sel in jsonresponse["items"]:
            item = TrailappItem()
            item["title"] = sel ["title"]
            item["description"] = sel ["description"]
            items.append(item)

        yield item
