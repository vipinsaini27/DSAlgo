"""
Problem Description
Given a string A, find the longest palindromic substring in A. You may assume that the maximum length of A is 1000. If there are more than one longest palindromic substrings possible, return the leftmost substring among them.


Problem Constraints
1 <= length( A ) <= 1000


Input Format
The only argument given is string A.


Output Format
Return the longest palindromic substring in A. If there are more than one longest palindromic substrings possible, return the leftmost substring among them.


Example Input
"babad"


Example Output
"bab"


Example Explanation
"aba" is also a valid answer but "bab" is the leftmost such substring.
"""

"""
Solution Approach
Substring A[i...j] would be a palindromic substring if A[i] == A[j] and A[i+1.....j-1] is a palindromic substring
"""

class Solution:
    
    def checkEqual(self, A, idx, i):
        if idx >= 0:
            if A[idx] == A[i]:
                return True

        return False

    def solve(self, A):
        n = len(A)
        dp = [[0]*n for _ in range(n)]

        maxLen, start, end = 0, 0, 1
        for i in range(n):
            dp[i][i] = 1

        for i in range(1, n):
            if A[i] == A[i-1]:
                dp[i][i-1] = 2
                if maxLen - 1:
                    maxLen = 1
                    start = i-1
                    end = i+1
            
        for i in range(2, n):
            for j in range(i, n):
                if A[j] == A[j-i]:
                    if dp[j-1][j-i+1]:
                        dp[j][j-i] = dp[j-1][j-i+1] + 2

                        if maxLen < i:
                            maxLen = i
                            start = j-i
                            end = j+1

        return A[start: end] 