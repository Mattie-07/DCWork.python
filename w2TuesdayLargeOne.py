# You will write a command line program to manage a phone book. When you start the phonebook.py program, it will print out a menu and ask the user to enter a choice:

# $ python3 phonebook.py
# Electronic Phone Book
# =====================
# 1. Look up an entry
# 2. Set an entry
# 3. Delete an entry
# 4. List all entries
# 5. Quit

# What do you want to do (1-5)?
# If they choose to look up an entry, you will ask them for the person's name, and then look up the person's phone number by the given name and print it to the screen.
# If they choose to set an entry, you will prompt them for the person's name and the person's phone number,
# If they choose to delete an entry, you will prompt them for the person's name and delete the given person's entry.
# If they choose to list all entries, you will go through all entries in the dictionary and print each out to the terminal.
# If they choose to quit, end the program.

print("Electronic Phone Book\n=========================\n1.Look up an entry\n2.Set an entry\n3.Delete an entry\n4.List all entries\n5.Quit")
answer = int(input("What would you like to do?(Type the numbers between 1 - 5)\n" ))
phonebook = {
    "Matthew" : "777-777-7777",
    "John"    : "664-222-2222",
    "Greg"    : "111-222-2222"
}

def numberCheck(number):
    if answer == 1 :
        print("You would like to look up someone.")
        name = input("Could you please type the person's name?\n")
        person = phonebook.get(name)
        print(person)

        # isFound = name in phonebook
        # if(isFound):
        #     print(name,phonebook[name])
        # else:
        #     print('name not found')

    elif answer == 2 : 
        print("You would like to set a new entry!")
        newName = input("Could you provide the name of the person you would like to add?\n")
        newNumber = input("Could you provide the number of the person you would like to add?\n")
        phonebook[newName] = newNumber
        print(f"You just added {phonebook[newName]}")
    elif answer == 3 : 
        print("You want to delete an entry")
        name = input("Please provide the name of the person you would like to remove from the phonebook\n")
        del phonebook[name]
    elif answer == 4:
        print("You want to see all of the entries in the phonebook\n")
        for key, value in phonebook.items():
            print(key)
            print(value)
    elif answer == 5: 
        print("You chose to quit.\n Good bye!")
        return
    elif answer > 5 :
        print("I'm sorry, your numbers should be within in the range of 1 to 5 ")


numberCheck(answer)


# for key, value in phonebook.items():
#     print(key)
#     print(value)