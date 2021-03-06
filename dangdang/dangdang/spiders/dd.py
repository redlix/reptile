#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Time    : 2019-03-30 22:02
@Author  : red
@Site    : 
@File    : dd.py.py
@Software: PyCharm
"""
import scrapy
from dangdang.items import DangdangItem
from scrapy.http import Request


class DdSpider(scrapy.Spider):
	name = "dd"
	allowed_domains = ["dangdang.com"]
	start_urls = (
		'http://category.dangdang.com/pg1-cp01.54.06.00.00.00.html',
	)

	def parse(self, response):
		item = DangdangItem()
		item["title"] = response.xpath("//a[@name='itemlist-title']/@title").extract()
		item["link"] = response.xpath("//a[@name='itemlist-title']/@href").extract()
		item["comment"] = response.xpath("//a[@name='itemlist-review']/text()").extract()
		yield item
		for i in range(2, 101):
			url = "http://category.dangdang.com/pg" + str(i) + "-cp01.54.06.00.00.00.html"
			yield Request(url, callback=self.parse)
