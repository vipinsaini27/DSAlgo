"""
Problem Description
Write a program to input an integer N from user and print pascal triangle up to N rows.


Problem Constraints
1 <= N <= 25


Input Format
First line is an integer N.


Output Format
N lines whose each row contains N+1 space separated integers.


Example Input
Input 1:
3

Input 2:
5


Example Output
Output 1:
1 0 0
1 1 0
1 2 1

Output 2:
1 0 0 0 0
1 1 0 0 0
1 2 1 0 0
1 3 3 1 0
1 4 6 4 1


Example Explanation
Explanation 1:
Row 1 = 1 0 0 0 0
Row 2 = 1C0 1C1 0 0 0= 1 1 0 0 0
Row 3 = 2C0 2C1 2C2 0 0= 1 2 1 0 0
Row 4 = 3C0 3C1 3C2 3C3 0= 1 3 3 1 0
"""

"""
Solution Approach
num at position i = number at position i in prev row + number at position (i - 1) in previous row.
Now, note that to calculate num at position i, we need the numbers in previous row. Which means it makes sense to create 
rows in order.
Create a 2D matrix where Matrix[r] denotes row r.
Now process the rows starting from row number 1.
Row number 1 is obviously just 1.
For Row i, Row[i][0] = Row[i][i] = 1. And Row[i][j] = Row[i-1][j] + Row[i-1][j-1], when j belongs to [1, i)
"""

class Solution:
    # @param A : integer
    # @return a list of list of integers
    def solve(self, n):
        if n == 0:
            return []
        ans = [[0] * n for _ in range(n)]

        ans[0][0] = 1
        i = 1
        while i < n:
            j = 1
            ans[i][0] = 1
            while j < i:
                ans[i][j] = ans[i - 1][j - 1] + ans[i - 1][j]
                j += 1

            ans[i][j] = 1

            i += 1

        return ans