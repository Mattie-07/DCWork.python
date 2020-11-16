#namae a subject function
one = input("Please enter a name\n") 
two = input("please enter a subject\n")

def nameAndsubject(name, subject):
    return name, subject

name = nameAndsubject(one, two)
print(f"Your name and the subject you chose are {name}")