"""
Problem Description
You are given a Binary Tree A with N nodes.

Write a function that returns the size of the largest subtree, which is also a Binary Search Tree (BST).

If the complete Binary Tree is BST, then return the size of the whole tree.

NOTE:

The largest subtree is the subtree with the most number of nodes.


Problem Constraints
1 <= N <= 105



Input Format
First and only argument is an pointer to root of the binary tree A.



Output Format
Return an single integer denoting the size of the largest subtree which is also a BST.



Example Input
Input 1:

     10
    / \
   5  15
  / \   \ 
 1   8   7
Input 2:

     5
    / \
   3   8
  / \ / \
 1  4 7  9


Example Output
Output 1:

 3
Output 2:

 7


Example Explanation
Explanation 1:

 Largest BST subtree is
                            5
                           / \
                          1   8
Explanation 2:

 Given binary tree itself is BST.
"""

"""
Solution Approach
Maintain a data structure that stores for every node the maximum value in the subtree of a node, the minimum value in the subtree of a node,
size of the subtree, size of the largest BST found in the subtree of a node, and flag to denote whether this subtree is bst or not.

Traverse the tree in a bottom-up manner.

A Tree is BST if the following is true for every node X.

The largest value in the left subtree (of X) is smaller than the value of X.
The smallest value in the right subtree (of X) is greater than the value of X.
update the details of these nodes accordingly.
"""

# Definition for a  binary tree node
class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution:
    
    Max = 0

    def subTree(self, A, is_left):
        lMaxVal, rMinVal = [A.val] * 2
        returnValid = True
        lValid, rValid = True, True
        lCount, rCount = 0, 0 
        
        if A.left is not None:
            lValid, lCount, lMaxVal = self.subTree(A.left, 1)
        if A.right is not None:
            rValid, rCount, rMinVal = self.subTree(A.right, 0)

        returnValid = True
        if lValid and rValid:
            if lMaxVal <= A.val and rMinVal >= A.val:
                if self.Max < (lCount + rCount + 1):
                    self.Max = (lCount + rCount + 1)
            else:
                returnValid = False
        else:
            return False, 0, 0

        if is_left:
            returnVal = max(lMaxVal, rMinVal, A.val)
        else:
            returnVal = min(lMaxVal, rMinVal, A.val)

        returnCount = lCount + rCount + 1

        return returnValid, returnCount, returnVal
    
    def solve(self, A):
        self.subTree(A, False)  

        return self.Max