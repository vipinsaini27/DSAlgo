"""
Problem Description
There is a rectangle with left bottom as (0, 0) and right up as (x, y).

There are N circles such that their centers are inside the rectangle.

Radius of each circle is R. Now we need to find out if it is possible that we can move from (0, 0) to (x, y) without touching any circle.

Note : We can move from any cell to any of its 8 adjecent neighbours and we cannot move outside the boundary of the rectangle at any point of time.



Problem Constraints
0 <= x , y, R <= 100

1 <= N <= 1000

Center of each circle would lie within the grid



Input Format
1st argument given is an Integer x , denoted by A in input.

2nd argument given is an Integer y, denoted by B in input.

3rd argument given is an Integer N, number of circles, denoted by C in input.

4th argument given is an Integer R, radius of each circle, denoted by D in input.

5th argument given is an Array A of size N, denoted by E in input, where A[i] = x cordinate of ith circle

6th argument given is an Array B of size N, denoted by F in input, where B[i] = y cordinate of ith circle



Output Format
Return YES or NO depending on weather it is possible to reach cell (x,y) or not starting from (0,0).



Example Input
Input 1:

 x = 2
 y = 3
 N = 1
 R = 1
 A = [2]
 B = [3]
Input 2:

 x = 1
 y = 1
 N = 1
 R = 1
 A = [1]
 B = [1]


Example Output
Output 1:

 NO
Output 2:

 NO


Example Explanation
Explanation 1:

 There is NO valid path in this case
Explanation 2:

 There is NO valid path in this case
"""

"""
Solution Approach
Check if (i,j) is a valid point for all 0<=i<=x, 0<=j<=y. By valid point we mean that none of the circle should contain it.

Now you know all the valid point in rectangle. You need to figure out if you can go from (0,0) to (x,y) through valid points.
This can be done with any graph traversal algorithms like BFS/DFS.
You may try both of these algorithms to get a feel or how they might work in real life problems.
"""

import math

class Solution:
    cords = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
    
    def checkBoundary(self, i, j, N, M):
        if (i >= 0 and i <= N) and (j >= 0 and j <= M):
            return 1
        return 0 
        
    def DFS(self, grid, A, B, visited):
        stack = []
        if grid[0][0] != 1:
            stack.append((0, 0))
            visited[0][0] = 1
        while stack:
            i, j = stack.pop()
            for m, n in self.cords:
                x = i + m
                y = j + n
                if self.checkBoundary(x, y, A, B):
                    if grid[x][y] != 1 and visited[x][y] != 1:
                        visited[x][y] = 1
                        if x == A and y == B:
                            return "YES"
                        stack.append((x, y))

        return "NO"
    
    def createCir(self, grid, row, col_s, col_e, A, B):
        for i in range(col_s, col_e+1):
            if self.checkBoundary(row, i, A, B):
                grid[row][i] = 1
    
    def solve(self, A, B, C, D, E, F):
        grid = [[0]*(B+1) for _ in range(A+1)]
        visited = [[0]*(B+1) for _ in range(A+1)]

        for i in range(0, A+1):
            for j in range(0, B+1):
                for c_i, c_j in zip(E, F):
                    grid[c_i][c_j] = 1
                    if math.sqrt((pow((c_i - i), 2) + pow((c_j - j), 2))) <= D:
                        grid[i][j] = 1

        ans = self.DFS(grid, A, B, visited)

        return ans