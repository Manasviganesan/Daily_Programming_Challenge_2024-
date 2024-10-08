'''
You are given an array of strings strs[], consisting of lowercase letters. Your task is to find the longest common prefix shared among all the strings. If there is no common prefix, return an empty string "".
A common prefix is a substring that appears at the beginning of all the strings in the array. The task is to identify the longest such prefix that all strings share.

Input:
An array of strings strs[] where each string consists of lowercase English letters.

Output:
A string representing the longest common prefix. If no common prefix exists, return an empty string "".

Examples:
Example 1
Input: strs[] = ["flower", "flow", "flight"]
Output: "fl"
Explanation: The longest common prefix among the strings "flower", "flow", and "flight" is "fl".
Example 2
Input: strs[] = ["dog", "racecar", "car"]
Output: ""
Explanation: There is no common prefix among the strings "dog", "racecar", and "car", so the output is an empty string.

Constraints:
1 ≤ strs.length ≤ 200 (The array can contain up to 200 strings)
0 ≤ strs[i].length ≤ 200 (Each string can be up to 200 characters long)
All strings in strs[] consist of lowercase English letters.

Test Cases:
Input: strs[] = ["flower", "flow", "flight"]
Output: 
Input: strs[] = ["dog", "racecar", "car"]
Output: ""
Input: strs[] = ["apple", "ape", "april"]
Output: "ap"
Input: strs[] = [""]
Output: “”
Input: strs[] = ["alone"]
Output: "alone"

Edge Cases:
Empty array: If the array is empty, the output should be an empty string.
Single string: If the array contains only one string, the output should be the string itself.
No common prefix: If the strings have no common prefix, return an empty string.

'''
def maximum_prefix(strs):
    if len(strs)==0:
        return ''
    elif len(strs)==1:
        return strs[0]
    else:
        for k in range(len(strs)-1):
            for j in range(len(strs)-1-k):
                if len(strs[j])>len(strs[j+1]):
                    strs[j],strs[j+1]=strs[j+1],strs[j]
        prefix=''
        for k in range(len(strs)-1):
            pointer=0
            while pointer<len(strs[k]):
                if strs[k][pointer]==strs[k+1][pointer]:
                    pointer+=1
                    continue
                else:
                    break
        prefix=strs[0][:pointer]
        return prefix

strs=input().split()
print(maximum_prefix(strs))