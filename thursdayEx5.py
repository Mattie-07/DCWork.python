#Change all characters in a given string / paragraph into leet speak. Dictionary below.
#A	4
# E	3
# G	6
# I	1
# O	0
# S	5
# T	7
#


longSaying = """Lorem ipsum is a pseudo-Latin text used in web design, typography, layout, and printing in plac
e of English to emphasise design elements over content. It's also called placeholder (or filler) text. It's a convenient tool for mock-ups. It helps to outline the visua
l elements of a document or presentation, eg typography, font, or layout. Lorem ipsum is mostly a part of a Latin text by the classical author and philosopher Cicero. Its words and letters have been changed by addition 
or removal, so to deliberately render its content nonsensical; it's not genuine, correct, or comprehensible Latin anymore. While lorem ipsum's still resembles classical Latin, it actually has no meaning whatsoever. As Cicero's
text doesn't contain the letters K, W, or Z, alien to latin, these, and others are often inserted randomly to mimic the typographic appearence of European languages, as are digraphs not to be found in the"""
nameList = list(longSaying) # converted the a list
leetspeak= [] # created an empty list

for string in nameList: # for 'dummy string' in listed saying, iterated through all and replace each occurance of letters with leet speak
    newStr = string.replace("a", "4")
    newStr = newStr.replace("e", "3")
    newStr = newStr.replace("g", "i")
    newStr = newStr.replace("i", "1")
    newStr = newStr.replace("o", "0")
    newStr = newStr.replace("s", "5")
    newStr = newStr.replace("t", "7")
    
            


    leetspeak.append(newStr) #adding changed to an empty list

leetspeak1 = "".join([str(item)for item in leetspeak]) # Seen on Google how str(item) was part of the code but even without it the code works the same.
print(leetspeak1)