"""
Problem Description
Given a non-negative number represented as an array of digits, add 1 to the number ( increment the number represented by the digits ).
The digits are stored such that the most significant digit is at the head of the list.
NOTE: Certain things are intentionally left unclear in this question which you should practice asking the interviewer. For example: for this problem, following are some good questions to ask :

Q : Can the input have 0's before the most significant digit. Or in other words, is 0 1 2 3 a valid input?
A : For the purpose of this question, YES
Q : Can the output have 0's before the most significant digit? Or in other words, is 0 1 2 4 a valid output?
A : For the purpose of this question, NO. Even if the input has zeroes before the most significant digit.


Problem Constraints
1 <= size of the array <= 1000000


Input Format
First argument is an array of digits.


Output Format
Return the array of digits after adding one.


Example Input
Input 1:
[1, 2, 3]


Example Output

Output 1:
[1, 2, 4]


Example Explanation
Explanation 1:
Given vector is [1, 2, 3].
The returned vector should be [1, 2, 4] as 123 + 1 = 124.
"""

class Solution:
    
    def plusOne(self, A):
        i = len(A)-1
        carry = 1
        while i >= 0:
            if carry == 1:
                if A[i] == 9:
                    A[i] = 0
                    carry = 1
                else:
                    A[i] += carry
                    carry = 0
            else:
                break
            i -= 1
        if carry == 1:
            A.insert(0, 1)

        i = 0
        while i < len(A):
            if A[i] != 0:
                return A[i:]

            i += 1

        return A