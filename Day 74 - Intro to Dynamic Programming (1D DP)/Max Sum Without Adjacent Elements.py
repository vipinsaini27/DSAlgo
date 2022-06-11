"""
Problem Description

Given a 2 x N grid of integer, A, choose numbers such that the sum of the numbers is maximum and no two chosen numbers are adjacent horizontally, vertically or diagonally, and return it.

Note: You can choose more than 2 numbers.



Problem Constraints

1 <= N <= 20000
1 <= A[i] <= 2000



Input Format

The first and the only argument of input contains a 2d matrix, A.



Output Format

Return an integer, representing the maximum possible sum.



Example Input

Input 1:

 A = [   
        [1]
        [2]    
     ]
Input 2:

 A = [   
        [1, 2, 3, 4]
        [2, 3, 4, 5]    
     ]


Example Output

Output 1:

 2
Output 2:

 8


Example Explanation

Explanation 1:

 We will choose 2.
Explanation 2:

 We will choose 3 and 5.
"""

"""
Solution Approach
V : 
1 |  2  |  3  | 4
2 |  3  |  4  | 5

Lets first try to reduce it into a simpler problem. 
We know that within a column, we can choose at max 1 element. 
And choosing either of those elements is going to rule out choosing anything from the previous or next column. 
This means that choosing V[0][i] or V[1][i] has identical bearing on the elements which are ruled out. 
So, instead we replace each column with a single element which is the max of V[0][i], V[1][i].

Now we have the list as : 
2 3 4 5

Here we can see that we have reduced our problem into another simpler problem.
Now we want to find maximum sum of values where no 2 values are adjacent. 
Now our recurrence relation will depend only on position i and,
 a "include_current_element" which will denote whether we picked last element or not.
  
MAX_SUM(pos, include_current_element) = 
IF include_current_element = FALSE THEN   
	max ( MAX_SUM(pos - 1, FALSE) , MAX_SUM(pos - 1, TRUE) )

ELSE
	MAX_SUM(pos - 1, FALSE) + val(pos) 
"""

class Solution:
    
    def adjacent(self, A):
        dp = [[-1]*len(A[0]), [-1]*len(A[1])]

        if len(A[0]) == 1:
            return max(A[0][0], A[1][0])
        else:
            dp[0][0] = A[0][0]
            dp[1][0] = A[1][0]
            dp[0][1] = max(A[0][0], A[0][1])
            dp[1][1] = max(A[1][0], A[1][1])

        mx = max(dp[0][0], dp[1][0])
        i = 2
        while i < len(A[0]):
            n = A[0][i] + mx
            if n > dp[0][i-1]:
                dp[0][i] = n
            else:
                dp[0][i] = dp[0][i-1]
            
            n = A[1][i] + mx
            if n > dp[1][i-1]:
                dp[1][i] = n
            else:
                dp[1][i] = dp[1][i-1]

            mx = max(dp[0][i-1], dp[1][i-1])

            i += 1

        return max(dp[0][i-1], dp[1][i-1])