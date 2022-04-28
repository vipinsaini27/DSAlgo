"""
Problem Description
You are given an integer array A having N integers.
You have to find the minimum length subarray A[l..r] such that sorting this subarray makes the whole array sorted.

Problem Constraints
1 <= N <= 105
-109 <= A[i] <= 109

Input Format
First and only argument is an integer array A.

Output Format
Return an integer denoting the minimum length.

Example Input
Input 1:
 A = [0, 1, 15, 25, 6, 7, 30, 40, 50]
Input 2:
 A = [10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60]

Example Output
Output 1:
 4
Output 2:
 6

Example Explanation
Explanation 1:
 The smallest subarray to be sorted to make the whole array sorted =  A[3..6] i.e, subarray lying between positions 3 and 6.
Explanation 2:
 The smallest subarray to be sorted to make the whole array sorted =  A[4..9] i.e, subarray lying between positions 4 and 9.
"""

"""
Solution Approach
ALGORITHM:
1) Find the candidate unsorted subarray
a) Scan from left to right and find the first element which is greater than the next element. Let l be the index of such 
an element.
b) Scan from right to left and find the first element (first in right to left order) which is smaller than the next 
element (next in right to left order). Let r be the index of such an element.

2) Check whether sorting the candidate unsorted subarray makes the complete array sorted or not. If not, then include 
more elements in the subarray.
a) Find the minimum and maximum values in arr[l..r]. Let minimum and maximum values be min and max.
b) Find the first element (if there is any) in arr[0..l-1] which is greater than min, change l to index of this element.
c) Find the last element (if there is any) in arr[r+1..N-1] which is smaller than max, change r to index of this element.

3) The subarray A[l..r] is the solution subarray. Hence, the length returned is r - l + 1.
"""

import math

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        start_elem = math.inf
        i = 1
        while i < len(A):
            if A[i] < A[i-1] and start_elem >= A[i]:
                start_elem = A[i]
            i += 1

        if start_elem == math.inf:
            return 0

        s = 0
        while s < len(A):
            if A[s] > start_elem:
                break
            s += 1

        end_elem = -math.inf
        i = len(A)-1
        while i > 0:
            if A[i] < A[i-1] and end_elem < A[i-1]:
                end_elem = A[i-1]
            i -= 1

        e = len(A)-1
        while e > -1:
            if end_elem > A[e]:
                break
            e -= 1

        return e - s + 1