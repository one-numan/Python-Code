# Question 8
''' 
Write A python program to convert a given list
of integers and tuples of integers in a list of the string

'''

# Approch 1
input_1=[1,2,3,4,5]
input_2=(1,2,3,4,4)

x=list(map(str, input_1))
y=tuple(map(str,input_2))
print(x,'\n',y)