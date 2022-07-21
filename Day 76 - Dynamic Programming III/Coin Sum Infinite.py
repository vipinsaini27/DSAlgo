"""
Problem Description
You are given a set of coins A. In how many ways can you make sum B assuming you have infinite amount of each coin in the set.

NOTE:

Coins in set A will be unique. Expected space complexity of this problem is O(B).
The answer can overflow. So, return the answer % (106 + 7).


Problem Constraints
1 <= A <= 500
1 <= A[i] <= 1000
1 <= B <= 50000



Input Format
First argument is an integer array A representing the set.
Second argument is an integer B.



Output Format
Return an integer denoting the number of ways.



Example Input
Input 1:

 A = [1, 2, 3]
 B = 4
Input 2:

 A = [10]
 B = 10


Example Output
Output 1:

 4
Output 2:

 1


Example Explanation
Explanation 1:

 The 4 possible ways are:
 {1, 1, 1, 1}
 {1, 1, 2}
 {2, 2}
 {1, 3} 
Explanation 2:

 There is only 1 way to make sum 10.
"""

"""
Solution Approach
Let’s suppose dp[i] denotes the number of ways to make sum i.

Assume we have calculated all the value of dp[k] for k < i.
To calculate dp[i], if the coin we are considering is A[j] then the number of ways is simply is dp[i-A[j]].

Base Case: dp[0] = 1 as sum 0 can be made without taking any coins.

Algorithm:

Run a loop on the coins 
    For each coin c_i, loop over all sum s_j from 0 to B:
        For each s_j dp[s_j] += dp[s_j - c_i]
dp[B] will be our answer. Remember to take modulo 1000007.
"""

class Solution:
    
    def coinchange2(self, A, B):
        dp = [0 for _ in range(B+1)]
        dp[0] = 1

        for coin in A:
            for i in range(coin, B+1):
                dp[i] = (dp[i] + dp[i-coin]) % (10**6 + 7)

        return dp[B]