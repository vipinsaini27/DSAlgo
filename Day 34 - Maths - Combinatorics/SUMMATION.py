"""
Problem Description
Given an integer A.

Calculate the sum = (ACr) * (r) * (r - 1) * (2r-2) for all r from 0 to A.

Return sum % 109 + 7.


Problem Constraints
2 <= A <= 106


Input Format
The first and only argument given is the integer A.


Output Format
Return a single integer denoting sum % 109 + 7.


Example Input
Input 1:
 A = 3

Input 2:
 A = 4


Example Output
Output 1:
 18

Output 2:
 108


Example Explanation
Explaination 1:
 (ACr) * (r) * (r - 1) * (2r-2)
 r = 0, (1) * (0) * (1) * (1/4) = 0
 r = 1, (3) * (1) * (0) * (1/2) = 0
 r = 2, (3) * (2) * (1) * (1) = 6
 r = 3, (1) * (3) * (2) * (2) = 12
 sum = 18
"""

"""
Solution Approach
(1+x)A = 1 + AC1 x + AC2 x2 + AC3 x3 + …. + xA

Differentiating w.r.t x both sides we get:

A(1+x)(A-1) = AC1 + 2AC2 x + 3AC3 x2 +…. + AxA-1

Differentiating w.r.t x again both sides we get:

A(A-1)(1+x)A-2 = 2AC2 + 6 AC3 x + …. + A(A-1)xA-2

Putting x=2 we get:

A(A-1)3A-2 = 2AC2 + 12AC3+…. + A(A-1)3A-2

So the right term is what we have to find so just calculate:

A(A-1)3A-2 using modulo exponentiation and multiplication.
"""

class Solution:

    def inversePow(self, a, p, m):
        x = 1

        while p > 1:
            if p%2 == 0:
                p = p // 2
                a = (a * a) % m
            else:
                p = (p - 1) // 2
                x = x * a
                a = (a * a) % m

        return (x * a) % m

    def solve(self, A):
        p = 10**9 + 7

        return (A * (A - 1) * self.inversePow(3, A - 2, p)) % p

A = 10**6
ans = Solution().solve(A)
print(ans)
