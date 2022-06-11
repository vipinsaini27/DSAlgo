"""
Problem Description
You are given an array A. You need to find the length of the Longest Increasing Subsequence in the array.

In other words, you need to find a subsequence of array A in which the elements are in sorted order, (strictly increasing) and as long as possible.



Problem Constraints
1 ≤ length(A), A[i] ≤ 105



Input Format
The first and only argument of the input is the array A.



Output Format
Output a single integer, the length of the longest increasing subsequence in array A.



Example Input
Input 1:

A: [2, 1, 4, 3]
Input 2:

A: [5, 6, 3, 7, 9]


Example Output
Output 1:

2
Output 2:

4


Example Explanation
Explanation 1:

 [2, 4] and [1, 3] are the longest increasing sequences of size 2. 
Explanation 2:

The longest increasing subsequence we can get is [5, 6, 7, 9] of size 4.
"""

"""
Solution Approach
Approach 1:
Let LIS[i] be the longest increasing subsequence of the array A[1..i] ending at A[i].
Now, consider the second last element of this subsequence, it should be smaller than A[i] and should lie to the left of i.
So, we can get a recurrence relation as follows:
LIS[i] = 1 + max(LIS[j]), over all j<i, such that A[j] < A[i]. 
This is not fast enough to pass. We can speed it up using segment trees.
We will maintain the segment tree from left to right, hence we do not need to worry about the condition j<i.
If we build segment tree on the values A[i], instead of i, the recurrence becomes:
LIS[A[i]] = 1 + max(LIS[A[j]]), over all j<i, such that A[j] < A[i]. 
Now, we can simply query the segment tree from 1 to A[i]-1 and take the maximum value. This way transition takes O(logN) time.
When we move from index i to i+1, we update the segment tree at A[i] for further queries.
Final answer would be max(LIS[A[i]]) over all i from 1 to N.

Approach 2:
Let dp[i] be the smallest element at which a subsequence of length i terminates.
Initially we assume d[0] = −inf and for all other elements d[i] = inf.
We will again gradually process the numbers, first a[0], then a[1], etc, and in each step maintain the array d[] so that it is up to date.
We now make two important observations.
The array d will always be sorted: d[i−1] ≤ d[i] for all i= 1 … n.
And also the element a[i] will only update at most one value d[j].
Thus we can find this element in the array d[] using binary search in O(logn).
In fact we are simply looking in the array d[] for the first number that is strictly greater than a[i], and we try to update this element.
After processing all the elements of a[] the length of the desired subsequence is the largest l with d[l] < inf.
"""

import sys

sys.setrecursionlimit(10**5)

class Solution:
    # @param A : list of integers
    # @return an integer
    
    def findCeil(self, A, dp, l, r, key):
        while r - l > 1:
            m = l + (r - l)//2
            if A[dp[m]] >= key:
                r = m
            else:
                l = m

        return r
    
    def findLIS(self, A):
        dp = [0]
        i = 1
        while i < len(A):
            if A[i] > A[dp[-1]]:
                dp.append(i)
            elif A[i] < A[dp[0]]:
                dp[0] = i
            else:
                idx = self.findCeil(A, dp, -1, len(dp)-1, A[i])
                dp[idx] = i
            i += 1

        return len(dp)   
