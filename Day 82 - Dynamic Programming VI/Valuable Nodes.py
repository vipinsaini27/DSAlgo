"""
Problem Description

Given a tree T containing N nodes numbered [1,2, …, N] rooted at node 1.

Each node has a value associated with it. You need to choose some of the nodes from the tree such that the sum of values of the chosen nodes is maximum possible.

Moreover, if you have chosen a node V you cannot choose any of its children or grand children.

In simple words, you have to choose a subset of nodes such that no two nodes in the chosen set have a parent-child relation or grandfather-grandchild relation between them.



Problem Constraints

1 <= N <= 500000

1 <= val <= 10000



Input Format

First argument is the vector A, where A[i] denotes parent of i+1

Second argument is the vector B, where B[i] if the value associated with node i+1



Output Format

Return an integer containing the maximum possible sum. (As the answer can be large, output the answer modulo 1000000007)



Example Input

Input 1:

A = [0]
B = [1]
Input 2:

A = [0, 1, 2, 3]
B = [1, 50, 3, 4]


Example Output

Output 1:

 1
Output 2:

 50


Example Explanation

Explanation 1:

 Only node 1 is taken.
Explanation 2:

 Only node 2 is taken.
"""

class Solution:
    
    def solve(self, A, B):
        pass