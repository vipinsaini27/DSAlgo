"""
Problem Description
Given a binary tree of integers denoted by root A. Return an array of integers representing the right view of the Binary tree.

Right view of a Binary Tree is a set of nodes visible when the tree is visited from Right side.



Problem Constraints
1 <= Number of nodes in binary tree <= 100000

0 <= node values <= 10^9



Input Format
First and only argument is head of the binary tree A.



Output Format
Return an array, representing the right view of the binary tree.



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

 [1, 3, 7, 8]
Output 2:

 [1, 3, 4, 5]


Example Explanation
Explanation 1:

Right view is described.
Explanation 2:

Right view is described.
"""

"""
Solution Approach
Whenever you encounter the last node on that level, append it to the answer for each level.
Try to Modify the level order traversal of the tree for this problem.
You should finally append the rightmost node for each level of the
given binary tree and return the vector of the same.
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
    
    def righView(self, A, l, hash = {}):
        if A.right is not None:
            hash = self.righView(A.right, l+1, hash)
        
        if l not in hash:
            hash[l] = A.val
        
        if A.left is not None:
            hash = self.righView(A.left, l+1, hash)

        return hash
    
    def solve(self, A):
        ans = []
        hash = self.righView(A, 1, {})
        for i in range(1, 100001):
            if i in hash:
                ans.append(hash[i])
            else:
                break

        return ans