"""
Problem Description

You are given an array A of size N consisting of integers.

You have to process Q queries of two types on it:

i x, change the i-th element of A to x.
l r, find the maximum value of (A[i]+A[i+1]…A[j]) over all pairs (i,j) such that l <= i <= j <= r.


Problem Constraints

1 <= N,Q <= 105
-1000 <= A[i] <= 1000 (for all i in [1…N])
For query of the 1st type,

1 <= i <= N
-1000 <= x <= 1000
For query of the 2nd type,

1 <= l <= r <= N


Input Format

The first argument of the input is the array A.

The second argument of the input is a 2-D array B containing the description of the queries.



Output Format

You should return an array of answers to each query of the 2nd type, in the same order they were asked in the input.



Example Input

Input 1:

A: [3, -1, 2, -9, -15]

B: [
        [2,1,4],
        [1,3,7],
        [2,5,5],
        [2,1,3]
    ]
Input 2:

A: [6, -1, 9]

B:  [
        [2,1,3],
        [1,2,10],
        [2,1,3]
    ]


Example Output

Output 1:

[4, -15, 9]
Output 2:

[14, 25]


Example Explanation

Explanation 1:

For the 1st query, the required sum is A[1] + A[2] + A[3] = 4.
After the 2nd query, array becomes [3,-1,7,-9,-15].
For the 3rd query, there is only one answer possible, -15, which is thus the answer itself.
For the 4th query, the required sum is A[1] + A[2] + A[3] = 9.
Explanation 2:

For the 1st query, the required sum is A[1] + A[2] + A[3] = 14.
After the 2nd query, array becomes [6, 10, 9].
For the 3rd query, the required sum is A[1] + A[2] + A[3] = 14.
"""

class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        pass