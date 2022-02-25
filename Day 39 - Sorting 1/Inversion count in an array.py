"""
Problem Description
Given an array of integers A. If i < j and A[i] > A[j] then the pair (i, j) is called an inversion of A. Find the total number of inversions of A modulo (109 + 7).


Problem Constraints
1 <= length of the array <= 100000
1 <= A[i] <= 10^9


Input Format
The only argument given is the integer array A.


Output Format
Return the number of inversions of A modulo (109 + 7).


Example Input
Input 1:
A = [3, 2, 1]

Input 2:
A = [1, 2, 3]


Example Output
Output 1:
3

Output 2:
0


Example Explanation
Explanation 1:
 All pairs are inversions.

Explanation 2:
 No inversions.
"""

class Solution:

    def solve(self, A):
        ans = 0
        m = 10**9 + 7
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                if A[i] > A[j]:
                    ans = (ans + 1) % m

        return ans

A = [1, 2, 3]
ans = Solution().solve(A)
print(ans)