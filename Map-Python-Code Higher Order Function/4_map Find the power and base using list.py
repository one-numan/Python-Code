# Question 4
"""
Create a list containing the power of said number
 in bases raised tothe correseponding 
 no. in theindex using python map()


"""
base_number=[10,20,30,40,50,60,70,80,90,100]
index_number=[1,2,3,4,5,6,7,8,9,10]

# Approch 1  Using Lamda and dual astrick Operator 

output_1 = list(map(lambda x,y: x**y ,
     base_number,index_number))
print(output_1)


# Approch 2 using pow function
output_2 = list(map(pow,base_number,index_number))
print(output_2)


# Approch 3  Using Power Variable
def power(base_number,index_number):
    return base_number**index_number

output_3 = list(map(power,base_number,index_number))
print(output_3)