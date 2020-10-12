# -*- coding: utf-8 -*-
import scrapy


class NbabbsSpider(scrapy.Spider):
    name = 'nbabbs'
    allowed_domains = ['ptt.cc']
    start_urls = ['https://www.ptt.cc/bbs/NBA/index.html']

    def parse(self, response):
        target = response.css("div.r-list-container")
        titles = target.css("div.r-ent")
        for title in titles:
        	data = dict()
        	try:
        		num = title.css("div.nrec span::text").extract_first().strip()
        		if num=="爆":
        			data['num'] = 100
        		else:
        			data['num'] = int(num)
        	except:
        		data['num'] = 0
        	data['href'] = title.css("div.title a::attr(href)").extract_first()
        	if data['href'] is not None:
        		data['href'] = data['href'].strip()
        	data['title'] = title.css("div.title a::text").extract_first()
        	if data['title'] is not None:
        		data['title'] = data['title'].strip()
        	data['author'] = title.css("div.author::text").extract_first()
        	data['date'] = title.css("div.date::text").extract_first()
        	yield data
        next_page = response.css("#action-bar-container > div > div.btn-group.btn-group-paging > a:nth-child(2)::attr(href)").extract_first().strip()
        if next_page is not None:
        	yield response.follow(response.urljoin(next_page), callback=self.parse)
