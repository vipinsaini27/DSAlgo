"""
Problem Description
You are given a string A of size N.
Return the string A after reversing the string word by word.
NOTE:
A sequence of non-space characters constitutes a word.
Your reversed string should not contain leading or trailing spaces, even if it is present in 
the input string.
If there are multiple spaces between words, reduce them to a single space in the reversed 
string.

Problem Constraints
1 <= N <= 3 * 105

Input Format
The only argument given is string A.

Output Format
Return the string A after reversing the string word by word.

Example Input
Input 1:
    A = "the sky is blue"
Input 2:
    A = "this is ib"

Example Output
Output 1:
    "blue is sky the"
Output 2:
    "ib is this"    

Example Explanation
Explanation 1:
    We reverse the string word by word so the string becomes "the sky is blue".
Explanation 2:
    We reverse the string word by word so the string becomes "this is ib".
"""

"""
Solution Approach
One simple approach is a two-pass solution:
First pass to split the string by spaces into an array of words
Then second pass to extract the words in reversed order
We can do better in one-pass. While iterating the string in reverse order, we keep track of a 
word’s beginning and end position.
When we are at the beginning of a word, we append it.
"""

class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        A = list(A)
        i = 0
        while i < len(A) and A[i] == ' ':
            i += 1
        A = A[i:]
        
        i = len(A) - 1
        while i >= 0 and A[i] == ' ':
            i -= 1
        A = A[:i+1]

        i = 0
        while i < len(A):
            while i < len(A) and A[i] != ' ':
                i += 1
            
            j = i + 1
            while j < len(A) and A[j] == ' ':
                j += 1

            k = i + 1
            while j < len(A):
                A[k] = A[j]
                j += 1
                k += 1
            A = A[:k]
            
            i += 1
        
        i = 0
        while i < len(A) - i - 1:
            a, b = i, len(A) - i - 1
            A[a], A[b] = A[b], A[a]
            i += 1

        i = 0
        while i < len(A):
            while i < len(A) and A[i] == " ":
                i += 1

            j = i + 1
            while j < len(A) and A[j] != " ":
                j += 1
            
            k = 0
            while i+k < j-k-1:
                a, b = i+k, j-k-1
                A[a], A[b] = A[b], A[a]
                k += 1
            
            i = j

        return "".join(A)