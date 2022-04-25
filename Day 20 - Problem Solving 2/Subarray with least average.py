"""
Problem Description
Given an array of size N, find the subarray of size K with the least average.

Problem Constraints
1<=k<=N<=1e5
-1e5<=A[i]<=1e5

Input Format
First argument contains an array A of integers of size N.
Second argument contains integer k.

Output Format
Return the index of the first element of the subarray of size k that has least average.
Array indexing starts from 0.

Example Input
Input 1:
A=[3, 7, 90, 20, 10, 50, 40]
B=3
Input 2:
A=[3, 7, 5, 20, -10, 0, 12]
B=2

Example Output
Output 1:
3
Output 2:
4

Example Explanation
Explanation 1:
Subarray between indexes 3 and 5
The subarray {20, 10, 50} has the least average
among all subarrays of size 3.
Explanation 2:
 Subarray between [4, 5] has minimum average
"""

"""
Solution Approach
An Efficient Solution is to solve the above problem in O(n) time and O(1) extra space. The idea is to use sliding window 
of size k. Keep track of sum of current k elements. To compute sum of current window, remove first element of previous 
window and add current element (last element of current window).
1) Initialize res_index = 0 // Beginning of result index
2) Find sum of first k elements. Let this sum be 'curr_sum'
3) Initialize min_sum = sum
4) Iterate from (k+1)'th to n'th element, do following
   for every element arr[i]
      a) curr_sum = curr_sum + arr[i] - arr[i-k]
      b) If curr_sum < min_sum
           res_index = (i-k+1)
5) Print res_index and res_index+k-1 as beginning and ending
   indexes of resultant subarray.
"""

class Solution:

    def solve(self, A, B):
        sm = sum(A[0:B])
        new_sm = sum(A[0:B])
        ans = 0

        for i in range(B, len(A)):
            new_sm = (new_sm - A[i - B] + A[i])
            if sm > new_sm:
                sm = new_sm
                ans = i - B + 1

        return ans
