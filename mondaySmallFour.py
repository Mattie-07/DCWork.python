# Write a letter_histogram program that asks the user for input, and 
# prints a dictionary containing the tally of how many times each letter
# in the alphabet was used in the word
# . For example:

# Please enter a word: banana
# {'a': 3, 'b': 1, 'n': 2}


# superhero["alias"] = "Princess Diana of Themyscira"
# superhero["hometown"] = "Themyscira"

# The word I use will be broken up - lets use a list and then from there I should be able 
# to create the dictionary. 

# dictionary
# user input
# counter
#breaks each word up

# wordDictionary = []
# counter = 1
# tempValue = 0

# word = input("Hi, what word would you like counted in a dictionary?\n")
# listWord = list(word)
# for i in listWord:
#     wordDictionary.append(i)

# wordDictionary[] = 1

def histogram(anyWord):
    count = {}
    for char in anyWord:
            if char not in count:
                count[char] = 1 
            else :
                count[char] +=1
    return count
print(histogram("Matthew"))









# print (wordDictionary)
# print(listWord)


