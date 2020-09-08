
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

# prompt fo a url
url = input('Enter URL:')
html = urllib.request.urlopen(url).read().decode()


tree = ET.fromstring(html)   #Make a tree xml
lcomments = tree.findall('comments/comment')
count = 0
print(lcomments)
for  c in  lcomments:
    count = count + int(c.find('count').text)

print('Total:', count)
