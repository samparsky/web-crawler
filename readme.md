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
    event_name  
    description 
    age_group    
    location     
    price        
    link		 
    event_link 
    date
```
The mongodb database is `mommy` and the collection is `crawl`
To view the crawled data run the below commands at the mongo shell

```
 > use mommy
 > db.crawl.find()

```
