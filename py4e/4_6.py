def computepay(h,r):
    salary = 0

    if fhrs > 40:
        reg =  fhrs * frate
        otp = (fhrs - 40.0) * (frate * 0.5)
        salary = reg + otp
    else:
        salary =   fhrs * frate
    return salary


shrs = input("Enter Hours:")
srate = input("Enter Rate:")
try:
    fhrs = float(shrs)
    frate = float(srate)
except:
    print("Error, please enter numeric input")
    quit()

p = computepay(10,20)
print("Pay",p)
