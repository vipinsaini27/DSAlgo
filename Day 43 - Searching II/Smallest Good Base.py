"""
Given an integer A, we call k >= 2 a good base of A, if all digits of A base k are 1. Now given a string representing A,
you should return the smallest good base of A in string format.


Input Format
The only argument given is the string representing A.

Output Format
Return the smallest good base of A in string format.


Constraints
3 <= A <= 10^18


For Example
Input 1:
    A = "13"
Output 1:
    "3"     (13 in base 3 is 111)

Input 2:
    A = "4681"
Output 2:
    "8"     (4681 in base 8 is 11111).
"""

import math

class Solution:

    def solve(self, A):
        A = int(A)
        ans = A - 1

        for i in range(2, 65):
            l, h = 2, A - 1
            while l <= h:
                m = (l + h) // 2
                s = (m**i - 1) // (m - 1)
                if s == A:
                    ans = min(ans, m)
                    break
                elif s > A:
                    h = m - 1
                else:
                    l = m + 1

        return str(ans)


A = "1000000000000000000"
ans = Solution().solve(A)
print(ans)