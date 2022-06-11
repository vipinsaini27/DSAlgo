"""
Problem Description
Given two strings A and B. Find the longest common subsequence ( A sequence which does not need to be contiguous), which is common in both the strings.

You need to return the length of such longest common subsequence.



Problem Constraints
1 <= Length of A, B <= 1005



Input Format
First argument is a string A.
Second argument is a string B.



Output Format
Return an integer denoting the length of the longest common subsequence.



Example Input
Input 1:

 A = "abbcdgf"
 B = "bbadcgf"
Input 2:

 A = "aaaaaa"
 B = "ababab"


Example Output
Output 1:

 5
Output 2:

 3


Example Explanation
Explanation 1:

 The longest common subsequence is "bbcgf", which has a length of 5.
Explanation 2:

 The longest common subsequence is "aaa", which has a length of 3.
"""

"""
Solution Approach
Suppose LCS[i][j] represents the longest common subsequence of A[1..i] and B[1..j]

A[1..i] represents first i characters of string A
A[1..j] represents first j characters of string B

For every i, j we have two conditions A[i] == B[j] or not. Divide the problem based on this condition.

Recursion relation to divide the problem into smaller sub problems can be written as:-

LCS(i, j) = maximum (LCS(i-1, j-1] + 1,       //if(A[i] = B[j])
                     LCS(A[i-1], B[j],
                     LCS(A[i], B[j-1] )
LCS[ len(A) ][ len(B) ] will be our answer.

Think about the time complexity of this solution.
"""

import sys

sys.setrecursionlimit(1500*1500)

class Solution:
    def lca(self, A, B, i, j, dp):
        if i < len(A) and j < len(B):
            if dp[i][j] != -1:
                return dp[i][j]
            if A[i] == B[j]:
                dp[i][j] = self.lca(A, B, i+1, j+1, dp) + 1
            else:
                dp[i][j] = max(self.lca(A, B, i+1, j, dp), self.lca(A, B, i, j+1, dp))
        else:
            return 0
        
        return dp[i][j]
    
    def solve(self, A, B):
        dp = []
        maxLen = max(len(A), len(B))
        for i in range(0, len(A)):
            dp.append([-1]*len(B))

        self.lca(A, B, 0, 0, dp)

        return dp[0][0]