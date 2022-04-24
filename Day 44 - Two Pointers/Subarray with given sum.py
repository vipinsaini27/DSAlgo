"""
Problem Description
Given an array of positive integers A and an integer B, find and return first continuous subarray which adds to B.
If the answer does not exist return an array with a single element "-1".
First sub-array means the sub-array for which starting index in minimum.

Problem Constraints
1 <= length of the array <= 100000
1 <= A[i] <= 109
1 <= B <= 109

Input Format
The first argument given is the integer array A.
The second argument given is integer B.

Output Format
Return the first continuous sub-array which adds to B and if the answer does not exist return an array with a single element "-1".

Example Input
Input 1:
 A = [1, 2, 3, 4, 5]
 B = 5
Input 2:
 A = [5, 10, 20, 100, 105]
 B = 110

Example Output
Output 1:
 [2, 3]
Output 2:
 -1

Example Explanation
Explanation 1:
 [2, 3] sums up to 5.
Explanation 2:
 No subarray sums up to required number.
"""

"""
Solution Approach
We can use 2 pointer technique to solve this problem efficiently.
WE can keep pointers left and right.
we move right if our sum is < target.
we move left when sum > target. using left and right, we get our subarray.
"""

class Solution:

    def solve(self, A, B):
        j, i = 0, 1
        s = sum(A[0:2])
        while i < len(A):
            if s == B:
                return A[j: i+1]
            elif s > B:
                s -= A[j]
                j += 1
            else:
                i += 1
                if i < len(A):
                    s += A[i]

        return [-1]