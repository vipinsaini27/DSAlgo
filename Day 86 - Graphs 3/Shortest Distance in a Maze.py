"""
Problem Description
Given a matrix of integers A of size N x M describing a maze. The maze consists of empty locations and walls.

1 represents a wall in a matrix and 0 represents an empty location in a wall.

There is a ball trapped in a maze. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall (maze boundary is also considered as a wall). When the ball stops, it could choose the next direction.

Given two array of integers of size B and C of size 2 denoting the starting and destination position of the ball.

Find the shortest distance for the ball to stop at the destination. The distance is defined by the number of empty spaces traveled by the ball from the starting position (excluded) to the destination (included). If the ball cannot stop at the destination, return -1.



Problem Constraints
2 <= N, M <= 100

0 <= A[i] <= 1

0 <= B[i][0], C[i][0] < N

0 <= B[i][1], C[i][1] < M



Input Format
The first argument given is the integer matrix A.

The second argument given is an array of integer B.

The third argument if an array of integer C.



Output Format
Return a single integer, the minimum distance required to reach destination



Example Input
Input 1:

A = [ [0, 0], [0, 0] ]
B = [0, 0]
C = [0, 1]
Input 2:

A = [ [0, 0], [0, 1] ]
B = [0, 0]
C = [0, 1]


Example Output
Output 1:

 1
Output 2:

 1


Example Explanation
Explanation 1:

 Go directly from start to destination in distance 1.
Explanation 2:

 Go directly from start to destination in distance 1.
"""

"""
Solution Approach
We can definitely say that ball will roll only in one of 4 directions, this gives us only 4 options for each place.
This points towards a BFS based solution. This can be written easily using starting point as source and running bfs until
queue gets empty or we reach our destiniation.
"""

class Solution:
    
    dir = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

    def get_next_pos(self, pos, d):
        i, j = pos
        x, y = self.dir[d]

        return i+x, j+y

    def is_path(self, pos, N, M):
        i, j = pos
        if i < 0 or i >= N or j < 0 or j >= M:
            return 0

        return 1

    def solve(self, A, B, C):
        N, M = len(A), len(A[0])
        visited = []
        for i in range(N):
            visited.append([])
            for _ in range(M):
                visited[i].append([])

        i, j = B
        visited[i][j] = ['U', 'D', 'R', 'L']

        q = []
        for d in visited[i][j]:
            x, y = self.get_next_pos((i, j), d)
            if self.is_path((x, y), N, M) and A[x][y] == 0:
                q.append([(x, y), 1])
                visited[x][y].append(d)

        while q:
            pos, l = q.pop(0)
            i, j = pos
            for d in visited[i][j]:
                x, y = self.get_next_pos((i, j), d)
                if i == C[0] and j == C[1]:
                    if not self.is_path((x, y), N, M) or A[x][y] == 1:
                        return l

                if self.is_path((x, y), N, M) and A[x][y] == 0:
                    if d not in visited[x][y]:
                        visited[x][y].append(d)
                        q.append([(x, y), l+1])
                elif d == 'U' or d == 'D':
                    for nextD in ['R', 'L']:
                        x, y = self.get_next_pos((i, j), nextD)
                        if self.is_path((x, y), N, M) and A[x][y] == 0:
                            if nextD not in visited[x][y]:
                                visited[x][y].append(nextD)
                                q.append([(x, y), l+1])
                elif d == 'R' or d == 'L':
                    for nextD in ['D', 'U']:
                        x, y = self.get_next_pos((i, j), nextD)
                        if self.is_path((x, y), N, M) and A[x][y] == 0:
                            if nextD not in visited[x][y]:
                                visited[x][y].append(nextD)
                                q.append([(x, y), l+1])

        return -1