"""
Problem Description
Given a 2-D board A of size N x M containing 'X' and 'O', capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.



Problem Constraints
1 <= N, M <= 1000



Input Format
First and only argument is a N x M character matrix A.



Output Format
Make changes to the the input only as matrix is passed by reference.



Example Input
Input 1:

 A = [ 
       [X, X, X, X],
       [X, O, O, X],
       [X, X, O, X],
       [X, O, X, X] 
     ]
Input 2:

 A = [
       [X, O, O],
       [X, O, X],
       [O, O, O]
     ]


Example Output
Output 1:

 After running your function, the board should be:
 A = [
       [X, X, X, X],
       [X, X, X, X],
       [X, X, X, X],
       [X, O, X, X]
     ]
Output 2:

 After running your function, the board should be:
 A = [
       [X, O, O],
       [X, O, X],
       [O, O, O]
     ]


Example Explanation
Explanation 1:

 O in (4,2) is not surrounded by X from below.
Explanation 2:

 No O's are surrounded.
"""

"""
Solution Approach
We already know chunks of O which remain as O are the ones which have at least one O connected to them which is on the boundary.

Use BFS starting from ‘O’s on the boundary and mark them as ‘B’, then iterate over the whole board and mark ‘O’ as ‘X’ and ‘B’ as ‘O’.

Note: Don’t return any matrix. Do the changes in the given matrix.
"""

class Solution:

    cords = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def flip(self, A, i, j):
        q = []
        q.append((i, j))
        A[i][j] = 'X'

        while q:
            i, j = q.pop(0)

            for a, b in self.cords:
                x = i + a
                y = j + b
                if A[x][y] == 'O':
                    A[x][y] = 'X'
                    q.append((x, y))

        return A
    
    def searchValidRegion(self, A, i, j, N, M, visited):
        isValidRegion = True

        q = []
        q.append((i, j))
        visited[i][j] = 1

        while q:
            i, j = q.pop(0)
            for a, b in self.cords:
                x = i + a
                y = j + b
                if (x >= 0 and x < N) and (y >= 0 and y < M):
                    if A[x][y] == 'O' and visited[x][y] == 0:
                        visited[x][y] = 1
                        q.append((x, y))
                else:
                    isValidRegion = False

        return isValidRegion

    def solve(self, A):
        N, M = len(A), len(A[0])

        visited = [[0]*M for _ in range(N)]

        for i in range(N):
            for j in range(M):
                if A[i][j] == 'O' and visited[i][j] == 0:
                    if self.searchValidRegion(A, i, j, N, M, visited):
                        A = self.flip(A, i, j)

        return A