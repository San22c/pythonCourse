
total = 0.0
count = 0
while True:
    ientry = input("Enter a number: ")
    if ientry != "done":
        try:
            fentry = float(ientry)
        except:
            print("Error, please enter numeric input")
            continue;
        total = total + fentry
        count = count + 1
    else:
        break;

print(total, count, total/count)
