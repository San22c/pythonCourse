largestnumber = None
smallestnumber = None
total = 0.0
count = 0
while True:
    ientry = input("Enter a number: ")
    if ientry != "done":
        try:
            intentry = int(ientry)
        except:
            print("Invalid input")
            continue;

        #largest number
        if largestnumber is None:
            largestnumber = intentry
        if largestnumber < intentry:
            largestnumber = intentry
        #Smallest largestnumber
        if smallestnumber is None:
            smallestnumber = intentry
        if smallestnumber > intentry:
            smallestnumber = intentry
    else:
        break;

print("Maximum is", largestnumber)
print("Minimum is", smallestnumber)
