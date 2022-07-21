"""
Problem Description

Given a matrix C of integers, of dimension A x B.

For any given K, you are not allowed to travel between cells that have an absolute difference greater than K.

Return the minimum value of K such that it is possible to travel between any pair of cells in the grid through a path of adjacent cells.

NOTE:

Adjacent cells are those cells that share a side with the current cell.


Problem Constraints

1 <= A, B <= 102

1 <= C[i][j] <= 109



Input Format

The first argument given is A.

The second argument give is B.

The third argument given is the integer matrix C.



Output Format

Return a single integer, the minimum value of K.



Example Input

Input 1:

 A = 3
 B = 3
 C = [  [1, 5, 6]
        [10, 7, 2]
        [3, 6, 9]   ]


Example Output

Output 1:

 4


Example Explanation

Explanation 1:

 
 It is possible to travel between any pair of cells through a path of adjacent cells that do not have an absolute
 difference in value greater than 4. e.g. : A path from (0, 0) to (2, 2) may look like this:
 => (0, 0) -> (0, 1) -> (1, 1) -> (2, 1) -> (2, 2)
"""

"""
Solution Approach
Think of matrix as a graph with A*B nodes and Each node has an edge to its four neighbouring cells with weight as absolute difference of values between them.

Apply any MST algorithm on it and find the maximum weighted edge in that MST.

Why we have to apply MST?
Because in MST we always consider smallest weighted edge as to minimize the total cost so just find mst and find the maximum weighted edge in that MST.

You can use any of Kruskal or Prims Implementation of MST to solve this question.
"""

import heapq

class Solution:
    
    cords = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def checkBoundary(self, pos, A, B):
        i, j = pos
        if i < 0 or i >= A or j < 0 or j >= B:
            return 0

        return 1

    def solve(self, A, B, C):
        visited = [[0]*B for _ in range(A)]

        ans = 0
        q = []
        heapq.heappush(q, (0, (0, 0)))

        while q:
            v, pos= heapq.heappop(q)
            i, j = pos
            if not visited[i][j]:
                visited[i][j] = 1
                if v > ans:
                    ans = v
                for a, b in self.cords:
                    x = i + a
                    y = j + b
                    if self.checkBoundary((x, y), A, B):
                        if not visited[x][y]:
                            val = abs(C[x][y] - C[i][j])
                            heapq.heappush(q, (val, (x, y)))

        return ans