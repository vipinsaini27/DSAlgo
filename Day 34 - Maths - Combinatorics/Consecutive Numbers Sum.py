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