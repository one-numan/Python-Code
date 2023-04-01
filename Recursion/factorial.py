"""
Calculating Factorial Using Recursion

"""

def factorial(n):
    try:
        if n==1 or  n==0:
            return 1
        else:
            return n * factorial(n-1)
    except RecursionError as re:
        print("Recusrion Error",re)
    except ValueError as ve:
        print("Value Error ",ve)
    except TypeError as te:
        print("Type Error ",te)
a=int(input("Enter the Number"))
b=factorial(a)
print(b)