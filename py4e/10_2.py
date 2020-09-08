#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
#  You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#  From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#  Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.


# File's name
fname = input('Enter a file name:')
hfile = open(fname)
dhours = dict()

for line in hfile:
    if line.startswith('From '):
         sline = line.split()
         shours = sline[5].split(':')
         dhours[shours[0]] = dhours.get(shours[0],0) + 1

#dictionary completed
#Use idiom to transfor dictionary into a list and sorted it
litems = sorted([(k,v) for k,v in dhours.items()])
for k,v in litems:
    print(k,v)
