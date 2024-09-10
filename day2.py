'''
You are given an array arr containing n-1 distinct integers. The array consists of integers taken from the range 1 to n, meaning one integer is missing from this sequence. Your task is to find the missing integer.

Input:
An integer array arr of size n-1 where the elements are distinct and taken from the range 1 to n.
Example : arr = [1, 2, 4, 5]

Output:
Return the missing integer from the array.
Example: Missing number: 3
'''

def missing_num(arr):
    n=len(arr)+1
    sum_theoretical=n*(n+1)//2
    sum_calculated=0
    for k in range(len(arr)):
        sum_calculated+=arr[k]
    return sum_theoretical-sum_calculated

arr=input().split(',')
arr=list(map(int,arr))
print("Missing number:",missing_num(arr))


