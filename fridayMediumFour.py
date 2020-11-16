longestList = ["astring"," rngongrognweo", "535y3y3y4323", "gregergn","38","bgwbgwgbwiugbwiwbigwbgwb"]

# def shortString(anyString):
#     myValue =  min(shortestList, key=len)
#     return myValue


# answer = shortString(shortestList)
# print(answer)



# def longString(myString):
#     for index in myString:
#         checkValue = myString[0]
#         if(index > checkValue):
#             checkValue = index
#     print(checkValue)

def longString(myString):
    counter = 0
    while counter < len(myString):
        checkValue = myString[0]
        if(checkValue > myString[counter]):
            checkValue = myString[counter]
        counter += 1
    return checkValue
        


answer = longString(longestList)
print(answer)
