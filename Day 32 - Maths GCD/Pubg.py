"""
Problem Description
There are N players, each with strength A[i]. when player i attack player j, player j strength 
reduces to max(0, A[j]-A[i]). When a player's strength reaches zero, it loses the game, and the 
game continues in the same manner among other players until only 1 survivor remains.
Can you tell the minimum health last surviving person can have?

Problem Constraints
1 <= N <= 100000
1 <= A[i] <= 1000000

Input Format
First and only argument of input contains a single integer array A.

Output Format
Return a single integer denoting minimum health of last person.

Example Input
Input 1:
 A = [6, 4]
Input 2:
 A = [2, 3, 4]

Example Output
Output 1:
 2
Output 2:
 1

Example Explanation
Explanation 1:

 Given strength array A = [6, 4]
 Second player attack first player, A =  [2, 4]
 First player attack second player twice. [2, 0]
Explanation 2:

 Given strength array A = [2, 3, 4]
 First player attack third player twice. [2, 3, 0]
 First player attack second player. [2, 1, 0]
 Second player attack first player twice. [0, 1, 0]
"""

"""
Solution Approach
Let’s consider if there were only 2 people with strength A and B (A<=B). then A would attack B, 
leading to A, B-A.
It would continue until it gets smaller than A or A, B%A. Then the process would repeat as 
A%(B%A), B%A, and so on…
You can see this is exactly what is done in Euclid GCD algorithm. So, the answer is always gcd 
of numbers.
"""

import math

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        ans = A[0]
        i = 1

        while i < len(A):
            ans = math.gcd(ans, A[i])
            i += 1

        return ans
    