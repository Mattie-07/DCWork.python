#tip Calculator
print("How much was the bill?")
billAmount = float(input())
print("Thank you!")
print("And be honest...how was the service? Bad, fair, or was it great!?")
servicelevel = input()
if(servicelevel == "bad"):
  tip = (billAmount * 0.10) 
  print("You should leave a tip of $", tip)  
if(servicelevel == "fair"):
    tip = (billAmount * 0.15)
    print("They did okay, Leave a tip of $", tip)
if(servicelevel == "great"):
    tip = (billAmount * 0.20)
    print("Go ahead! Leave them a tip of $", tip)

