# 2021
"""
def differenceofSum(n.m)
The function takes two integrals m and n
as arguments. You are required to obtain
the total of all integers ranging between 1
to n (both inclusive) which are not divisible
by m. You must also return the distinction
between the sum of integers not divisible
by m with the sum of integers divisible by
m.



Assumption 
* m > 0 and n > 0
* Sum Lies Within the integral Range

Example :
Input :
m = 6
n = 30

Output :
285


* Integers Divisible by 6 , 12 , 18 , 24 and 30 . Their Sum is 90

Integers that are not divisible by 6 are 1,
2, 3, 4, 5, 7, 8, 9, 10, 11, 13, 14, 15, 16,
17, 19, 20, 21, 22, 23, 25, 26, 27, 28,
and 29. Their sum is 375.
The difference between them is 285 (375-90).

Sample output:
19
"""

def differenceofSum(n,m):
    sum_divisible = 0 
    sum_not_divisible = 0
    for i in range(1,n+1):
        if (i % m == 0):
            sum_divisible += i
        else:
            sum_not_divisible += i
    
    print("Sum_divisible : ",sum_divisible)
    print("Sum_not_divisible : ",sum_not_divisible)
    print("Difference Between them  : ",sum_not_divisible-sum_divisible)

test_Case_1=differenceofSum(m=6,n=30)
test_Case_2=differenceofSum(m=3,n=10)


