#Would count the number of coins the user wants.
coins = 0
print("You have 0 coins")
while (True):
    answer = input("Would you like a coin?\n")
    if(answer != "yes"):
      break
    coins += 1
    print("You have %d coin(s)" % coins)
print("You finished with %d coins" % coins)

