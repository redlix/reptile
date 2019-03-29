#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Time    : 2019-03-29 17:06
@Author  : red
@Site    : 
@File    : fst.py
@Software: PyCharm
"""
import scrapy
from first_scrapy.items import FirstScrapyItem


class FirstSpider(scrapy.Spider):
	name = 'fst'
	allowed_domains = ["aliwx.com.cn"]
	start_urls = ["http://www.aliwx.com.cn/"]

	def parse(self, response):
		item = FirstScrapyItem()
		item['title'] = response.xpath("//p[@class='title']/text()").extract()
		yield item
