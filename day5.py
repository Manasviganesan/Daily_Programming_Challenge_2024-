'''
Problem : Find the Leaders in an Array
You are given an integer array arr of size n. An element is considered a leader if it is greater than all the elements to its right. Your task is to find all such leader elements in the array.

Input :
An integer array arr of size n.
Example : 
arr = [16, 17, 4, 3, 5, 2]

Output :
Return an array containing all the leader elements in the order in which they appear in the original array.
Example:
Leaders: [17, 5, 2]
'''
arr=input().split(",")
arr=list(map(int,arr))
leaders=[]
if len(arr)==1:
    leaders=arr
else:
    for k in range(len(arr)):
        for j in range(k+1,len(arr)):
            if arr[k]<arr[j]:
                break
        else:
            if arr[k] not in leaders:
                leaders.append(arr[k])
print(leaders)
