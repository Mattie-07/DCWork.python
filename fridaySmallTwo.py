#Celcius conversion
#F = (C * 9/5) + 32
# The user enters the celcius and the Farenheit is returned


userInput = int(input("What is the Celcius you would like retured for the Farenhiet\n"))

def farenTemp(temp):
    Farenheit  =( temp * 9/5 )+ 32
    return Farenheit

print(f"The tempurate in Farenheit is {farenTemp(userInput)}") 
