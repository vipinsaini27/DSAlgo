"""
Problem Description

A students applied for admission in IB Academy. An array of integers B is given representing the strengths of A people i.e. B[i] represents the strength of ith student.

Among the A students some of them knew each other. A matrix C of size M x 2 is given which represents relations where ith relations depicts that C[i][0] and C[i][1] knew each other.

All students who know each other are placed in one batch.

Strength of a batch is equal to sum of the strength of all the students in it.

Now the number of batches are formed are very much, it is impossible for IB to handle them. So IB set criteria for selection: All those batches having strength at least D are selected.

Find the number of batches selected.

NOTE: If student x and student y know each other, student y and z know each other then student x and student z will also know each other.



Problem Constraints

1 <= A <= 105

1 <= M <= 2*105

1 <= B[i] <= 104

1 <= C[i][0], C[i][1] <= A

1 <= D <= 109



Input Format

The first argument given is an integer A.
The second argument given is an integer array B.
The third argument given is a matrix C.
The fourth argument given is an integer D.



Output Format

Return the number of batches selected in IB.



Example Input

Input 1:

 A = 7
 B = [1, 6, 7, 2, 9, 4, 5]
 C = [  [1, 2]
        [2, 3] 
       `[5, 6]
        [5, 7]  ]
 D = 12
Input 2:

 A = 5
 B = [1, 2, 3, 4, 5]
 C = [  [1, 5]
        [2, 3]  ]
 D = 6


Example Output

Output 1:

 2
Output 2:

 1


Example Explanation

Explanation 1:

 Initial Batches :
    Batch 1 = {1, 2, 3} Batch Strength = 1 + 6 + 7 = 14
    Batch 2 = {4} Batch Strength = 2
    Batch 3 = {5, 6, 7} Batch Strength = 9 + 4 + 5 = 18
    Selected Batches are Batch 1 and Batch 2.
Explanation 2:

 Initial Batches :
    Batch 1 = {1, 5} Batch Strength = 1 + 5  = 6
    Batch 2 = {2, 3} Batch Strength = 5
    Batch 3 = {4} Batch Strength = 4  
    Selected Batch is only Batch 1.
"""

"""
Solution Approach
Modify the above problem in the form of an undirected weighted graph.
Consider students as nodes and relations as edges between them.
All connected components come under one batch.
Strength of a batch is the sum of the weight of nodes of connected components of the graph(batch).

After Modifying the problem statement to graph perspective, It is easy to see find the solution.

Initiaize ans = 0

Pick any unvisited node and find the sum of all the weights of nodes which are reachable from this node and mark all such nodes as visited. if this sum is greater than equal to D then increment ans.

If N is the number of students and M is the number of relations then
Time Complexity : O (N+M)
"""

class Solution:

    def findParent(self, i, parent):
        if parent[parent[i]] != parent[i]:
            parent[i] = self.findParent(parent[i], parent)
        
        return parent[i]
    
    def unionNodes(self, a, b, parent, size, B):
        p_a = self.findParent(a, parent)
        p_b = self.findParent(b, parent)

        if p_a != p_b:
            if size[p_a] >= size[p_b]:
                size[p_a] += size[p_b]
                parent[p_b] = p_a
                B[p_a - 1] += B[p_b - 1]
                B[p_b - 1] = 0
            else:
                size[p_b] += size[p_a]
                parent[p_a] = p_b
                B[p_b - 1] += B[p_a - 1]
                B[p_a - 1] = 0

    def solve(self, A, B, C, D):
        parent = [i for i in range(A+1)]
        size = [1 for _ in range(A+1)]

        for u, v in C:
            self.unionNodes(u, v, parent, size, B)

        ans = 0
        for i in range(1, A+1):
            if parent[i] == i and B[i-1] >= D:
                ans += 1

        return ans