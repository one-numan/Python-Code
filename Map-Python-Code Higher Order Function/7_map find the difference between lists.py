#Question 7

"""
Write a python program to add two given list
and find the difference between lists. use map() function.


"""

#Approch 1 Using Lmbda Function

a=[6,5,3,9]
b=[0,1,7,7]

output_1=list(map(lambda x,y:(x+y,x-y),a,b))
print(output_1)