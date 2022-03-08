"""
Problem Description
Given a sorted array A of size N and a target value B, return the index (0-based indexing) if the target is found.
If not, return the index where it would be if it were inserted in order.
NOTE: You may assume no duplicates in the array. Users are expected to solve this in O(log(N)) time.


Problem Constraints
1 <= N <= 106


Input Format
First argument is an integer array A of size N.
Second argument is an integer B.


Output Format
Return an integer denoting the index of target value.


Example Input
Input 1:
A = [1, 3, 5, 6]
B = 5

Input 2:
A = [1]
B = 1


Example Output
Output 1:
2

Output 2:
0


Example Explanation
Explanation 1:
The target value is present at index 2.

Explanation 2:
The target value is present at index 0.
"""

"""
Solution Approach
You need to return the index of least element >= x.
You can do this by binary search.
Note that this is classic binary search. Instead of looking for the element x,
you are looking for the least elements >= x.
You can do this by binary search.
Look for its implementation. There are multiple ways to do this.
Remember that index starts from 0.
"""

class Solution:

    def searchInsert(self, A, B):
        M = 0
        L, H = 0, len(A) - 1
        while L < H:
            if A[H] < B:
                return H + 1
            elif A[L] > B:
                return L

            M = (L + H) // 2
            if A[M] == B:
                return M
            elif A[M] < B:
                L = M + 1
            else:
                H = M

        if A[M] < B:
            return M + 1

        return M
