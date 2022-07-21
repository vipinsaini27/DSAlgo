"""
Problem Description
Given a tree with N nodes labeled from 1 to N.

Each node has a certain weight assigned to it given by an integer array A of size N.

Your task is to find the maximum difference in weights of two nodes where one node is a descendant of the other.

NOTE:

The tree is rooted at node labeled with 1.


Problem Constraints
2 <= N <= 105

-103 <= A[i] <= 103



Input Format
First argument is an integer array A of size N denoting the weight of each node.

Second argument is a 2-D array B of size (N-1) x 2 denoting the edge of the tree.



Output Format
Return an single integer denoting the maximum difference in weights of two nodes where one node is a descendant of the other.



Example Input
Input 1:

 A = [10, 5, 12, 6]
 B = [  [1, 2]
        [1, 4]
        [4, 3]
     ]
Input 2:

 A = [11, 12]
 B = [  [1, 2]
     ]


Example Output
Output 1:

 6
Output 2:

 1


Example Explanation
Explanation 1:

 The maximum difference occurs between the 3rd and 4th nodes. A[3] − A[4] = 12 - 6 = 6 .
Explanation 2:

 The maximum difference occurs between the 2nd and 1st nodes. A[2] − A[1] = 12 - 11 = 1 .
"""

class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        pass