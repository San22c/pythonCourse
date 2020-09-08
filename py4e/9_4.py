#9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
  #The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
  #The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
  #After the dictionary is produced,
  #the program reads through the dictionary using a maximum loop to find the most prolific committer.


#Enter name file
fname = input('Enter a file name:')
#Create a handle
hfile = open(fname)
#Create a dictionary
dsenders = dict()

for line in hfile:
    if line.startswith('From '):
        sline = line.split()
        dsenders[sline[1]] = dsenders.get(sline[1],0) + 1

#Extract the largest item.
sender = None
nmails = None
for k,v in dsenders.items():
    if sender == None or v > nmails:
        sender = k
        nmails = v
#Print output
print(sender,nmails)
