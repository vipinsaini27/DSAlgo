"""
Problem Description
Given a matrix of integers A of size N x M consisting of 0 or 1.

For each cell of the matrix find the distance of nearest 1 in the matrix.

Distance between two cells (x1, y1) and (x2, y2) is defined as |x1 - x2| + |y1 - y2|.

Find and return a matrix B of size N x M which defines for each cell in A distance of nearest 1 in the matrix A.

NOTE: There is atleast one 1 is present in the matrix.



Problem Constraints
1 <= N, M <= 1000

0 <= A[i][j] <= 1



Input Format
The first argument given is the integer matrix A.



Output Format
Return the matrix B.



Example Input
Input 1:

 A = [
       [0, 0, 0, 1]
       [0, 0, 1, 1] 
       [0, 1, 1, 0]
     ]
Input 2:

 A = [
       [1, 0, 0]
       [0, 0, 0]
       [0, 0, 0]  
     ]


Example Output
Output 1:

 [ 
   [3, 2, 1, 0]
   [2, 1, 0, 0]
   [1, 0, 0, 1]   
 ]
Output 2:

 [
   [0, 1, 2]
   [1, 2, 3]
   [2, 3, 4] 
 ]


Example Explanation
Explanation 1:

 A[0][0], A[0][1], A[0][2] will be nearest to A[0][3].
 A[1][0], A[1][1] will be nearest to A[1][2].
 A[2][0] will be nearest to A[2][1] and A[2][3] will be nearest to A[2][2].
Explanation 2:

 There is only a single 1. Fill the distance from that 1.
"""

"""
Solution Approach
The idea is to use multi-source BFS. At the begining insert all the nodes having value 1 in the queue.

We first explore immediate adjacent of all 1’s, then adjacent of adjacent, and so on.

Only if the distance at the cell of matrix is greater than the current distance, then only we update the distance of the cell.

Therefore we find minimum distance.

Time Complexity: O( N x M)
"""

class Solution:
    
    cords = [(0, -1), (0, 1), (1, 0), (-1, 0)]

    def solve(self, A):
        N, M = len(A), len(A[0])

        ans = [[0]*M for _ in range(N)]

        q = []
        li = []

        for i in range(N):
            for j in range(M):
                if A[i][j] == 1:
                    li.append((i, j))
        q.append(li)

        while q:
            li = []
            lvl = q.pop(0)
            for i, j in lvl:
                for a, b in self.cords:
                    x = i + a
                    y = j + b
                    if (x >= 0 and x < N) and (y >= 0 and y < M):
                        if A[x][y] != 1 and ans[x][y] == 0:
                            ans[x][y] = ans[i][j] + 1
                            li.append((x, y))
            
            if len(li) > 0:
                q.append(li)

        return ans