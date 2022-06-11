"""
Problem Description
Given a grid of size n * m, lets assume you are starting at (1,1) and your goal is to reach (n, m). At any instance, if you are on (x, y), you can either go to (x, y + 1) or (x + 1, y).

Now consider if some obstacles are added to the grids. How many unique paths would there be? An obstacle and empty space is marked as 1 and 0 respectively in the grid.



Problem Constraints
1 <= n, m <= 100
A[i][j] = 0 or 1



Input Format
Firts and only argument A is a 2D array of size n * m.



Output Format
Return an integer denoting the number of unique paths from (1, 1) to (n, m).



Example Input
Input 1:

 A = [
        [0, 0, 0]
        [0, 1, 0]
        [0, 0, 0]
     ]
Input 2:

 A = [
        [0, 0, 0]
        [1, 1, 1]
        [0, 0, 0]
     ]


Example Output
Output 1:

 2
Output 2:

 0


Example Explanation
Explanation 1:

 Possible paths to reach (n, m): {(1, 1), (1, 2), (1, 3), (2, 3), (3, 3)} and {(1 ,1), (2, 1), (3, 1), (3, 2), (3, 3)}  
 So, the total number of unique paths is 2. 
Explanation 2:

 It is not possible to reach (n, m) from (1, 1). So, ans is 0.
"""

"""
Solution Approach
Suppose dp[i][j] represents the number of unique paths to reach (i, j).

If you look at a cell, there are atmost 2 ways to reach it. From the cell left and up.

If the cell does not have an obstacle, then the number of ways to reach this cell would be the summation of the number of ways to reach the immediate neighbors preceding it ( left and up ).

So, dp[i][j] = dp[i-1][j] + dp[i][j-1] if (i-1, j) and (i, j-1) doesn’t have obstacles.
= dp[i-1][j] if only (i-1, j) doesn’t have obstacle
= dp[i][j-1] if only (i, j-1) doesn’t have obstacle
= 0 otherwise

dp[n][m] will be our answer.
"""

import sys

sys.setrecursionlimit(100*100)

class Solution:
    
    def minSteps(self, A, n, m, i, j, dp):
        if i < n and j < m:
            if dp[i][j] == -1:
                if A[i][j] == 1:
                    return 0
                if i == n-1 and j == m-1:
                    return 1
                bStep = self.minSteps(A, n, m, i+1, j, dp)
                fStep = self.minSteps(A, n, m, i, j+1, dp)
                dp[i][j] = bStep + fStep
        else:
            return 0

        return dp[i][j]
        
    def uniquePathsWithObstacles(self, A):
        n = len(A)
        m = len(A[0])
        dp = [[-1]*m for _ in range(n)]

        ans = self.minSteps(A, n, m, 0, 0, dp)

        return ans