# -*- coding: utf-8 -*-

import scrapy
import string

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
			next_url = [response.url[:-2] + str(int(response.url[-1])+1)]
			next_author =  sel.xpath()
			return #...
		else:
			#此时为类似http://dblp.uni-trier.de/pers/hd/a/A:Arun_Kumar的页面
			item = TutorialItem()
			item['name'] =  sel.xpath( ).extract()
			item['article'] =  sel.xpath( ).extract()
			item['coauther'] = sel.xpath( ).extract()

		

