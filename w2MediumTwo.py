def word_histogram(word):
    count = {}
    newWord = word.lower().split()
    print(newWord)
    for x in newWord:
        if x not in count:
            count[x] = 1
        else:
            count[x] += 1
    return count
print(word_histogram("To be or not to be"))