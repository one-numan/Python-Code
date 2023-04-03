# Bubble sort  defination
"""
Repeatedly swap two adjacent element if they are in wrong order

"""
#Condition L>R (wrong order ) & needs Swap
"""
in Every Loop Iteration decrease -1 
1st iteration n-1
2nd iteration n-2
3rd iteration n-3
i th  iteration n-i

but in python n-1 b'coz using of len function

"""

'''
hdiusiu
'''
def  bubblesort(arr):
    n=len(arr)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]


arr=[12,22,12,23,332,12,33]
bubblesort(arr)
print(arr)