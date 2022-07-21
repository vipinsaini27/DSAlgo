"""
Problem Description
Given a matrix of integers A of size N x M consisting of 0, 1 or 2.

Each cell can have three values:

The value 0 representing an empty cell.

The value 1 representing a fresh orange.

The value 2 representing a rotten orange.

Every minute, any fresh orange that is adjacent (Left, Right, Top, or Bottom) to a rotten orange becomes rotten. Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1 instead.

Note: Your solution will run on multiple test cases. If you are using global variables, make sure to clear them.



Problem Constraints
1 <= N, M <= 1000

0 <= A[i][j] <= 2



Input Format
The first argument given is the integer matrix A.



Output Format
Return the minimum number of minutes that must elapse until no cell has a fresh orange.

If this is impossible, return -1 instead.



Example Input
Input 1:

A = [   [2, 1, 1]
        [1, 1, 0]
        [0, 1, 1]   ]
Input 2:

 
A = [   [2, 1, 1]
        [0, 1, 1]
        [1, 0, 1]   ]


Example Output
Output 1:

 4
Output 2:

 -1


Example Explanation
Explanation 1:

 Max of 4 using (0,0) , (0,1) , (1,1) , (1,2) , (2,2)
Explanation 2:

 Task is impossible
"""

"""
Solution Approach
Every turn, the rotting spreads from each rotting orange to other adjacent oranges.
Initially, the rotten oranges have ‘depth’ 0, and every time they rot a neighbor,
the neighbors have 1 more depth. We want to know the largest possible depth.

Use multi-source BFS to achieve this with all cells containing rotten oranges as starting nodes.
At the end check if there are fresh oranges left or not.
"""

class Solution:

    cords = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    
    def checkBoundary(self, i, j, N, M):
        if (i >= 0 and i < N) and (j >= 0 and j < M):
            return 1
        return 0

    def solve(self, A):
        N, M = len(A), len(A[0])
        li, q = [], []
        for i in range(N):
            for j in range(M):
                if A[i][j] == 2:
                    li.append([(i, j), 0])

        q.append(li)
        ans = 0
        while q:
            li = []
            rOrange = q.pop(0)
            for o in rOrange:
                c, d = o[0], o[1]
                for (a, b) in self.cords:
                    x = c[0] + a
                    y = c[1] + b
                    if self.checkBoundary(x, y, N, M):
                        if A[x][y] == 1:
                            A[x][y] = 2
                            li.append([(x, y), d+1])

            if len(li) == 0:
                break
            q.append(li)
            ans += 1

        for i in range(N):
            for j in range(M):
                if A[i][j] == 1:
                    return -1

        return ans