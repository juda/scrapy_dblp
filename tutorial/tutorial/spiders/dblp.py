# -*- coding: utf-8 -*-

import scrapy
from tutorial.items import TutorialItem
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy import Selector
import re

class dblp(CrawlSpider):
	"""docstring for dblp"""
	name = 'dblp_spider'
	allowed_domains = ['http://dblp.uni-trier.de/']
	start_urls = [
		'http://dblp.uni-trier.de/pers?pos=1'
	]
	rules = [
		Rule(LinkExtractor(allow=['/pers\?pos=[0-9]+']) ),
		Rule(LinkExtractor(allow=['/pers/hd/[a-z]/.+']), 'parse_dblp')
	]

		
	def parse_dblp(self):

		sel = Selector(response)

		pat = re.compile('http://dblp.uni-trier.de/pers/hd/[a-z]/.+')
		if pat.match(response.url):
			aritcles = sel.xpath('//*[re:test(@id,"journals/[a-zA-Z]+/[a-zA-Z]*[0-9]+")]/div[3]/span[2]/text()').extract()
			for aritcle in aritcles:
				item = TutorialItem()
				item['name'] = sel.xpath('/html/head/title/text()').extract()
				item['article'] = article
				yield item
			aritcles = sel.xpath('//*[re:test(@id,"conf/[a-zA-Z]+/[a-zA-Z]*[0-9]+")]/div[3]/span[2]/text()').extract()
			for aritcle in aritcles:
				item = TutorialItem()
				item['name'] = sel.xpath('/html/head/title/text()').extract()
				item['article'] = article
				yield item

