shrs = input("Enter Hours:")
srate = input("Enter Rate:")
try:
    fhrs = float(shrs)
    frate = float(srate)
except:
    print("Error, please enter numeric input")
    quit()
salary = 0
if fhrs <= 40 :
  salary = fhrs * frate
elif fhrs > 40:
    reg =  fhrs * frate
    otp = (fhrs - 40.0) * (frate * 0.5)
   salary = reg + otp

print(salary)
