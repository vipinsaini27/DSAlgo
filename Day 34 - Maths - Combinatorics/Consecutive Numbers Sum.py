"""
Problem Description
Given a positive integer A.

Return the number of ways it can be written as a sum of consecutive positive integers.


Problem Constraints
1 <= A <= 109


Input Format
The first and the only argument of input contains an integer, A.


Output Format
Return an integer, representing the answer as described in the problem statement.


Example Input
Input 1:
 A = 5

Input 2:
 A = 15


Example Output
Output 1:
 2

Output 2:
 4


Example Explanation
Explanation 1:
 The 2 ways are:
 => [5]
 => [2, 3]

Explanation 2:
 The 4 ways are:
 => [15]
 => [7, 8]
 => [4, 5, 6]
 => [1, 2, 3, 4, 5]
"""

"""
Solution Approach
As in the hint, 2 * A = k(2 * x + k + 1) with x >= 0, k >= 1.

Call k the first factor, and 2 * x + k + 1 the second factor. We are looking for ways to solve this equation without trying all 2 * A possibilities.

Now notice that the parity of k and (2 * x + k + 1) are different. That is, if k is even then the other quantity is odd, and vice versa.

Also, 2 * x + k + 1 >= k + 1 > k, so the second factor must be bigger.

Now write 2*A = 2y * M, where M is odd. If we factor M = a * b, then two candidate solutions are:
1. k = a, 2x+k+1 = b * 2y
2. k = a * 2y, 2x+k+1 = b

However, only one of these solutions will have the second factor larger than the first. (Because y >= 1, we are guaranteed that one factor is strictly larger.)

Thus, the answer is the number of ways to factor the odd part of A.
"""

"""
Solution Approach
As in the hint, 2 * A = k(2 * x + k + 1) with x >= 0, k >= 1.

Call k the first factor, and 2 * x + k + 1 the second factor. We are looking for ways to solve this equation without trying all 2 * A possibilities.

Now notice that the parity of k and (2 * x + k + 1) are different. That is, if k is even then the other quantity is odd, and vice versa.

Also, 2 * x + k + 1 >= k + 1 > k, so the second factor must be bigger.

Now write 2*A = 2y * M, where M is odd. If we factor M = a * b, then two candidate solutions are:
1. k = a, 2x+k+1 = b * 2y
2. k = a * 2y, 2x+k+1 = b

However, only one of these solutions will have the second factor larger than the first. (Because y >= 1, we are guaranteed that one factor is strictly larger.)

Thus, the answer is the number of ways to factor the odd part of A.
"""

import math


class Solution:

    def solve(self, A):
        while ((A & 1) == 0):
            A = A // 2
        ans = 1
        d = 3
        while (d * d <= A):
            e = 0
            while (A % d == 0):
                A = A // d
                e += 1
            ans *= e + 1
            d += 2
        if (A > 1):
            ans = ans * 2
        return ans