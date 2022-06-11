"""
Problem Description

You are given an array A of N integers and three integers B, C, and D.

You have to find the maximum value of A[i]*B + A[j]*C + A[k]*D, where 1 <= i <= j <= k <= N.



Problem Constraints

1 <= N <= 105

-10000 <= A[i], B, C, D <= 10000



Input Format

First argument is an array A
Second argument is an integer B
Third argument is an integer C
Fourth argument is an integer D



Output Format

Return an Integer S, i.e maximum value of (A[i] * B + A[j] * C + A[k] * D), where 1 <= i <= j <= k <= N.



Example Input

Input 1:

 A = [1, 5, -3, 4, -2]
 B = 2
 C = 1
 D = -1
Input 2:

 A = [3, 2, 1]
 B = 1
 C = -10
 D = 3


Example Output

Output 1:

 18
Output 2:

 -4


Example Explanation

Explanation 1:

 If you choose i = 2, j = 2, and k = 3 then we will get
 A[2]*B + A[2]*C + A[3]*D = 5*2 + 5*1 + (-3)*(-1) = 10 + 5 + 3 = 18
Explanation 2:

 If you choose i = 1, j = 3, and k = 3 then we will get
 A[1]*B + A[3]*C + A[3]*D = (3*1) + (-10*1) + (3*1) = 3 - 10 + 3 = -4
"""

"""
Solution Approach
Create a dynamic programming table of size n * 3. In this, dp[i][0] stores maximum of value B * A[p] for p between 1 and i. Similarly dp[i][1] stores the maximum value of B * A[p] + C * A[q] such that p <= q <= i and dp[i][2] stores maximum value of B * A[p] + C * A[q] + D * A[r] for p <= q <= r <= i.

To calculate the dp:

dp[i][0] = max(dp[i-1][0], B * A[i])

dp[i][1] = max(dp[i-1][1], dp[i][0] + C * A[i])

dp[i][2] = max(dp[i-1][2], dp[i][1] + D * A[i])

The answer will be stored in dp[n][2]
"""

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @return an integer

    def solve(self, A, B, C, D):
        dp = [[], [], []]
        dp[0].append(A[0]*B)
        dp[1].append(dp[0][-1] + A[0]*C)
        dp[2].append(dp[1][-1] + A[0]*D)

        i = 1
        while i < len(A):
            val = A[i]
            if val*B > dp[0][-1]:
                dp[0].append(val*B)
            else:
                dp[0].append(dp[0][-1])

            if (val*C + dp[0][-1]) > dp[1][-1]:
                dp[1].append(val*C + dp[0][-1])
            else:
                dp[1].append(dp[1][-1])

            if (val*D + dp[1][-1]) > dp[2][-1]:
                dp[2].append(val*D + dp[1][-1])
            else:
                dp[2].append(dp[2][-1])

            i += 1


        return dp[2][-1]