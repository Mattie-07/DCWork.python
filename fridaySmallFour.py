# Write a method that accepts a number and returns true if it is even and false if it is not.


userNumber = int(input("What is the number that you would like to check to see if it is even?\n"))

def isEven(number):
    if number % 2 == 0 :
        print("Your number is even! Congradulations!")
        return True
    else:
        print("Your number is odd. Sorry!")
        return False

check = isEven(userNumber)
print(f"The value is {check}")