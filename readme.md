## Simple Web Crawler
-----------------

This is a simple web crawler that crawls
[link](https://mommypoppins.com/events?area%5B%5D=118&field_event_date_value%5B%5D=03-04-2017&event_end=2017-04-07). Parses through the results page. It works based on the (Scrapy)[https://scrapy.org/] crawling engine. Its uses Extructor

### To start 
------------
```python

pip install -r requirements.txt

````

### To run the crawler

```
 cd <directory>
 scrapy crawl wizard

````

### MongoDB

The mongodb collection schema is as follows

```python
    event_name   = scrapy.Field()
    description  = scrapy.Field()
    age_group    = scrapy.Field()
    location     = scrapy.Field()
    price        = scrapy.Field()
    link		 = scrapy.Field()
    event_link   = scrapy.Field()
    date   		 = scrapy.Field()
```
""" This function parses a sample response. Some contracts are mingled
		with this docstring.
		@url http://www.babynamewizard.com/name-list/english-girls-names-most-popular-names-for-girls-in-england
		@returns items 1 1
		@scrapes gender country region names
		"""