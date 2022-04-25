"""
Problem Description
Given an array of integers A, find and return the minimum value of | A [ i ] - A [ j ] | where i != j and |x| denotes
the absolute value of x.

Problem Constraints
2 <= length of the array <= 100000
-109 <= A[i] <= 109

Input Format
The only argument given is the integer array A.

Output Format
Return the minimum value of | A[i] - A[j] |.

Example Input
Input 1:
 A = [1, 2, 3, 4, 5]
Input 2:
 A = [5, 17, 100, 11]

Example Output
Output 1:
 1
Output 2:
 6

Example Explanation
Explanation 1:
 The absolute difference between any two adjacent elements is 1, which is the minimum value.
Explanation 2:
 The minimum value is 6 (|11 - 5| or |17 - 11|).
"""

"""
Solution Approach
Sort the array.
We can observe that the answer will be the minimum value of absolute difference between the adjacent elements.
We can iterate over the sorted array and maintain the minimum value of absolute difference.
Return the answer.
"""

import math

class Solution:

    def solve(self, A):
        A.sort()
        ans = math.inf
        if len(A) == 1:
            return abs(A[0])

        for i in range(1, len(A)):
            if abs(A[i] - A[i - 1]) < ans:
                ans = abs(A[i] - A[i - 1])

        return ans