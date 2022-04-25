"""
Problem Description
You are given an N X N(where N = 2 or N = 3) 2D integer matrix A. You have to find the value of its determinant (det(A)
or |A|).

Problem Constraints
N = 2 or N = 3
-100 <= A[i][j] <= 100

Input Format
First and only argument is a 2D integer matrix A.

Output Format
Return an integer denoting the value of |A|.

Example Input
Input 1:
 A = [[1, 2],
      [3, 4]]
Input 2:
 A = [[6, 1, 1],
      [4, -2, 5],
      [2, 8, 7]]

Example Output
Output 1:
 -2
Output 2:
 -306

Example Explanation
Explanation 1:
 |A| = 1 * 4 - 2 * 3 = 4 - 6 = -2
Explanation 2:
 |A| = 6 * ((-2) * 7 - 5 * 8) - 1 * (4 * 7 - 5 * 2) + 1 * (4 * 8 - (-2) * 2) = -306
"""

"""
Solution Approach
You can check whether the given 2D matrix is 2X2 or 3X3, and use the formula given to calculate determinant accordingly 
by accessing the values of matrix elements..
"""

class Solution:

    def solve(self, A):
        if len(A) == 2:
            x = A[0][0] * A[1][1]
            y = A[0][1] * A[1][0]
            return x - y

        x = A[0][0] * (A[1][1] * A[2][2] - A[1][2] * A[2][1])
        y = A[0][1] * (A[1][0] * A[2][2] - A[1][2] * A[2][0])
        z = A[0][2] * (A[1][0] * A[2][1] - A[1][1] * A[2][0])
        return x - y + z
