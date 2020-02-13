# -*- coding: utf-8 -*-
import scrapy


class ItemSpider(scrapy.Spider):
    name = 'item'
    allowed_domains = ['www.ptt.cc']
    start_urls = ['http://www.ptt.cc/']

    def parse(self, response):
        pass
