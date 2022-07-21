"""
Problem Description
Given a undirected graph having A nodes. A matrix B of size M x 2 is given which represents the edges such that there is an edge between B[i][0] and B[i][1].

Find whether the given graph is bipartite or not.

A graph is bipartite if we can split it's set of nodes into two independent subsets A and B such that every edge in the graph has one node in A and another node in B

Note:

There are no self-loops in the graph.

No multiple edges between two pair of vertices.

The graph may or may not be connected.

Nodes are Numbered from 0 to A-1.

Your solution will run on multiple testcases. If you are using global variables make sure to clear them.



Problem Constraints
1 <= A <= 100000

1 <= M <= min(A*(A-1)/2,200000)

0 <= B[i][0],B[i][1] < A



Input Format
The first argument given is an integer A.

The second argument given is the matrix B.



Output Format
Return 1 if the given graph is bipartide else return 0.



Example Input
Input 1:

A = 2
B = [ [0, 1] ]
Input 2:

A = 3
B = [ [0, 1], [0, 2], [1, 2] ]


Example Output
Output 1:

1
Output 2:

0


Example Explanation
Explanation 1:

Put 0 and 1 into 2 different subsets.
Explanation 2:

 
It is impossible to break the graph down to make two different subsets for bipartite matching
"""

"""
Solution Approach
You can use and approach either BFS or DFS to check whether the graph can be colored using two colors or not.

Start from any node that hase not been colored yet:
a. Assign color1 to this nodes
b. check its adjacent nodes
a. if this is colored in color1 then the graph can’t be bipartite ,return 0.
b. else if this is colored in color1 do nothing.
c. else color it with color 2 and push it into queue.
Repet step1 until no nodes is left for coloring.
"""

class Solution:
    
    def BFS(self, graph, visited, u):
        visited[u] = 1
        q = [(u, 1)]

        while q:
            u, s = q.pop(0)
            s1 = 2 if s == 1 else 1

            for v in graph[u]:
                if visited[v] == s:
                    return 0
                
                if visited[v] == 0:
                    visited[v] = s1
                    q.append((v, s1))
        
        return 1

    def solve(self, A, B):
        visited = [0]*A

        graph = [[] for _ in range(A)]

        for u, v in B:
            graph[u].append(v)
            graph[v].append(u)

        for i in range(A):
            if visited[i] == 0:
                if not self.BFS(graph, visited, i):
                    return 0

        return 1