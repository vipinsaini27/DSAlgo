"""
Problem Description
Given two binary strings, return their sum (also a binary string).
Example:

a = "100"

b = "11"
Return a + b = "111".
"""

class Solution:

    def addBinary(self, A, B):
        out = ''
        A_idx = len(A) - 1
        B_idx = len(B) - 1
        carry, next_carry = '0', '0'
        while A_idx >= 0 or B_idx >= 0:
            x = A[A_idx] if A_idx >= 0 else '0'
            y = B[B_idx] if B_idx >= 0 else '0'

            if x == '1' and y == '1':
                result = '0'
                next_carry = '1'
            elif (x == '1' and y == '0') or (x == '0' and y == '1'):
                result = '1'
                next_carry = '0'
            else:
                result = '0'
                next_carry = '0'

            if result == '1' and carry == '1':
                result = '0'
                next_carry = '1'
            elif (result == '1' and carry == '0') or (result == '0' and carry == '1'):
                result = '1'
            else:
                result = '0'

            out = result + out
            carry = next_carry

            A_idx -= 1
            B_idx -= 1

        if carry == '1':
            out = carry + out

        return out
