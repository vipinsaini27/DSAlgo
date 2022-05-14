"""
Problem Description
Given a 2D Matrix A of dimensions N*N, we need to return the sum of all possible submatrices.

Problem Constraints
1 <= N <=30
0 <= A[i][j] <= 10

Input Format
Single argument representing a 2-D array A of size N x N.

Output Format
Return an integer denoting the sum of all possible submatrices in the given matrix.

Example Input
A = [ [1, 1]
      [1, 1] ]

Example Output
16

Example Explanation
Number of submatrices with 1 elements = 4, so sum of all such submatrices = 4 * 1 = 4
Number of submatrices with 2 elements = 4, so sum of all such submatrices = 4 * 2 = 8
Number of submatrices with 3 elements = 0
Number of submatrices with 4 elements = 1, so sum of such submatrix = 4
Total Sum = 4+8+4 = 16
"""

"""
Solution Approach
Let us suppose the index of an element be (X, Y) in 0 based indexing, then the number of 
submatrices Sub(x,y) for this element
can be given by the formula Sub(x, y) = (X + 1) * (Y + 1) * (N – X) * (N – Y) .
This formula works because we just have to choose two different positions on the matrix that 
will create a submatrix that
envelopes the element. Thus, for each element, ‘sum’ can be updated as sum += Sub(x,y) * 
A[x][y].
More Formally,
Number of ways to choose from top-left elements (X + 1) * (Y + 1)
Number of ways to choose from bottom-right elements (N - X) * (N - Y)
"""

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        A.insert(0, [0]*n)
        for i in range(n+1):
            A[i].insert(0, 0)
        n = n+1

        sumMat = [[0]*(n) for _ in range(n)]
        for i in range(1, n):
            for j in range(1, n):
                sumMat[i][j] = A[i][j] + sumMat[i-1][j] + sumMat[i][j-1] - sumMat[i-1][j-1]

        ans = 0
        for i in range(1, n):
            for j in range(1, n):
                for x in range(1, i+1):
                    for y in range(1, j+1):
                        ans += sumMat[i][j] - sumMat[i][y-1] - sumMat[x-1][j] + sumMat[x-1][y-1]

        return ans