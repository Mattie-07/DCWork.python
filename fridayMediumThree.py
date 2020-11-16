shortestList = ["astring"," rngongrognweo", "535y3y3y4323", "gregergn","38"]

# def shortString(anyString):
#     myValue =  min(shortestList, key=len)
#     return myValue


# answer = shortString(shortestList)
# print(answer)



def shortString(myString):
    for index in myString:
        checkValue = myString[0]
        if(index < checkValue):
            checkValue = index
    print(checkValue)

shortString(shortestList)