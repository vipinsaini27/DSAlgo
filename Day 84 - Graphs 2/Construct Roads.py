"""
Problem Description
A country consist of N cities connected by N - 1 roads. King of that country want to construct maximum number of roads such that the new country formed remains bipartite country.

Bipartite country is a country, whose cities can be partitioned into 2 sets in such a way, that for each road (u, v) that belongs to the country, u and v belong to different sets. Also, there should be no multiple roads between two cities and no self loops.

Return the maximum number of roads king can construct. Since the answer could be large return answer % 109 + 7.

NOTE: All cities can be visited from any city.



Problem Constraints
1 <= A <= 105

1 <= B[i][0], B[i][1] <= N



Input Format
First argument is an integer A denoting the number of cities, N.

Second argument is a 2D array B of size (N-1) x 2 denoting the initial roads i.e. there is a road between cities B[i][0] and B[1][1] .



Output Format
Return an integer denoting the maximum number of roads king can construct.



Example Input
Input 1:

 A = 3
 B = [
       [1, 2]
       [1, 3]
     ]
Input 2:

 A = 5
 B = [
       [1, 3]
       [1, 4]
       [3, 2]
       [3, 5]
     ]


Example Output
Output 1:

 0
Output 2:

 2


Example Explanation
Explanation 1:

 We can't construct any new roads such that the country remains bipartite.
Explanation 2:

 We can add two roads between cities (4, 2) and (4, 5).
"""

"""
Solution Approach
As we know, the tree is itself bipartite.

Run a Depth First search over the given tree and partition it into two sets.

We can’t add an edge between any 2 nodes in the same set and we can add an edge between every 2 nodes in different sets, so let the number of nodes in the left set be x and the number of nodes in the right set be y.

The maximum number of edges that can exist is x * y, but N - 1 edges already exist so the maximum number of edges to be added is x * y - (N - 1).
"""

class Solution:
    
    def BFS(self, graph, visited, i):
        visited[i-1] = 1
        q = [(i, 1)]

        while q:
            u, s = q.pop(0)
            s = 2 if s == 1 else 1
            for v in graph[u-1]:
                if visited[v-1] == 0:
                    visited[v-1] = s
                    q.append((v, s))

    def solve(self, A, B):
        visited = [0]*A

        graph = [[] for _ in range(A)]

        for u, v in B:
            graph[u-1].append(v)
            graph[v-1].append(u)

        for i in range(A):
            if visited[i] == 0:
                self.BFS(graph, visited, i+1)

        ans = 0
        set1, set2 = 0, 0
        for i in range(A):
            if visited[i] == 1:
                set1 += 1
            else:
                set2 += 1

        for i in range(A):
            if visited[i] == 1:
                ans = (ans + (set2 - len(graph[i]))) % (10**9 + 7)
            else:
                ans = (ans + (set1 - len(graph[i]))) % (10**9 + 7)
        

        return ans // 2