#!/usr/bin/env python2.7
from bs4 import BeautifulSoup
import urllib2
import re
URL = input("Input web address to scrape from:\n")
#URL_PRINT = input("Input web address without modifiers:\n")
html_page = urllib2.urlopen(URL)
soup = BeautifulSoup(html_page)
for link in soup.findAll('a'):
	print URL+link.get('href')
