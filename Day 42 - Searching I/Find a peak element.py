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

class Solution:

    def solve(self, A):
        l = len(A) - 1
        L, H = 0, l
        M = 0
        while L <= H:
            M = (L + H) // 2
            if M == 0 or M == l:
                return A[M]

            if A[M] > A[M-1] and A[M] > A[M+1]:
                return A[M]
            elif A[M] < A[M-1] and A[M] < A[M+1]:
                if A[M+1] >= A[M-1]:
                    L = M+1
                else:
                    H = M
            elif A[M+1] > A[M]:
                L = M+1
            else:
                H = M

        return A[M]


A = [10, 20, 15, 2, 23, 90, 67]
ans = Solution().solve(A)
print(ans)