'''
You are given a string s that consists of multiple words separated by spaces. Your task is to reverse the order of the words in the string. Words are defined as sequences of non-space characters. The output string should not contain leading or trailing spaces, and multiple spaces between words should be reduced to a single space.

Input:
A string s of length n (1 ≤ n ≤ 10^4) consisting of letters, digits, punctuation, and spaces.

Output:
A string where the words in s are reversed, with a single space separating the words, and no leading or trailing spaces.

Examples:
Example 1
Input: "the sky is blue"
Output: "blue is sky the"
Explanation: The input string has leading and trailing spaces, which are removed in the output, and the words are reversed.
Example 2
Input: "  hello world  "
Output: "world hello"
Explanation: The input string has leading and trailing spaces, which are removed in the output, and the words are reversed.
Example 3
Input: "a good   example"
Output: "example good a"
Explanation: The input string contains multiple spaces between the words. These are reduced to a single space, and the words are reversed in the output.

'''
def reverse_string(a):
    word=''
    for k in range(len(s)):
        if s[k]==" ":
            if word:
                words.append(word)
                word=''
            else:
                pass
        else:
            word+=s[k]
    if s[-1]!=" ":
        words.append(word)
    if not words:
        print('')
    else:
        for k in range(len(words)-1,-1,-1):
            print(words[k],end=" ")

s=input()
words=[]
reverse_string(s)