print("Whats the size of the box you want??")
width = int(input("Input the width\n"))
height = int(input("Input the height\n"))

stars = 0

while(stars <= height):
    print("*")
    stars += 1
stars = 0

while(stars <= width):
    if(stars == 1 or stars == width):
        print("*")
    else:
        print(" ")
    stars += 1


#Everytime that that print is used in python a new line happens. 
# regardless of what the user inpupyyt make sure that a star is printed at first then whatever the user
# inputs as the width would need to be used to add a star at the very end too. 
#Lets start with just printing a line that is printed down the command - it will represesnt the height