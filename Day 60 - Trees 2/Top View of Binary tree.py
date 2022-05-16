"""
Problem Description
Given a binary tree of integers denoted by root A. Return an array of integers representing the top view of the Binary tree.

The top view of a Binary Tree is a set of nodes visible when the tree is visited from the top.

Return the nodes in any order.



Problem Constraints
1 <= Number of nodes in binary tree <= 100000

0 <= node values <= 10^9



Input Format
First and only argument is head of the binary tree A.



Output Format
Return an array, representing the top view of the binary tree.



Example Input
Input 1:

 
            1
          /   \
         2    3
        / \  / \
       4   5 6  7
      /
     8 
Input 2:

 
            1
           /  \
          2    3
           \
            4
             \
              5


Example Output
Output 1:

 [1, 2, 4, 8, 3, 7]
Output 2:

 [1, 2, 3]


Example Explanation
Explanation 1:

Top view is described.
Explanation 2:

Top view is described.
"""

"""
Solution Approach
You need to return every node to be visible from the top.
In other words, it should be the leftmost or the rightmost till that level.
This can be found using a queue and modifying the level order
traversal algorithm. You may need to maintain the level of each
node along with the nodes themselves.
"""

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def solve(self, A):
        hash = {}
        queue = []
        ver = 0
        mn, mx = 0, 0
        queue.append((A, 0))
        while queue:
            node, ver = queue.pop(0)
            if ver not in hash:
                hash[ver] = node.val

            if node.left is not None:
                queue.append((node.left, ver-1))
            if node.right is not None:
                queue.append((node.right, ver+1))

            if ver > mx:
                mx = ver
            elif ver < mn:
                mn = ver

        ans = []
        i = 0
        while i >= mn:
            ans.append(hash[i])
            i -= 1

        i = 1
        while i <= mx:
            ans.append(hash[i])
            i += 1


        return ans 