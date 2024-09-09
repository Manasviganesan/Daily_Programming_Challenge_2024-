'''Problem: Sort an Array of 0s, 1s, and 2s
You are given an array arr consisting only of 0s, 1s, and 2s. The task is to sort the array in increasing order in linear time (i.e., O(n))
without using any extra space. This means you need to rearrange the array in-place.

Input :
An integer array arr of size n where each element is either 0, 1, or 2.
Example : arr = [0, 1, 2, 1, 0, 2, 1, 0]

Output :
The sorted array, arranged in increasing order of 0s, 1s, and 2s.
Example: [0, 0, 0, 1, 1, 1, 2, 2]
'''
arr=input().split(',')
arr=list(map(int,arr))

insert_at=0
for k in range(len(arr)):
    if arr[k]==0:
        arr[k],arr[insert_at]=arr[insert_at],arr[k]
        insert_at+=1
for k in range(len(arr)):
    if arr[k]==1:
        arr[k],arr[insert_at]=arr[insert_at],arr[k]
        insert_at+=1
print(arr)