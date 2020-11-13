#print the first 100 triangle numbers. 
# the first triangle number is 1
# the second is 1 + 2 = 3
# The 3rd is 1 + 2 + 3 = 6
# 4th is 10
# and so on.

x = 3     #The number of triangle numbers 
y = 1       # our iterator that will continue to increase with each triangle
counter = 1  # The number of iterations ot go through the triangle
tempV = 2

while(counter <= 15):
    print(y)
    y += tempV
    counter += 1
    tempV = y
    