"""
Exponential Power(X,N)
"""

def expo(x,n):
    if n <= 0:
        return 1
    else:
        return x * expo(x,n-1)


def expon(x,n):
    return 1 if n<= 0 else x * expo(x,n-1)


print(expo(2,3))
print(expon(2,4))


