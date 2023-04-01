"""
Sum of Array Using Recursion 
"""

def sumA(ar):
    if len(ar) == 1:
        return ar[0]
    else:
        return ar[-1] + sumA(ar[:-1])


# a=[12,23,34,56,78,89]
# print(a[:-1])


"""Optimization using Recursion"""

def sumArr(ar):
    return ar[0] if len(ar) == 1 else ar[-1] + sumArr(ar[:-1])

ar=[22,11,23,4]
a=sumA(ar)
print(a)
b=sumArr(ar)
print(b)