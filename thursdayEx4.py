#Make a string and remove any strings that happen to be duplicates and print that list.

name = "Matthew"

nameWithoutDups = "".join(dict.fromkeys(name))
print(nameWithoutDups)