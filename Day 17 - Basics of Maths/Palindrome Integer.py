"""
Problem Description
Determine whether an integer is a palindrome. Do this without extra space.
A palindrome integer is an integer x for which reverse(x) = x where reverse(x) is x with its digit reversed. Negative
numbers are not palindromic.

Example :
Input : 12121
Output : True
Input : 123
Output : False
"""

"""
Solution Approach
Corner cases to consider:
1) Negative numbers
2) If you are thinking of converting the integer to string, note the restriction of using extra space.
3) Try reversing the integer.
"""


class Solution:

    def isPalindrome(self, A):
        if A < 0:
            return 0

        a = 1
        while A // (a * 10) > 0:
            a *= 10

        while A > 0:
            x = A // a
            y = A % 10

            if x != y:
                return 0

            A = A % a
            A = A // 10

            a = a // 100

        return 1