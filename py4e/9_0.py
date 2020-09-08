#Counting words

#Create dictionary
dwords = dict()

#Input sentence
line = input('Enter a line of text:')

#Split words

swords = line.split()
print(swords)
print('Counting...')
for word in swords:
    dwords[word] = dwords.get(word,0) + 1

print(dwords)        
