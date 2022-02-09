"""
Problem Description
Given a binary sorted matrix A of size N x N. Find the row with the maximum number of 1.
NOTE:
If two rows have the maximum number of 1 then return the row which has a lower index.
Rows are numbered from top to bottom and columns are numbered from left to right.
Assume 0-based indexing.
Assume each row to be sorted by values.
Expected time complexity is O(rows).


Problem Constraints
1 <= N <= 1000
0 <= A[i] <= 1


Input Format
The only argument given is the integer matrix A.


Output Format
Return the row with the maximum number of 1.


Example Input
Input 1:

 A = [   [0, 1, 1]
         [0, 0, 1]
         [0, 1, 1]   ]

Input 2:
 A = [   [0, 0, 0, 0]
         [0, 1, 1, 1]    ]


Example Output
Output 1:
 0

Output 2:
 1


Example Explanation
Explanation 1:
 Row 0 has maximum number of 1s.

Explanation 2:
 Row 1 has maximum number of 1s.
"""

"""
Solution Approach
You can maintain 2 variables, maxCnt and ansIdx. maxCnt stores the maximum 1s encountered in a row till now and ansIdx 
will store the index of the row at which the maxCnt was updated. For each row, just get the count of 1s in it and then 
we can update maxCnt and ansIdx according to the number of ones encountered in the row.
"""

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        ans = 0
        max_elem = 0
        for i in range(0, len(A)):
            for j in range(0, len(A[i])):
                if A[i][j] == 1:
                    if len(A[i]) - j > max_elem:
                        ans = i
                        max_elem = len(A[i]) - j
                        break

        return ans
