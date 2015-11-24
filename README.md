# cs294
projects
This program is a web crawler/scraper
This program uses the scrapy frame work. http://scrapy.org
Currently scrapes park alert warning from http://www.nps.gov/havo/index.htm.

Usage 
from consle while in top directory (i.e. ~/trailApp/), 

scrapy crawl havo -o havo.json

or 

scrapy crawl havo

a test spider called test has been updated, it will parse both a local and online version of the 
file and it should return the same scraped data (until the website is updated).
Test file is havoAlert.json, 

test can be run with 

scrapy crawl test

Notes:
To enable the log and output, in settings.py comment out:  
LOG_ENABLED = False
LOG_LEVEL = 'INFO'
