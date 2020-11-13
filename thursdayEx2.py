# Given two two-dimensional lists of numbers of the size 2x2 two dimensional list is represented as an list of lists:

# [ [2, -2],
#    [5, 3] ]
# Calculate the result of adding the two matrices. The number in each position in the resulting matrix should be the sum of the numbers in
#the corresponding addend matrices. Example: to add
# Try to loop through just the first array then build from there. 
# What I could do is just put each value in a variable then when its finished reiterate through a new array and initalize it with the new values. 
#Maybe I could just replace the numbers in the first index with the sum of the numbers from the second index. 



x = 0
y = 0

listOne =[ [ 3 , 7] , [8, 9]]
listTwo =[ [ 9, 2] , [7, 20]] 
# listThree = [ [ 3, 7] , [8, 9], [9,2], [7,20]]

# for i in range(len(listOne) )
#     for x in range(len(listTwo) )
# print(listOne[0][0])        
while x <= len(listOne[x]):
    print(x)


# while(x < 4):
#     while(y < 4):
#         listThree = listOne[[x][y]] + listTwo[[x][y]]
#         y += 1
#     y = 0    
#     x += 1
    
# print(listThree)cl