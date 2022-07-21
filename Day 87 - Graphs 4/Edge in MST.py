"""
Problem Description

Given a undirected weighted graph with A nodes labelled from 1 to A with M edges given in a form of 2D-matrix B of size M * 3 where B[i][0] and B[i][1] denotes the two nodes connected by an edge of weight B[i][2].

For each edge check whether it belongs to any of the possible minimum spanning tree or not , return 1 if it belongs else return 0.

Return an one-dimensional binary array of size M denoting answer for each edge.

NOTE:

The graph may be disconnected in that case consider mst for each component.
No self-loops and no multiple edges present.
Answers in output array must be in order with the input array B output[i] must denote the answer of edge B[i][0] to B[i][1].


Problem Constraints

1 <= A, M <= 3*105

1 <= B[i][0], B[i][1] <= A

1 <= B[i][1] <= 103



Input Format

The first argument given is an integer A representing the number of nodes in the graph.

The second argument given is an matrix B of size M x 3 which represents the M edges such that there is a edge between node B[i][0] and node B[i][1] with weight B[i][2].



Output Format

Return an one-dimensional binary array of size M denoting answer for each edge.



Example Input

Input 1:

 A = 3
 B = [ [1, 2, 2]
       [1, 3, 2]
       [2, 3, 3]
     ]


Example Output

Output 1:

 [1, 1, 0]


Example Explanation

Explanation 1:

 Edge (1, 2) with weight 2 is included in the MST           1
                                                          /   \
                                                         2     3
 Edge (1, 3) with weight 2 is included in the same MST mentioned above.
 Edge (2,3) with weight 3 cannot be included in any of the mst possible.
 So we will return [1, 1, 0]
"""

"""
Solution Approach
This is an easy modification of Kruskal’s algorithm.

Note that if all the weights are unique, the minimum spanning tree is also unique and Kruskal’s algorithm will construct it. Thus, the only “freedom of choice” we have in the general case is the order in which Kruskal’s algorithm will process groups of edges that share the same weight.

As you execute Kruskal’s algorithm, whenever you encounter multiple edges that share the same weight, process them all at once as follows:

For each edge, check whether its endpoints currently lie in different components.
If they do, this edge can be a part of a minimum spanning tree, because if you process it as the first edge from this batch of edges, it will be added to the spanning tree.
If they don’t, this edge cannot be a part of a minimum spanning tree.
Process all the edges from the current batch as you would in the standard algorithm. The order in which you process them does not matter, the resulting connected components will clearly always be the same.
"""

class Solution:
    
    def findParent(self, i, parent):
        if parent[parent[i]] != parent[i]:
            parent[i] = self.findParent(parent[i], parent)

        return parent[i]

    def unionNodes(self, a, b, parent, size):
        p_a = self.findParent(a, parent)
        p_b = self.findParent(b, parent)

        if p_a == p_b:
            return 0

        if size[p_a] >= size[p_b]:
            size[p_a] += size[p_b]
            parent[p_b] = p_a
        else:
            size[p_b] += size[p_a]
            parent[p_a] = p_b

        return 1

    def solve(self, A, B):
        parent = [i for i in range(A+1)]
        size = [1]*(A+1)

        for i in range(len(B)):
            B[i].append(i)

        C = sorted(B, key=lambda x: x[2])

        ans = [0]*len(B)
        i = 0
        while i < len(C):
            j = i
            while True:
                u, v, w, idx = C[j]
                p_u = self.findParent(u, parent)
                p_v = self.findParent(v, parent)
                if p_u != p_v:
                    ans[idx] = 1
                j += 1
                if j >= len(C) or w != C[j][2]:
                    break
            
            j = i
            while True:
                u, v, w, idx = C[j]
                self.unionNodes(u, v, parent, size)
                j += 1
                if j >= len(C) or w != C[j][2]:
                    break
            
            i = j
        
        return ans
        