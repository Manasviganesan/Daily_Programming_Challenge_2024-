'''
You are given an integer array arr of size n. Your task is to find all the subarrays whose elements sum up to zero. A subarray is defined as a contiguous part of the array, and you must return the starting and ending indices of each subarray.

Input:
An integer array arr of size n where n represents the number of elements in the array.
Example : 
Input: [1, 2, -3, 3, -1, 2]

Output:
Return a list of tuples, where each tuple contains two integers. The starting index (0-based) of the subarray. The ending index (0-based) of the subarray.
The output should list all subarrays that sum to zero. If no such subarrays are found, return an empty list.
Example
Output: [(0, 2), (1, 3)]

'''
def find_indices(arr):
    for k in range(1,len(arr)+1):
        for i in range(0,len(arr)+1-k):
            sum=0
            for j in range(i,i+k):
                sum+=arr[j]
            if sum==0:
                zero_sum.append((i,j))

arr=eval(input())
zero_sum=[]
find_indices(arr)
print(zero_sum)