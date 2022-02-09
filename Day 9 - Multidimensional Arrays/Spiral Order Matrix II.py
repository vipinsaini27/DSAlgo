"""
Problem Description
Given an integer A, generate a square matrix filled with elements from 1 to A2 in spiral order.


Problem Constraints
1 <= A <= 1000


Input Format
First and only argument is integer A


Output Format
Return a 2-D matrix which consists of the elements in spiral order.


Example Input
Input 1:
1

Input 2:
2


Example Output
Output 1:
[ [1] ]

Output 2:
[ [1, 2], [4, 3] ]


Example Explanation
Explanation 1:
Only 1 is to be arranged.

Explanation 2:
1 --> 2
      |
      |
4<--- 3
"""

"""
Solution Approach
This is more of a simulation problem.
You need to maintain state indicating which direction you are traversing to ( left to right, right to left, top to down, 
down to top ) and then know when to change the directions.
Note that in each direction, either row or column remains constant.
Based on the constant row or column, you can predict when to change the direction.
"""

class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generateMatrix(self, n):
        ans = [[0] * n for _ in range(n)]

        i = 1
        rs = 0
        cs = 0
        re = n - 1
        ce = n - 1
        while i <= n * n:
            j = cs
            while i <= n * n and j <= ce:
                ans[rs][j] = i
                i += 1
                j += 1

            rs += 1

            j = rs
            while i <= n * n and j <= re:
                ans[j][ce] = i
                i += 1
                j += 1

            ce -= 1

            j = ce
            while i <= n * n and j >= cs:
                ans[re][j] = i
                i += 1
                j -= 1

            re -= 1

            j = re
            while i <= n * n and j >= rs:
                ans[j][cs] = i
                i += 1
                j -= 1

            cs += 1

        return ans
