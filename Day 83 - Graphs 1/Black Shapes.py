"""
Problem Description

Given character matrix A of O's and X's, where O = white, X = black.

Return the number of black shapes. A black shape consists of one or more adjacent X's (diagonals not included)



Problem Constraints

1 <= |A|,|A[0]| <= 1000

A[i][j] = 'X' or 'O'



Input Format

The First and only argument is character matrix A.



Output Format

Return a single integer denoting number of black shapes.



Example Input

Input 1:

 A = [ [X, X, X], [X, X, X], [X, X, X] ]
Input 2:

 A = [ [X, O], [O, X] ]


Example Output

Output 1:

 1
Output 2:

 2


Example Explanation

Explanation 1:

 All X's belong to single shapes
Explanation 2:

 Both X's belong to different shapes
"""

"""
Solution Approach
Simple graph traversal approach:

Answer := 0
Loop i = 1 to N :
    Loop j = 1 to M:
          IF MATRIX at i, j equal to 'X' and not visited:
                 BFS/DFS to mark the connected area as visited
                 update Answer
    EndLoop
EndLoop

return Answer
You can always use both DFS and BFS to see the working of both of these traversal algorithms.
They will always help you solve such type of problems.
"""

class Solution:
    
    cords = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    
    def checkBoundary(self, i, j, N, M):
        if (i >= 0 and i < N) and (j >= 0 and j < M):
            return 1
        return 0
        
    def DFS(self, A, visited, i, j, N, M):
        stack = []
        visited[i][j] = 1
        stack.append((i, j))

        while stack:
            i, j = stack.pop()
            for a, b in self.cords:
                x = i + a
                y = j + b
                if self.checkBoundary(x, y, N, M):
                    if A[x][y] == 'X' and visited[x][y] == 0:
                        visited[x][y] = 1
                        stack.append((x, y))
                        
    def black(self, A):
        N, M = len(A), len(A[0])
        visited = [[0]*M for _ in range(N)]

        ans = 0
        for i in range(N):
            for j in range(M):
                if A[i][j] == "X" and visited[i][j] == 0:
                    ans += 1
                    self.DFS(A, visited, i, j, N, M)

        return ans