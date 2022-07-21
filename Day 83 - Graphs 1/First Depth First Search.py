"""
Problem Description
You are given N towns (1 to N). All towns are connected via unique directed path as mentioned in the input.

Given 2 towns find whether you can reach the first town from the second without repeating any edge.

B C : query to find whether B is reachable from C.

Input contains an integer array A of size N and 2 integers B and C ( 1 <= B, C <= N ).

There exist a directed edge from A[i] to i+1 for every 1 <= i < N. Also, it's guaranteed that A[i] <= i for every 1 <= i < N.

NOTE: Array A is 0-indexed. A[0] = 1 which you can ignore as it doesn't represent any edge.



Problem Constraints
1 <= N <= 100000



Input Format
First argument is vector A

Second argument is integer B

Third argument is integer C



Output Format
Return 1 if reachable, 0 otherwise.



Example Input
Input 1:

 A = [1, 1, 2]
 B = 1
 C = 2
Input 2:

 A = [1, 1, 2]
 B = 2
 C = 1


Example Output
Output 1:

 0
Output 2:

 1


Example Explanation
Explanation 1:

 Tree is 1--> 2--> 3 and hence 1 is not reachable from 2.
Explanation 2:

 Tree is 1--> 2--> 3 and hence 2 is reachable from 1.
"""

"""
Solution Approach
Since you have to start from town number 1 , start your traversal from 1 (root) and use depth first search to reach the second town i.e. y.
Let the query be 6 3, then first search 3 starting from 1.
Now apply depth first search considering root as y ( 3 in this case ) ( move away from 1 ) and search whether x ( i.e. 6 ) is one of its successor. If yes return 1 else return 0 .

OR

Consider parent of i as a[i] and start depth first search from ““y”” to search for x.
"""

class Solution:
	
    def BFS(self, graph, B, C, visited):
        q = []
        q.append(graph[C])
        visited[C] = 1

        while q:
            edges = q.pop(0)

            for e in edges:
                if e == B:
                    return 1
                if visited[e] != 1:
                    visited[e] = 1
                    q.append(graph[e])
        
        return 0
    
    def solve(self, A, B, C):
        if B == C:
            return 1
        N = len(A)
        graph = [[] for _ in range(0, N+1)]
        for i in range(1, N):
            graph[A[i]].append(i+1)
        
        visited = [0]*(N+1)

        ans = self.BFS(graph, B, C, visited)

        return ans