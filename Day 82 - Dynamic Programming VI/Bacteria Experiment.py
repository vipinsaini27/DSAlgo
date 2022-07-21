"""
Problem Description

A year after his bacteria experiment, Jason decided to perform another experiment on a new bacteria specie which evolves in a special way.

The initial form of the bacteria can be considered as an undirected tree with A nodes in terms of graph theory.

Every hour, an edge (x, y) is built if there exists a node z such that, in the previous hour, there exists edge (x, z) and edge (y, z), but not edge (x, y).

The bacteria keep evolving until no more edges can be formed.


As it may take months if not years for the bacteria to evolve to its ultimate form, it is impossible for Jason to stay at the laboratory to observe the change of the bacteria throughout the entire process.

Therefore, he wants you to calculate the time required for the bacteria to fully evolve, so that he can just get back to the laboratory on time.

NOTE:

The nodes are labeled from 1 to A.


Problem Constraints

2 <= N <= 105



Input Format

First argument is an integer A denoting the number of nodes in the tree.

Second argument is a 2-D array B of size (N-1) x 2 denoting the edge of the tree.



Output Format

Return a single integer denoting the time required for the bacteria to fully evolve.



Example Input

Input 1:

 A = 6
 B = [  [1, 5]
        [5, 3]
        [5, 6]
        [6, 2]
        [6, 4]
     ]
Input 2:

 A = 2
 B = [  [1, 2]
     ]


Example Output

Output 1:

 2
Output 2:

 0


Example Explanation

Explanation 1:

 See the diagram given in the question.
Explanation 2:

 There are no more edges that can be created which means the bacteria is already fully evolved so we will return 0.
"""

class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        pass