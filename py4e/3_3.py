
#Enter score
score = input("Enter Score: ")
fscore = float(score)
if fscore >= 0.0 and fscore <= 1.0:
    if fscore >= 0.9 :
        print("A")
    elif fscore >= 0.8 :
        print("B")
    elif fscore >= 0.7 :
        print("C")
    elif fscore >= 0.6 :
        print("D")
    else:
        print("F")
else :
    print("Error enter a number between 0.0 and 1.0")
