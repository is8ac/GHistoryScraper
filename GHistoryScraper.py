# v0.9
import random
import re
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
# Where do you want to save the data?
dataFile = "dataFile.html"
# Clear the data file
open(dataFile, 'w').close()
# Creat a Selenium webDriver object and go to the first page of Google history.
driver = webdriver.Chrome('chromedriver')
driver.get('https://history.google.com/history/app')
# Alow the user to sign in to their Google acount.
raw_input('Sign into you Google acount. Then press enter.')

linkFile = open(dataFile,'a')
isDone = False
n = 1
while isDone == False:
	print 'Now scraping data from page', n,'.'
	# Grab the code and extract the data.
	raw = driver.page_source
	soup = BeautifulSoup(raw)
	clusterContent = soup.findAll("div", {"class": "oc-cluster-content"})
	linkFile.write(str(clusterContent))
	
	# Get the back link and click on it.
	backLink = driver.find_element_by_link_text('Older')
	backLink.click()
	url = driver.current_url
	signIn = re.compile('.*accounts.*')
	if signIn.match(url):
		raw_input('Looks like Google wants you to sign in again. \n When you have done so, press enter.')
	# Be kind to the server.
	time.sleep(random.uniform(1,5))
	# Check if there is a back butten.
	try:
		driver.find_element_by_link_text('Older')
	except NoSuchElementException:
		isDone = True
		raw_input("Am I done now?")
	#raw_input('Press enter to continue.')
	n = n+1
linkFile.close()
driver.quit()

print("Your Google History has been scraped.")
print("Look in", dataFile, "for the data.")
