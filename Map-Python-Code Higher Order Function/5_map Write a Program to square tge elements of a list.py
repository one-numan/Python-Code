#Question 5
"""
Write a Program to square tge elements of a list
using map() function

"""

input_values = [4,5,6,8,9]

# Approch 1
output_1=list(map(lambda x:x*x, input_values))
print(output_1)


# Approch 2
def square(n):
    return n*n
output_2=list(map(square, input_values))
print(output_2)