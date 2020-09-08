
#Maching and Extracting data

import re

pr = 'xxxxxx@'
y = re.findall('@(.*)',pr)
print('PR:' ,y)

x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]',x)
#Print all numebers separed
print("Every single number separed",y)
z = re.findall('[0-9]+',x)
print("Normal numbers:", z)

#Print only vowels into the sentence
v = re.findall('[AEIOU]+',x)
print("Only upper vowels",v)


#Greedy Maching
e = 'From: Sandra@google.es  Sat Jan 5 09:14:16 2008'
g = re.findall('^F.+:',e)
print('Looking for From. Try one:',g)
#No Greedy Maching  ?
ng = re.findall('^F.+?:',e)
print('Looking for From. Try two:',ng)


#Search a word which contains @
at = re.findall('\S+?@\S+', e)
print('Search just words with @:',at)

#The samen thing but not use \S
domain2 = re.findall('@([^ ]+)',e)
print('just domain2:',domain2)
#Extract just email domain
domain = re.findall('@(\S+)',e)
print('just domain:',domain)
