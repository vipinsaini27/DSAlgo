"""
Problem Description
Give a N * N square matrix A, return an array of its anti-diagonals. Look at the example for more details.


Problem Constraints
1<= N <= 1000
1<= A[i][j] <= 1e9


Input Format
First argument is an integer N, denoting the size of square 2D matrix.
Second argument is a 2D array A of size N * N.


Output Format
Return a 2D integer array of size (2 * N-1) * N, representing the anti-diagonals of input array A.
The vacant spaces in the grid should be assigned to 0.


Example Input
Input 1:
3
1 2 3
4 5 6
7 8 9

Input 2:
1 2
3 4


Example Output
Output 1:
1 0 0
2 4 0
3 5 7
6 8 0
9 0 0

Output 2:
1 0
2 3
4 0


Example Explanation
For input 1:
The first anti diagonal of the matrix is [1 ], the rest spaces shoud be filled with 0 making the row as [1, 0, 0].
The second anti diagonal of the matrix is [2, 4 ], the rest spaces shoud be filled with 0 making the row as [2, 4, 0].
The third anti diagonal of the matrix is [3, 5, 7 ], the rest spaces shoud be filled with 0 making the row as [3, 5, 7].
The fourth anti diagonal of the matrix is [6, 8 ], the rest spaces shoud be filled with 0 making the row as [6, 8, 0].
The fifth anti diagonal of the matrix is [9 ], the rest spaces shoud be filled with 0 making the row as [9, 0, 0].

For input 2:
The first anti diagonal of the matrix is [1 ], the rest spaces shoud be filled with 0 making the row as [1, 0, 0].
The second anti diagonal of the matrix is [2, 4 ], the rest spaces shoud be filled with 0 making the row as [2, 4, 0].
The third anti diagonal of the matrix is [3, 0, 0 ], the rest spaces shoud be filled with 0 making the row as [3, 0, 0].
"""

"""
Solution Approach
Lets look at how the co-ordinates change when you move from one element to the other in the anti-diagonal.

With every movement, row increases by one, and the column decreases by one ( or in other words (1, -1) gets added to the 
current co-ordinates ).

Now, all we need to know is the start ( or the first element ) in each diagonal.

Can you figure out which elements qualify as the first elements in each diagonal ?
"""


class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def diagonal(self, A):
        ans = [[0] * len(A) for _ in range(0, len(A) * 2 - 1)]
        ans_c = 0
        ans_r = 0
        r = 0
        c = 0
        while c < len(A):
            i = r
            j = c
            while j >= 0:
                ans[ans_r][ans_c] = A[i][j]
                ans_c += 1
                j -= 1
                i += 1

            ans_r += 1
            ans_c = 0
            c += 1

        r += 1
        c -= 1
        while r < len(A):
            i = r
            j = c
            while i < len(A):
                ans[ans_r][ans_c] = A[i][j]
                ans_c += 1
                i += 1
                j -= 1

            ans_r += 1
            ans_c = 0
            r += 1

        return ans