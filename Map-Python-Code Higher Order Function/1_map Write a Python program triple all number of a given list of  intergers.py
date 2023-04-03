# Question
"""
Write a Python program triple all number of
a given list of  intergers


map(function,iterator)
"""
import timeit 

intergers=[1,2,3,4,5,6,7]
def sq(n)-> int:
    return n*n


#Approch 1  Using Function
sq_list=list(map(sq,intergers))
# print(sq_list)


#Approch 2 Using Lambda
sq_list2=list(map(lambda x:x*x,intergers))
print("Second List :",sq_list2)