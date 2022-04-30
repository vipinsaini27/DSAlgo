"""
Given a binary matrix A of integers 0 and 1, of size N x M.
Find and return the indices of the rows which are duplicate of rows which are already present in the matrix.
If row[i] and row[j] are same and i < j then answer will contain only index j.
Note: Rows are numbered from top to bottom and columns are numbered from left to right. There will be at least one
duplicate row in the matrix.

Input Format
The first argument given is the integer matrix A.

Output Format
Return the indices of the rows in the form of an integer array.

Constraints
2 <= N, M <= 1000
0 <= A[i] <= 1

For Example
Input 1:
    A = [   [1, 0, 0]
            [0, 1, 0]
            [0, 1, 0]   ]
Output 1:
    [3]

Input 2:
    A = [   [1, 1, 1, 0]
            [0, 0, 0, 1]
            [1, 1, 1, 0]
            [0, 0, 0, 1]    ]
Output 2:
    [3, 4]
"""

"""
Solution Approach
Since comparing each and every row will give TLE,
you can store the rows as string in a map. And then check if current
(row converted into string) exists in map, if yes then put row number in answer.
Else, You can use Trie data structure as well.
Insert as string in Trie and search iteratively.
"""


class Solution:

    def solve(self, A):
        ans = []
        row_hash = {}
        for i in range(0, len(A)):
            key = 0
            for j in range(0, len(A[i])):
                key += A[i][j]*2**j

            if key in row_hash.keys():
                ans.append(i+1)
            else:
                row_hash[key] = True

        return ans