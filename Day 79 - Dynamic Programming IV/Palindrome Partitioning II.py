"""
Problem Description
Given a string A, partition A such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of A.



Problem Constraints
1 <= length(A) <= 501



Input Format
The first and the only argument contains the string A.



Output Format
Return an integer, representing the minimum cuts needed.



Example Input
Input 1:

 A = "aba"
Input 2:

 A = "aab"


Example Output
Output 1:

 0
Output 2:

 1


Example Explanation
Explanation 1:

 "aba" is already a palindrome, so no cuts are needed.
Explanation 2:

 Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.
"""

class Solution:
    
    def minCut(self, A):
        n = len(A)
        p = [[False]*n for _ in range(n)]
        cuts = [0]*n

        for i in range(n):
            minCuts = i
            for j in range(i+1):
                if (A[i] == A[j]) and (i-j < 2 or p[j+1][i-1]):
                    p[j][i] = True
                    minCuts = min(minCuts, 0 if j == 0 else cuts[j-1]+1)
            cuts[i] = minCuts

        return cuts[-1]