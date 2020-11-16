
# use my isEven function to determine if the value that I have is odd - 

userNumber = int(input("What is the number that you would like to check to see if it is even?\n"))

def isEven(number):
    if number % 2 == 0 :
        print("Your number is even! Congradulations!")
        return True
    else:
        print("Your number is odd. Sorry!")
        return False


def isOdd(booVariable):
    if (booVariable != True):
        print("The number is odd")
    else:
        print("Yep, that value is still true!"
        )
check = isEven(userNumber)
print(f"The value is {check}")

isOdd(check)