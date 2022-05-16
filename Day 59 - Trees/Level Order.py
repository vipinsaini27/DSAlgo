"""
Problem Description
Given a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).



Problem Constraints
1 <= number of nodes <= 105



Input Format
First and only argument is root node of the binary tree, A.



Output Format
Return a 2D integer array denoting the zigzag level order traversal of the given binary tree.



Example Input
Input 1:

    3
   / \
  9  20
    /  \
   15   7
Input 2:

   1
  / \
 6   2
    /
   3


Example Output
Output 1:

 [
   [3],
   [9, 20],
   [15, 7]
 ]
Output 2:

 [ 
   [1]
   [6, 2]
   [3]
 ]


Example Explanation
Explanation 1:

 Return the 2D array. Each row denotes the traversal of each level.
"""

"""
Solution Approach
There are two ways to solve this problem.

Approach 1: Maintain a vector of size ‘depth’ of the tree. Do any tree traversals keep track of the current depth? Append the current element to vector[currentDepth]. Since we need stuff left to right, make sure the left subtree is visited before the right subtree ( Any traditional pre/post/inorder traversal should suffice ).

Approach 2: This is important. A lot of times, you’d be asked to do a traditional level order traversal. Or, to put informal words, a traversal where the extra memory used should be proportional to the nodes on a level rather than the depth of the tree. To do that, you need to make sure you are accessing all the nodes on a level before accessing the nodes next. This is a typical breadth-first search problem—queue FTW.
"""

# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
    
    def levelOrder(self, A):
        ans = []
        queue = []
        queue.append(A)
        while queue:
            level = []
            next_queue = []
            for node in queue:
                if node is not None:
                    next_queue.append(node.left)
                    next_queue.append(node.right)
                    level.append(node.val)
            if level:
                ans.append(level)
            queue = next_queue

        return ans