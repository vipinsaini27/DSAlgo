"""
Problem Description
Print a Pattern According to The Given Value of A.

Example: For A = 3 pattern looks like:
1 0 0
1 2 0
1 2 3


Problem Constraints
1 <= A <= 1000


Input Format
First and only argument is an integer denoting A.


Output Format
Return a two-dimensional array where each row in the returned array represents a row in the pattern.


Example Input
Input 1:
 A = 3

Input 2:
 A = 4


Example Output
Output :1
 [
   [1, 0, 0]
   [1, 2, 0]
   [1, 2, 3]
 ]

Output 2:
 [
   [1, 0, 0, 0]
   [1, 2, 0, 0]
   [1, 2, 3, 0]
   [1, 2, 3, 4]
 ]


Example Explanation
Explanation 2:
 For A = 4 pattern looks like:
                             1 0 0 0
                             1 2 0 0
                             1 2 3 0
                             1 2 3 4
 So we will return it as two-dimensional array.
"""

"""
Solution Approach
Pattern contains exactly A rows.

If you assign each row of the pattern a number from 1 to A then it’s easy to find the pattern .

Suppose A = 4
Pattern :
Row-1: 1 0 0 0
Row-2: 1 2 0 0
Row-3: 1 2 3 0
Row-4: 1 2 3 4
For row i, element at (i,j) is:
1: j if j<= i.
2: else 0.
"""

class Solution:

    def solve(self, A):
        result = []
        for i in range(A):
            temp = [j for j in range(1, i + 2)]
            result.append(temp)

        return result