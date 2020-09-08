


import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup


url = input('Enter - ')
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html.read(), 'html.parser')

lspan = soup('span')
counter = 0
for span in lspan:
    print('span:',span)
    print('Value:',span.string)
    counter = counter + int(span.string)
print('Total:',counter)
