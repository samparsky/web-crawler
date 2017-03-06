import scrapy
from scrapy.spiders import Spider
from scrapy.selector import Selector
from mommypoppins.items import MommypoppinsItem
from extruct.jsonld import JsonLdExtractor

class Wizard(scrapy.Spider):
	name 	 	 = "wizard"
	base_url	 = 'https://mommypoppins.com'
	current_page = 1
	base_query 	 = 'https://mommypoppins.com/events?area%5B%5D=118&field_event_date_value%5B%5D=03-04-2017&event_end=2017-04-07&page='
	start_urls 	 = []
	MAX        	 = 20

	def __init__(self):
		super().__init__()
		self.start_urls.append( self.base_query+str(self.current_page) )
	
	
	def extract_body(self,response):
		''''
		Extract data from html body	
		@scrapes body of the response to parse using xpath
		'''
		event = {}

		event_name = "//h1[@id='page-title']/text()"
		event['name'] = response.xpath(event_name).extract_first()
		
		description = '//div[contains(@class,"field-type-text-with-summary")]//div[contains(@class,"field-items")]//div[contains(@class, "field-item even")]/p/text()'
		event['description'] = response.xpath(description).extract_first()

		location = '//span[contains(@class, "fn")]/text()'
		event['location'] = response.xpath(location).extract_first()
		event['url']     = response.url

		start_date = '//span[contains(@class, "date-display-single")]/text()'
		event['startDate'] = response.xpath(start_date).extract_first()

		return event;

	def parse_item(self, response):
		'''
		Extract data from application/ld+json of the html document
		@url parses each url from the search result page
		@returns event
		@scrapes name description location url startDate event_link age_group price
		'''
		extractor = JsonLdExtractor()
		items = extractor.extract(response.body_as_unicode(), response.url)

		if len(items['items']) == 0:
			'''
			Extract from html body if application/ld+json is empty
			'''
			items['items'] = []
			body_extract = self.extract_body(response)
			items['items'].append(body_extract)

		# xpath rules for extracting data
		EVENT_LINK_XPATH = '//div[contains(@class,"field-name-field-website")]//div[contains(@class, "field-item even")]/a/@href'
		AGE_GROUP        = '//div[contains(@class, "field-name-field-age")]//div[contains(@class,"field-items")]//div[contains(@class,"field-item")]/text()'
		PRICE            = '//div[contains(@class, "field-name-field-price")]//div[contains(@class,"field-items")]//div[contains(@class,"field-item")]/text()'

		event = MommypoppinsItem()
		
		event['event_name']  = items['items'][0]['name']
		event['description'] = items['items'][0]['description']
		event['location']    = items['items'][0]['location']
		event['link']        = items['items'][0]['url']
		event['date']  		 = items['items'][0]['startDate']
		event['event_link']  = response.xpath(EVENT_LINK_XPATH).extract_first()
		event['age_group']   = response.xpath(AGE_GROUP).extract_first()
		event['price']       = response.xpath(PRICE).extract_first()
		
		return event
		                
	def parse(self, response):
		
		SET_SELECTOR = '.view-content'
		urls         = []
		# parse content 
		for data in response.css(SET_SELECTOR):
			NAME_SELECTOR = '//span/a/@href'
			urls = data.xpath(NAME_SELECTOR).extract()

		for item_url in urls:
			item_url = self.base_url + item_url
			yield scrapy.Request(item_url, self.parse_item)

		if self.current_page < self.MAX:
			urls = []
			self.current_page += 1
			yield scrapy.Request(self.base_query+str(self.current_page), self.parse)

