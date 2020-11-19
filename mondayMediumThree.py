#break the dictionary up by the freqency

def word_histogram(word):
    count = {}
    newWord = word.split()
    for x in newWord:
        if x not in count:
            count[x] = 1
        else:
            count[x] += 1
    for keys, values in count:
        newList = count[values]
        print(newList)
        
    return count


print(word_histogram("To be or not to be"))