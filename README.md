# Web Scraping and Data Mining Course
Code files and more for my [web scraping and data mining course](http://robertwdempsey.com/web-scraping-data-mining-course/)

## Running the Sample Site for Scraping (Week 2)

### Prerequisites

* Python (3.5)

### Instructions

1. Change into the week2/test_site directory
2. Run a web server in the current directory:
```
python -m http.server
```

## Running the Twitter Example Scripts (Week 4)

### Prerequisites

* Python 3.5.1
* Tweepy 3.5.0

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

* Python 3.5.1
* python-forecastio 

### Instructions

1. Install python-forecastio:
```
pip install python-forecastio
```
2. Sign up for a developer account at [Forecast.io](https://developer.forecast.io/)
3. Add your api key to the config file
4. Run the sample scripts in the week4 folder
5. Enjoy the awesome!