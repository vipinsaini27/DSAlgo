"""
Problem Description
Given an integer array A of size N. Find the contiguous subarray within the given array (containing at least one number) which has the largest product.

Return an integer corresponding to the maximum product possible.

NOTE: Answer will fit in 32-bit integer value.



Problem Constraints
1 <= N <= 5 * 105

-100 <= A[i] <= 100



Input Format
First and only argument is an integer array A.



Output Format
Return an integer corresponding to the maximum product possible.



Example Input
Input 1:

 A = [4, 2, -5, 1]
Input 2:

 A = [-3, 0, -5, 0]


Example Output
Output 1:

 8
Output 2:

 0


Example Explanation
Explanation 1:

 We can choose the subarray [4, 2] such that the maximum product is 8.
Explanation 2:

 0 will be the maximum product possible.
"""

"""
Solution Approach
If there were no zeros or negative numbers, then the answer would definitely be the product of the whole array.

Now lets assume there were no negative numbers and just positive numbers and 0. In that case we could maintain a current maximum product which would be reset to A[i] when 0s were encountered.
When the negative numbers are introduced, the situation changes ever so slightly. We need to now maintain the maximum product in positive and maximum product in negative. On encountering a negative number, the maximum product in negative can quickly come into picture.
"""

class Solution:
    
    def maxProduct(self, A):
        dp_max = [A[0]]
        dp_min = [A[0]]

        i = 1
        while i < len(A):
            val = A[i]
            mx = max(dp_max[-1]*val, dp_min[-1]*val, val)     
            mn = min(dp_max[-1]*val, dp_min[-1]*val, val)
            dp_max.append(mx)
            dp_min.append(mn)

            i += 1

        return max(dp_max)