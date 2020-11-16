



userInput = float(input("What is the Farenheits you would like returned in Celsius?\n"))

def celsciusMethod(temp):
    celciusTemp  =( temp - 32 ) * 5/9
    return celciusTemp

print(f"The tempurate in Celcius is {celsciusMethod(userInput)}") 