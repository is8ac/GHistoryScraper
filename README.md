# Recently, Google has made major changes to the history page breaking this script. I intend to soon update the code for the new page, however in mean time there is no point in using this script. Check back soon.

# Google History Scraper
Scrapes your full Google history found [here](https://history.google.com/history/app).

Google allows you to download your search history, and you can usually grab the browser's local history. However, Google does not yet allow users to download their full web and app activity. (Note that this may be turned off by default, you can change this at [here](https://www.google.com/settings/accounthistory/search).) Google shows you this history, but only 24 entries at a time.

For each page this Python script scrapes the relevant data and appends it to the end of the file.

## Setup
You will need [Selenim](http://www.seleniumhq.org/) and [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup).

  pip install beautifulsoup4
  
  pip install selenium

You will also need to put the Selenium web driver in your path. You can download the Chrome web driver [here](https://sites.google.com/a/chromium.org/chromedriver/downloads). Then you should be able to just copy it to ~/bin/.

Note that I have only tested this on Ubuntu 15.04 with Chromium. I expect that it should work on other Linux distributions, and it should work with with other browsers if you change "driver = webdriver.Chrome('chromedriver')" to some other driver.

## Usage
Open the terminal and type:

  python GHistoryScraper.py

A file will be created names dataFile.html. (You can change the name by editing the line 'dataFile = "dataFile.html"' and replacing dataFile.html with whatever you want.) Selenium should then put up a new Chrome window. Google will immediately redirect you to the sign in page. Sign in to your Google account, (as this is the normal Google authentication page second factor authentication will work fine), and then, back at the shell, press enter to continue. GHistoryScraper will download the data from each file and append it to the data file.

If you have less then ~1500 history entries, then it should run fine. However, if you have lots of entries, then it will run for more then ~10 minutes, and Google will ask you to sign in again. When this happens, the script will ask you to sign in again. When you have done this, press enter to resume.

The output file is a series of html of the structure:
  
  <div>Visited 
    <a href="https://www.example.com/page.html">
      <div class="oc-chrome-title">page title</div>
    </a> - example.com - on ComputerName - 12:34pm
  </div>

Now that it is all in one file, you can use linux coreutils to parse it.
