"""
Given an array of integers, A of length N, find out the maximum sum sub-array of non negative 
numbers from A.
The sub-array should be contiguous i.e., a sub-array created by choosing the second and fourth
 element and skipping the third element is invalid.
Maximum sub-array is defined in terms of the sum of the elements in the sub-array.
Find and return the required subarray.
NOTE:
    1. If there is a tie, then compare with segment's length and return segment which has 
    maximum length.
    2. If there is still a tie, then return the segment with minimum starting index.

Input Format:
The first and the only argument of input contains an integer array A, of length N.

Output Format:
Return an array of integers, that is a subarray of A that satisfies the given conditions.

Constraints:
1 <= N <= 1e5
-INT_MAX < A[i] <= INT_MAX

Examples:
Input 1:
    A = [1, 2, 5, -7, 2, 3]
Output 1:
    [1, 2, 5]

Explanation 1:
    The two sub-arrays are [1, 2, 5] [2, 3].
    The answer is [1, 2, 5] as its sum is larger than [2, 3].

Input 2:
    A = [10, -1, 2, 3, -4, 100]
Output 2:
    [100]

Explanation 2:
    The three sub-arrays are [10], [2, 3], [100].
    The answer is [100] as its sum is larger than the other two.
"""

"""
Solution Approach
Loop i = 1 to Array.length :
        IF current element is positive :
                update current sum
                compare max sum with current sum
                update max sum
                update max ranges
        ELSE :
            current sum := 0
            update current ranges.
EndLoop;

return elements of max ranges
"""

import math

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        max_sum = -math.inf
        sm = 0
        x, m = 0, 0
        y, n = 0, 0
        i = 0
        
        while i < len(A):
            while i < len(A) and A[i] < 0:
                i += 1
            m = i
            sm = 0
            while i < len(A) and A[i] > -1:
                sm += A[i]
                i += 1
            n = i
            if sm > max_sum:
                max_sum = sm
                y = n
                x = m
            elif sm == max_sum and n-m > y-x:
                y = n
                x = m
        
        return A[x:y]