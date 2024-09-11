'''
You are given an array arr containing n+1 integers, where each integer is in the range [1, n] inclusive. There is exactly one duplicate number in the array, but it may appear more than once. Your task is to find the duplicate number without modifying the array and using constant extra space.

Input:
An integer array arr of size n+1, where each element is an integer in the range [1, n].
Example : arr = [3, 1, 3, 4, 2]

Output:
Return the duplicate integer present in the array.
Example: Duplicate number: 3

Constraints:
1 ≤ n ≤ 10^5.
There is only one duplicate number, but it may appear more than once.
You must not modify the array (arr) or use extra space greater than O(1).
The time complexity must be O(n).
'''
def find_duplicate(arr):
    slow=0
    fast=0
    while True:
        slow=arr[slow]
        fast=arr[arr[fast]]
        if slow==fast:
            break
    slow1=0
    while True:
        slow=arr[slow]
        slow1=arr[slow1]
        if slow==slow1:
            return slow
arr=input().split(",")
arr=list(map(int,arr))
print(find_duplicate(arr))