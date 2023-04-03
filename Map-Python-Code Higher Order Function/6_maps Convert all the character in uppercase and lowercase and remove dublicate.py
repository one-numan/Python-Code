# Question 6
"""
Convert all the character in uppercase and lowercase and
 eliminate dublicate letter form a given squence 
 use map() fn

"""
Input = ['f','b','F','u','i','o','E','a'] 
Input=set(Input)
# Approch 1 using function

def up_low(c):
    return (c.upper(),c.lower())

output_1=list(map(up_low,Input))
print(output_1)


output_2=list(map(lambda x:(x.upper(),x.lower()), Input))
print(output_2)