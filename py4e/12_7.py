
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup


url = input('Enter - ')
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html.read(), 'html.parser')

lnames = list()

x=0
while x<=6:
    lhrefs = soup('a')
    ihref =  lhrefs[17]
    print('span:',ihref)

    lnames.append(ihref.string)
    nwurl= ihref.get('href')
    print('Value:',nwurl)

    nwhtml = urllib.request.urlopen(nwurl)
    soup = BeautifulSoup(nwhtml.read(), 'html.parser')
    x = x+1

print('Total:',lnames)
