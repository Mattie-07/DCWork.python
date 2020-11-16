## any word that has repeating vowels, extend the vowels by 3 more. 

testWords = "greetandmoose"

wordsInaList = list(testWords)

print(wordsInaList)
emptyList = []


for newInstance in wordsInaList:
    wordsInaList1 = newInstance.replace("ee","7")
    print(wordsInaList1)
testWords.index