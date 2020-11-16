# Write a function that accepts a List of numbers as an argument.
# Return a new List that includes the only the even numbers.

# a while or for look could be used, at least for the length of the listofNumbers
# userList = input("H! input a list of numbers to see if they are ")


listOfNumbers = [18, 30,17 , 21, 99 ,316]
myList = []
def returningEvens(someList):
    for x in someList:
        counter = 0
        while( counter <= len(listOfNumbers)):
            if counter == 6:  # had to add this to my code in order for it to work - honestly not sure why
                continue
            checkValue = isEven(someList[counter])
            if checkValue == True:
                newList = someList.append([counter])
            counter += 1
    return newlist


def isEven(number):
    if number % 2 == 0 :
        print("Your number is even! Congradulations!")
        return True
    else:
        print("Your number is odd. Sorry!")
        return False

lastList = returningEvens(listOfNumbers)
print(lastList)






# def returningEvens(numberList):
#     createdList =[]
#     for i in range (listOfNumbers:
#         if listOfNumbers[i] % 2 == 0:
#             createdList = listOfNumbers.append[i]
#     return createdList

# newList = returningEvens(listOfNumbers)
