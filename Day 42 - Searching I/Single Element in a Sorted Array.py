"""
Problem Description
Given a sorted array of integers A where every element appears twice except for one element which appears once, find and
return this single element that appears only once.
NOTE: Users are expected to solve this in O(log(N)) time.


Problem Constraints
1 <= |A| <= 100000
1 <= A[i] <= 10^9


Input Format
The only argument given is the integer array A.


Output Format
Return the single element that appears only once.


Example Input
Input 1:
A = [1, 1, 7]

Input 2:
A = [2, 3, 3]


Example Output
Output 1:
 7

Output 2:
 2


Example Explanation
Explanation 1:
 7 appears once

Explanation 2:
 2 appears once
"""

"""
Solution Approach
You need to return the index of 1 time occuring element >= x.
You can do this by binary search.
Note that this is classic binary search. Instead of looking for the element x,
you are looking for the least elements >= x.
You can do this by binary search.
Look for its implementation. There are multiple ways to do this.
Remember that index starts from 0.
"""

class Solution:

    def solve(self, A):
        L, H = 0, len(A) - 1
        while L < H:
            M = (L + H) // 2
            if A[M] == A[M+1]:
                if (H - M + 1) % 2 != 0:
                    L = M
                else:
                    H = M - 1
            else:
                if (H - M) % 2 != 0:
                    L = M + 1
                else:
                    H = M

        return A[H]