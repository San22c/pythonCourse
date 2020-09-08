
#https://www.crummy.com/software/BeautifulSoup/bs4/doc/
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup


url = input('Enter - ')
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html.read(), 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
print(type(tags))
print(tags)
for tag in tags:
 print(tag.get('href', None))
