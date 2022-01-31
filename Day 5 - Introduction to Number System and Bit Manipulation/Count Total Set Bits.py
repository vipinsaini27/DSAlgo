"""
Problem Description
Given a positive integer A, the task is to count the total number of set bits in the binary representation of all the numbers from 1 to A.
Return the count modulo 109 + 7.


Problem Constraints
1 <= A <= 109


Input Format
First and only argument is an integer A.


Output Format
Return an integer denoting the ( Total number of set bits in the binary representation of all the numbers from 1 to A )modulo 109 + 7.


Example Input
Input 1:
 A = 3

Input 2:
 A = 1


Example Output
Output 1:
 4

Output 2:
 1


Example Explanation
Explanation 1:
 DECIMAL    BINARY  SET BIT COUNT
    1          01        1
    2          10        1
    3          11        2
 1 + 1 + 2 = 4
 Answer = 4 % 1000000007 = 4

Explanation 2:
 A = 1
  DECIMAL    BINARY  SET BIT COUNT
    1          01        1
 Answer = 1 % 1000000007 = 1
"""

class Solution:

    def solve(self, A):
        sm = 0
        i = 0
        N = A
        while A:
            x = 2**i
            sm += ((N // (2*x))*x) % 1000000007

            remaining = (N%(2*x))
            if (remaining+1) > x:
                sm += (remaining - x + 1) % 1000000007

            A = A >> 1
            i += 1

        return sm