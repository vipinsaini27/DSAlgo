"""
Problem Description
Given a matrix of integers A of size N x M consisting of 0 and 1. A group of connected 1's forms an island. From a cell (i, j) such that A[i][j] = 1 you can visit any cell that shares a corner with (i, j) and value in that cell is 1.

More formally, from any cell (i, j) if A[i][j] = 1 you can visit:

(i-1, j) if (i-1, j) is inside the matrix and A[i-1][j] = 1.
(i, j-1) if (i, j-1) is inside the matrix and A[i][j-1] = 1.
(i+1, j) if (i+1, j) is inside the matrix and A[i+1][j] = 1.
(i, j+1) if (i, j+1) is inside the matrix and A[i][j+1] = 1.
(i-1, j-1) if (i-1, j-1) is inside the matrix and A[i-1][j-1] = 1.
(i+1, j+1) if (i+1, j+1) is inside the matrix and A[i+1][j+1] = 1.
(i-1, j+1) if (i-1, j+1) is inside the matrix and A[i-1][j+1] = 1.
(i+1, j-1) if (i+1, j-1) is inside the matrix and A[i+1][j-1] = 1.
Return the number of islands.

NOTE: Rows are numbered from top to bottom and columns are numbered from left to right.



Problem Constraints
1 <= N, M <= 100

0 <= A[i] <= 1



Input Format
The only argument given is the integer matrix A.



Output Format
Return the number of islands.



Example Input
Input 1:

 A = [ 
       [0, 1, 0]
       [0, 0, 1]
       [1, 0, 0]
     ]
Input 2:

 A = [   
       [1, 1, 0, 0, 0]
       [0, 1, 0, 0, 0]
       [1, 0, 0, 1, 1]
       [0, 0, 0, 0, 0]
       [1, 0, 1, 0, 1]    
     ]


Example Output
Output 1:

 2
Output 2:

 5


Example Explanation
Explanation 1:

 The 1's at position A[0][1] and A[1][2] forms one island.
 Other is formed by A[2][0].
Explanation 2:

 There 5 island in total.
"""

"""
Solution Approach
Whenever a cell with unvisited value ‘1’ is encountered we explore all the nodes that are reachable from it and continue exploring until no more nodes are left to explore.

While exploring we mark them visited so that no nodes can be explored twice.

After completion of traversal increament the count of islands.

Find for the 1 which is not visited yet.
"""

import sys

sys.setrecursionlimit(10000)

class Solution:
    
    cords = [[-1, 0], [0, -1], [1, 0], [0, 1], [-1, -1], [1, 1], [1, -1], [-1, 1]]

    def checkCords(self, i, j, N, M):
        if (i >= 0 and i < N) and (j >= 0 and j < M):
            return 1
        return 0

    def DFS(self, A, i, j, N, M, visited):
        for c in self.cords:
            x = i + c[0]
            y = j + c[1]
            if self.checkCords(x, y, N, M):
                if A[x][y] == 1 and visited[x][y] != 1:
                    visited[x][y] = 1
                    self.DFS(A, x, y, N, M, visited)

    def solve(self, A):
        ans = 0
        N, M = len(A), len(A[0])
        visited = [[0]*M for _ in range(N)]

        for i in range(N):
            for j in range(M):
                if A[i][j] == 1 and visited[i][j] != 1:
                    ans += 1
                    self.DFS(A, i, j, N, M, visited)

        return ans 