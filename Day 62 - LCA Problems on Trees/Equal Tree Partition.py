"""
Problem Description
Given a binary tree A. Check whether it is possible to partition the tree to two trees which have equal sum of values after removing exactly one edge on the original tree.



Problem Constraints
1 <= size of tree <= 100000

0 <= value of node <= 109



Input Format
First and only argument is head of tree A.



Output Format
Return 1 if the tree can be partitioned into two trees of equal sum else return 0.



Example Input
Input 1:

 
                5
               /  \
              3    7
             / \  / \
            4  6  5  6
Input 2:

 
                1
               / \
              2   10
                  / \
                 20  2


Example Output
Output 1:

 1
Output 2:

 0


Example Explanation
Explanation 1:

 Remove edge between 5(root node) and 7: 
        Tree 1 =                                               Tree 2 =
                        5                                                     7
                       /                                                     / \
                      3                                                     5   6    
                     / \
                    4   6
        Sum of Tree 1 = Sum of Tree 2 = 18
Explanation 2:

 The given Tree cannot be partitioned.
"""

"""
Solution Approach
After removing some edge from parent to child,
(where the child cannot be the original root)
the subtree rooted at child must be half the sum of the entire tree.

Let’s record the sum of every subtree. We can do this recursively using depth-first search.
After, we should check that half the sum of the entire tree occurs somewhere in our recording
(and not from the total of the entire tree.)
"""

# Definition for a  binary tree node
class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution:
    
    def getSum(self, A):
        lSumList, rSumList = [], []
        if A.left is not None:
            lSumList = self.getSum(A.left)
        if A.right is not None:
            rSumList = self.getSum(A.right)
        
        s = 0
        if lSumList:
            s += lSumList[-1]
        if rSumList:
            s += rSumList[-1]

        s += A.val

        return lSumList + rSumList + [s]
    
    def solve(self, A):
        sumList = self.getSum(A)
        i = 0
        while i < len(sumList) - 1:
            if sumList[-1] - sumList[i] == sumList[i]:
                return 1
            i += 1

        return 0
