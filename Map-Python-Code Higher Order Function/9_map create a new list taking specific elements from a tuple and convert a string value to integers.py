# Question 9

""" 
Write a Program to create a new list taking specific elements from a tuple and convert a string value to integers

"""

input_1=[ ('Tim','01/03/2021','35Kg'),
            ('Jim','51/03/2021','40Kg'),    
            ('John','09/08/2021','75Kg'),
            ('Fish','09/03/2021','32Kg')
        ]
print(input_1)



Name1=list(map(lambda x:x[0],input_1))

Date1=list(map(lambda x:x[1],input_1))

Weigh1=list(map(lambda x:x[2],input_1))
print(Name1,'\n',Date1,'\n',Weigh1)