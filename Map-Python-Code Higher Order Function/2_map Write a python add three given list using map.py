# Question 2 
'''
Write a python add three given list using 
python list of intergers using Map

'''

l1=[1,2,3,4,5,6,7,8]
l2=[85,74,5,9,4,21,47,52]
l3=[8,9,6,6,6,3,4,2]

def sum(a,b,c):
    return a+b+c

# Approch 1 Using Named Function
add1=list(map(sum,l1,l2,l3))
print(add1)


# Approch 2 Using Lambda
add2=list(map(lambda x,y,z:x+y+z ,l1,l2,l3))
print(add2)


