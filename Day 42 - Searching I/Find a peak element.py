"""
Problem Description
Given an array of integers A, find and return the peak element in it. An array element is peak if it is NOT smaller than
its neighbors.
For corner elements, we need to consider only one neighbor. We ensure that answer will be unique.
NOTE: Users are expected to solve this in O(log(N)) time.


Problem Constraints
1 <= |A| <= 100000
1 <= A[i] <= 109


Input Format
The only argument given is the integer array A.


Output Format
Return the peak element.


Example Input
Input 1:
A = [1, 2, 3, 4, 5]

Input 2:
A = [5, 17, 100, 11]


Example Output
Output 1:
 5

Output 2:
 100


Example Explanation
Explanation 1:
 5 is the peak.

Explanation 2:
 100 is the peak.
"""

"""
Solution Approach
Observation: Given the condition that there is only a single peak element, We can observe that the array can be one of 3 types:
1) The whole array is decreasing with at most one pair of equal adjacent elements.
2) The whole array is non-increasing with at most one pair of equal adjacent elements.
3) The array is increasing first, then decreasing.

Note that if there are three or more adjacent elements equal to each other, then there can be more than one peak element. Hence, no three adjacent elements in the array are pairwise equal.
Also, there can be at most one pair of adjacent equal elements (i, i+1), and if they exist, one of these elements must be a peak element.

You need to find the index of the peak element.

Let us apply binary search on the index. Note that this is a classic binary search.
ALGORITHM:
1) Initially let l = 0 and r = A.size()-1
2) Repeat steps 3-4 while l<=r
3) Set m=(l+r)/2
4) If A[m] >= A[m-1] and A[m] >= A[m+1], A[m] is the peak element. Set ans = A[m] and exit the loop
Else if A[m] > A[m-1] we know that the peak element has to be on the right side of A[m]. Hence, we set l =m+1
Else if A[m] < A[m-1] we know that the peak element has to be on the left side of A[m]. Hence, we set r=m-1.
5) Return ans
Take extra care of edge cases, where the first or last element is the peak element.
Look for its implementation. There are multiple ways to do this.
Remember that the index starts from 0.
"""

class Solution:

    def solve(self, A):
        if len(A) == 1:
            return A[0]
        elif len(A) == 2:
            return max(A)

        l = len(A) - 1
        L, H = 0, l
        M = 0
        while L <= H:
            M = (L + H) // 2
            if M == 0 or M == l:
                return A[M]

            if A[M] > A[M - 1] and A[M] > A[M + 1]:
                return A[M]
            elif A[M] < A[M - 1] and A[M] < A[M + 1]:
                if A[M + 1] >= A[M - 1]:
                    L = M + 1
                else:
                    H = M
            elif A[M + 1] >= A[M]:
                L = M + 1
            else:
                H = M

        return A[M]