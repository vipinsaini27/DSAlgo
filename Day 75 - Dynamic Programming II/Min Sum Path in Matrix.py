"""
Problem Description
Given a M x N grid A of integers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Return the minimum sum of the path.

NOTE: You can only move either down or right at any point in time.



Problem Constraints
1 <= M, N <= 2000

-1000 <= A[i][j] <= 1000



Input Format
First and only argument is a 2-D grid A.



Output Format
Return an integer denoting the minimum sum of the path.



Example Input
Input 1:

 A = [
       [1, 3, 2]
       [4, 3, 1]
       [5, 6, 1]
     ]
Input 2:

 A = [
       [1, -3, 2]
       [2, 5, 10]
       [5, -5, 1]
     ]


Example Output
Output 1:

 8
Output 2:

 -1


Example Explanation
Explanation 1:

 The path will be: 1 -> 3 -> 2 -> 1 -> 1.
Input 2:

 The path will be: 1 -> -3 -> 5 -> -5 -> 1.
"""

"""
Solution Approach
Let DP[i][j] store the minimum sum of numbers along the path from top left to (i,j). where 0<=i<=n-1 and 0<=j<=m-1.

Basically, DP[i][j] = A[i][j] + min(DP[i-1][j],DP[i][j-1]).

You only need to figure out the base conditions and boundary conditions now.

The answer to the problem would be simply Dp[n-1][m-1]. where n is the no. of rows and m is the no. of columns.
"""

class Solution:
    
    def minPathSum(self, A):
        dp = [[0]*len(N) for N in A]
        
        M = len(A)
        N = len(A[0])
        
        dp[0][0] = A[0][0]

        for i in range(1, N):
            dp[0][i] = dp[0][i-1] + A[0][i]

        for i in range(1, M):
            dp[i][0] = dp[i-1][0] + A[i][0]

        for i in range(1, M):
            for j in range(1, N):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + A[i][j]

        return dp[M-1][N-1]