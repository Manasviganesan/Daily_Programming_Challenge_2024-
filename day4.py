'''You are given two sorted arrays arr1 of size m and arr2 of size n. Your task is to merge these two arrays into a single sorted array without using any extra space (i.e., in-place merging). The elements in arr1 should be merged first, followed by the elements of arr2, resulting in both arrays being sorted after the merge.

Input:
Two sorted integer arrays arr1 of size m and arr2 of size n.
Example : 
arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]

Output:
Both arr1 and arr2 should be sorted after the merge. Since you cannot use extra space, the final result will be reflected in arr1 and arr2.
Example:
arr1 = [1, 2, 3, 4]
arr2 = [5, 6, 7, 8]

Constraints:
The arrays are sorted in non-decreasing order.
You must not use any extra space beyond a few variables (O(1) space complexity).
1 ≤ m, n ≤ 10^5.
1 ≤ arr1[i], arr2[j] ≤ 10^9.
'''
def sort(arr):
    for k in range(0,len(arr)-1):
        for j in range(0,len(arr)-1-k):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

def merge_arrays(a1,a2):
    k=0
    while k<len(a2):
        elt=a2[k]
        flag=0
        for j in range(len(a1)-1,-1,-1):
            if elt>a1[-1]:
                flag=1
                break
            if elt>a1[j]:
                arr1[-1],a2[k]=a2[k],arr1[-1]
                sort(arr1)
                sort(arr2)
                break
        else:
            k+=1
        if flag==1:
            break

arr1=input().split(",")
arr2=input().split(",")
arr1=list(map(int,arr1))
arr2=list(map(int,arr2))
merge_arrays(arr1,arr2)
print(arr1,arr2)