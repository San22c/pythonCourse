
#Finding Numbers in a Haystack

#In this assignment you will read through and parse a file with text and numbers.
#You will extract all the numbers in the file and compute the sum of the numbers.

import re

fname = input('Enter file name:')
handle = open(fname)

txt = handle.read()

mtnumber = re.findall('[0-9]+',txt)
print('List of numbers:',mtnumber)

score = 0
for n in mtnumber:
    score = score + int(n)

print('Total:', score)
