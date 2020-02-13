# -*- coding: utf-8 -*-
import scrapy


class D26HwSpider(scrapy.Spider):
    name = 'D26_HW'
    allowed_domains = ['www.ptt,cc']
    start_urls = ['http://www.ptt,cc/']

    def parse(self, response):
        pass
