# -*- coding: utf-8 -*-

import scrapy
from tutorial.items import TutorialItem
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

class dblp(scrapy.Spider):
	"""docstring for dblp"""
	name = 'dblp_spider'
	allowed_domains = ['http://dblp.uni-trier.de/']
	start_urls = [
		'http://dblp.uni-trier.de/pers?pos=1'
	]

	def __init__(self, arg):
		super(dblp, self).__init__()
		self.arg = arg
		
	def parse(self):

		sel = Selector(response)

		if response.url[-1] in string.letter:
			#此时为类似http://dblp.uni-trier.de/pers?pos=1的页面
			url_item = response.url.split('=')
			next_url = url_item[0] + str(int(url_item[1])+300)]
			next_author =  sel.xpath('//*[@id="browse-person-output"]/div/div[1]/ul/li[1]/a/text()')
			return #...
		else:
			#此时为类似http://dblp.uni-trier.de/pers/hd/a/A:Arun_Kumar的页面
			item = TutorialItem()
			item['name'] =  sel.xpath('//span[@class="this-person"]/text()').extract()
			item['article'] =  sel.xpath('//span[@class="title"]/text()').extract()
			item['coauther'] = sel.xpath('//div[@class="data"]/a/text()').extract()
