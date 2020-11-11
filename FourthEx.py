print("Whats the size of the box you want??")
width = int(input("Input the width\n"))
height = int(input("Input the height\n"))
stars = 0
while (stars < width):
    print("*")
    stars += 1
# regardless of what the user input make sure that a star is printed at first then whatever the user
# inputs as the width would need to be used to add a star at the very end too. pr F