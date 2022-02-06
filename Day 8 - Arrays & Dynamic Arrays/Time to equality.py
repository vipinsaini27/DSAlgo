"""
Problem Description
Given an integer array A of size N. In one second you can increase the value of one element by 1.
Find the minimum time in seconds to make all elements of the array equal.


Problem Constraints
1 <= N <= 1000000
1 <= A[i] <= 1000


Input Format
First argument is an integer array A.


Output Format
Return an integer denoting the minimum time to make all elements equal.


Example Input
A = [2, 4, 1, 3, 2]


Example Output
8


Example Explanation
We can change the array A = [4, 4, 4, 4, 4]. The time required will be 8 seconds.
"""

"""
Solution Approach
Since we can only increase the element by 1. We should increase all element upto the maximum element.
We can find the maximum element and for finding the minimum number of moves we should find the summation of absolute 
difference of all 
elements with maximum element.  
"""

class Solution:

    def solve(self, A):
        ans = 0
        max_elem = max(A)

        for i in range(0, len(A)):
            ans += max_elem - A[i]

        return ans