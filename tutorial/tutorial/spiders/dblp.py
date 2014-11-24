# -*- coding: utf-8 -*-

import scrapy

class dblp(scrapy.Spider):
	"""docstring for dblp"""
	name = 'dblp_spider'
	allowed_domains = ['http://dblp.uni-trier.de/']
	start_urls = [
		'http://dblp.uni-trier.de/pers?prefix=%c'%(str(ch+65)) for ch in range(0,26)
	]

	def __init__(self, arg):
		super(dblp, self).__init__()
		self.arg = arg
		
	def parse(self):
		author=response.url.split[-1]