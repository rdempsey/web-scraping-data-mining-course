# Web Scraping and Data Mining Course
Code files and more for my [web scraping and data mining course](http://robertwdempsey.com/web-scraping-data-mining-course/)

## Running the Sample Site for Scraping (Week 2)

### Prerequisites

* Python >= 3.5.1

### Instructions

1. Change into the week2/test_site directory
2. Run a web server in the current directory:
```
python -m http.server
```


## Running the Twitter Example Scripts (Week 4)

### Prerequisites

* Python >= 3.5.1
* Tweepy >= 3.5.0

### Instructions

1. Install Tweepy:
```
pip install tweepy
```
2. Create an application on [http://apps.twitter.com](http://apps.twitter.com)
3. Copy config/example.ini to config/config.ini
4. Add your credentials to config/config.ini
5. (Optional) If you're going to save the tweets to a SQLite database, add the full path to the database file to config.ini
6. Run the sample scripts in the week4 folder
7. Enjoy the awesome


## Running the Forecast.io Example Scripts (Week 4)

### Prerequisites

* Python >= 3.5.1
* python-forecastio >= 1.3.4

### Instructions

Install python-forecastio:
```
pip install python-forecastio
```

1. Sign up for a developer account at [Forecast.io](https://developer.forecast.io/)
2. Add your api key to the config file
3. Run the sample scripts in the week4 folder
4. Enjoy the awesome!


## Simple Web Scraper: PBIC Pricing Scraper (Week 5)

### Prerequisites

* Python >= 3.5.1
* BeaufifulSoup4 >= 4.4.1

### Instructions

1. Change the file path on line 80 of pbic_pricing_scraper.py or in the Jupyter notebook file
2. Run the script (or notebook)


## Web Spider With Scrapy: govbenefitsspider (Week 5)

### Prerequisites

* Python >= 2.7.11
* Scrapy >= 1.0.5
* fake-useragent >= 0.0.8
* service_identity >= 14.0.0

### Available Spiders

1. benefitstofile: scraper to save the entire HTML response to a file
2. benefitlist: scraper to grab only the programs from the list page
3. benefitprogramspider: full on looping spider; will get the details for each program


### Instructions

Install Scrapy and fake-useragent
```
pip install scrapy
pip install fake-useragent
```

1. Change into the govbenefitsspider/govbenefitsspider directory
2. Run the following commmands replacing [NAME_OF_SPIDER] with the name of one of the spiders above:
```
scrapy crawl [NAME_OF_SPIDER]
```