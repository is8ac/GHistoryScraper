# Google History Scraper
Scrapes you full Google history found [here](https://history.google.com/history/app).

Google allows you to download your search history, and you can usually grab the browsers local history, however Google does not yet allow users to download there full web and app activity. (Note that this may be terned off by befalt, you can change this at [here](https://www.google.com/settings/accounthistory/search).) Google shows you this history, but only 24 entrys at a time.

For each page this Python script scraps the relevint data and appends it to the end of the file

## Setup
You will need [Seleneam](http://www.seleniumhq.org/) and [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup).

  pip install beautifulsoup4
  pip install selenium

You will also need to put the selenium web driver in you path. You can download the Chrome web driver [here](https://sites.google.com/a/chromium.org/chromedriver/downloads).

Note that I have only tested this on Ubuntu 15.04 with Chromium. I expect that it shuld work on other Linux distrobutions, and it should work with with other browsers if you change driver = webdriver.Chrome('chromedriver') to some other driver

## Usage
Open the terminal and type:

  python GHistoryScraper.py

A file will be created (you can change the name by editing the line 'dataFile = "dataFile.html"' and replacing dataFile.html with whatever you want). Selenium should then put up a new Chrome window. Google will immediately redirect you to the sign in page. Sign in to you Google account, (as this is the normal Google authentication page second factor authentication will work fine), and then, back at the shell, press enter to continue. GHistoryScraper will download the data from each file and append it to the data file.

If you have less then ~1500 history entries, then it should run fine. However if you have lots of entries, then it it will run for more then ~10 minutes, and Google will ask you to sign in again. When this happens, the the script will ask you to sign in again. When you have done this, press enter to resume.
