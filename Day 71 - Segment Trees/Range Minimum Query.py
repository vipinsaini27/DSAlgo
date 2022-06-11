"""
Problem Description

Given an integer array A of size N.

You have to perform two types of query, in each query you are given three integers x,y,z.

If x = 0, then update A[y] = z.
If x = 1, then output the minimum element in the array A between index y and z inclusive.
Queries are denoted by a 2-D array B of size M x 3 where B[i][0] denotes x, B[i][1] denotes y, B[i][2] denotes z.



Problem Constraints

1 <= N, M <= 105

1 <= A[i] <= 109

If x = 0, 1<= y <= N and 1 <= z <= 109

If x = 1, 1<= y <= z <= N



Input Format

First argument is an integer array A of size N.

Second argument is a 2-D array B of size M x 3 denoting queries.



Output Format

Return an integer array denoting the output of each query where value of x is 1.



Example Input

Input 1:

 A = [1, 4, 1]
 B = [ 
        [1, 1, 3]
        [0, 1, 5]
        [1, 1, 2] 
     ]
Input 2:

 A = [5, 4, 5, 7]
 B = [ 
        [1, 2, 4]
        [0, 1, 2]
        [1, 1, 4]
     ]


Example Output

Output 1:

 [1, 4]
Output 2:

 [4, 2]


Example Explanation

Explanation 1:

 For 1st query, the minimum element from range (1, 3) is 1.
 For 2nd query, update A[1] = 5, now A = [5, 4, 1].
 For 3rd query, the minimum element from range (1, 2) is 4.
Explanation 2:

 For 1st query, the minimum element from range (2, 4) is 4.
 For 2nd query, update A[1] = 2, now A = [2, 4, 5, 7].
 For 3rd query, the minimum element from range (1, 4) is 2.
"""

class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        pass