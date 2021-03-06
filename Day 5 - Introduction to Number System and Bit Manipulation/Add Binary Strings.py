"""
Problem Description
Given two binary strings, return their sum (also a binary string).
Example:

a = "100"

b = "11"
Return a + b = "111".
"""

"""
Solution Approach
Since sizes of two strings may be different, we first make the size of smaller string equal to that of bigger string by adding leading 0s for simplicity
Note that you can handle the addition without adding zeroes as well by adding a few if statements.
After making sizes same, one by one, we add bits from rightmost bit to leftmost bit.
In every iteration, we need to sum 3 bits: 2 bits of 2 given strings and carry.

The sum bit will be 1 if, either all of the 3 bits are set or one of them is set.
So we can add all the bits and then take remainder with 2 to get the current bit in the answer.

How to find carry?

Carry will be 1 if any of the two bits is set. So we can find carry by adding the bits and dividing the result by 2.

Following is a step by step algorithm:

Make them equal sized by adding 0s at the begining of smaller string.

Perform bit addition

Boolean expression for adding 3 bits a, b, c

Sum = (a + b + c) % 2
Carry = (a + b + c ) / 2
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
