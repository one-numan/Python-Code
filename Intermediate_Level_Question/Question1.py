""" QUESTION 36 Write a Program for the following
input--> a3b2c4
output--> aaabbcccc
"""
# Traditional python Approach 
a='a3b2c4'
print("\n\n\n\n")
for i in range(len(a)):
    if i%2==0:
        print(a[i]*int(a[i+1]),end="")
print("\n\n\n\n")

