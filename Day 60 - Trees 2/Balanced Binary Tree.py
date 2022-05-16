"""
Problem Description
Given a root of binary tree A, determine if it is height-balanced.

A height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.



Problem Constraints
1 <= size of tree <= 100000



Input Format
First and only argument is the root of the tree A.



Output Format
Return 0 / 1 ( 0 for false, 1 for true ) for this problem.



Example Input
Input 1:

    1
   / \
  2   3
Input 2:

 
       1
      /
     2
    /
   3


Example Output
Output 1:

1
Output 2:

0


Example Explanation
Explanation 1:

It is a complete binary tree.
Explanation 2:

Because for the root node, left subtree has depth 2 and right subtree has depth 0. 
Difference = 2 > 1.
"""

"""
Solution Approach
A tree is balanced if :
1) Left subtree is balanced
2) Right subtree is balanced
3) The difference in the height of the left and right subtree is at most 1.

Can you think of a way to simulate that with recursion?
Note that depth of a tree can also be calculated recursively as max(depth(rightSubtree), depth(leftSubtree)) + 1.
"""

# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
    
    maxLeftH = -1000000
    maxRightH = -1000000
    
    def heightCheck(self, A):
        lh = 0
        rh = 0
        is_balanced = 1
        if is_balanced and A.left is not None:
            is_balanced, lh = self.heightCheck(A.left)
        if is_balanced and A.right is not None:
            is_balanced, rh = self.heightCheck(A.right)

        if not is_balanced:
            return 0, 0
        if lh == rh or lh+1 == rh or rh+1 == lh:
            is_balanced = 1
        else:
            is_balanced = 0

        if lh >= rh:
            return (is_balanced, lh+1)
        
        return (is_balanced, rh+1)
        
    def isBalanced(self, A):
        ans, _ = self.heightCheck(A)

        return ans 