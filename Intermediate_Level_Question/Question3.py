#Accenture Q2 
"""

def LargeSmallSum(arr)
The function takes an integral arr which is
of the size or length of its arguments.
Return the sum of the second smallest
element from the odd position ‘arr’ and the
largest element from the even position.


Assumption

* Every array element is unique.
* We are treating the zero position as 7th.

Note

* If the array is empty, return 0.
* If array length is 3 or <3, return 0.

Example
Input:
Arr: 3 2 1 7 5 4
Output:
7
Explanation

The second largest element from the
even position is 3.
The second largest element from the
odd position is 4.
The output is 7 (3 + 4).


Sample input:
Arr: 1 8 0 2 3 5 6
Sample output:
8

"""

def LargeSmallSum(arr):
    odd_second_smallest = arr[0]
    odd_first_smallest  = arr[0]
    o=[]
    e=[]
    [o.append(i) for i in r]

    for i in range(len(arr)):
        
        if i%2 == 0 and odd_first_smallest <= arr[i] or odd_second_smallest <= arr[i]:
            print('even',arr[i])
        else:
            print('odd',arr[i])

test_Case_1=LargeSmallSum([3,2,1,7,5,4])
