# -*- coding: utf-8 -*-

import scrapy
from tutorial.items import TutorialItem
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy import log
from scrapy.http import Request
import os
import re
import time

class dblpSpider(Spider):
	"""docstring for dblp"""
	name = 'dblp'
	allowed_domains = ['dblp.uni-trier.de']
	start_urls = [
		'http://dblp.uni-trier.de/pers?pos=1'
	]

		
	def parse(self, response):

		print response.url
		sel = Selector(response)
		if(response.url == 'http://dblp.uni-trier.de/pers?pos=1'):
			sites = sel.xpath('//div/ul/li/a/@href').extract()
			for site in sites:
				print site
				yield Request(site ,callback=self.parse)
		else:
			time.sleep(1)
			pat = re.compile('http://dblp.uni-trier.de/pers/hd/[a-z]/.+')
			if pat.match(response.url):
				aritcles = sel.xpath('//*[re:test(@id,"journals/[a-zA-Z]+/[a-zA-Z]*[0-9]+")]/div[3]/span[2]/text()').extract()
				print 'aritcles'
				print aritcles
				for aritcle in aritcles:
					item = TutorialItem()
					item['name'] = sel.xpath('/html/head/title/text()').extract()
					item['article'] = aritcles
					yield item
				aritcles = sel.xpath('//*[re:test(@id,"conf/[a-zA-Z]+/[a-zA-Z]*[0-9]+")]/div[3]/span[2]/text()').extract()
				for aritcle in aritcles:
					item = TutorialItem()
					item['name'] = sel.xpath('/html/head/title/text()').extract()
					item['article'] = aritcles
					yield item

