#Tip Calculator that splits it based on people eating.
print("How much was the bill?")
billAmount = float(input())
print("Thank you!")
print("And be honest...how was the service? Bad, fair, or was it great!?")
servicelevel = input()
if(servicelevel != "great"):
  print("awww, Im sorry to hear that!")
number_of_eaters =float(input("How many people ate today?") )
if(servicelevel == "bad"):
  tip = (  (billAmount * 0.10 )/ number_of_eaters ) 
  print("Everyone should leave a tip of", tip)  
if(servicelevel == "fair"):
    tip = (  ( billAmount * 0.15) / number_of_eaters )
    print("They did okay, Let's all leave a tip of $", tip)
if(servicelevel == "great"):
    tip = ( (billAmount * 0.20) / number_of_eaters )
    print("Go ahead! Let's leave a tip of $", tip)

