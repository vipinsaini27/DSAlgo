"""
Problem Description
Print a Pattern According to The Given Value of A.
Example: For A = 3 pattern looks like:
    1
  2 1
3 2 1


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
   [0, 0, 1]
   [0, 2, 1]
   [3, 2, 1]
 ]

Output 2:
 [
   [0, 0, 0, 1]
   [0, 0, 2, 1]
   [0, 3, 2, 1]
   [4, 3, 2, 1]
 ]


Example Explanation
Explanation 2:
 For A = 4 pattern looks like:
                                   1
                                 2 1
                               3 2 1
                             4 3 2 1
 So we will return it as two-dimensional array.
 Row 1 contains 3 spaces and 1 integer so spaces will be considered as 0 in the output.
"""

"""
Solution Approach
Pattern contains exactly A rows.

If you assign each row of the pattern a number from 1 to A then it’s easy to find the pattern .

Suppose A = 4
Pattern :
Row-1: 0 0 0 1
Row-2: 0 0 2 1
Row-3: 0 3 2 1
Row-3: 4 3 2 1

As,
Row-1 contains one number from [1,1] and A-1 zeroess.
Row-2 contains two numbers from [2,1] and A-2 zeroes.
Row-3 contains three numbers from [3,1] and A-3 zeroes
Row-4 contains four numbers from [4,1] and A-4 zeroes.
"""

class Solution:

    def solve(self, A):
        ans = []
        i = 1
        while i <= A:
            ans.append([])
            spaces = A - i
            while spaces > 0:
                ans[i-1].append(0)
                spaces -= 1

            j = i
            while j > 0:
                ans[i-1].append(j)
                j -= 1

            i += 1

        return ans