"""
Problem Description
Given a binary tree,

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Assume perfect binary tree and try to solve this in constant extra space.



Problem Constraints
1 <= Number of nodes in binary tree <= 100000

0 <= node values <= 10^9



Input Format
First and only argument is head of the binary tree A.



Output Format
Return the head of the binary tree after the changes are made.



Example Input
Input 1:

 
     1
    /  \
   2    3
Input 2:

 
        1
       /  \
      2    5
     / \  / \
    3  4  6  7


Example Output
Output 1:

 
        1 -> NULL
       /  \
      2 -> 3 -> NULL
Output 2:

 
         1 -> NULL
       /  \
      2 -> 5 -> NULL
     / \  / \
    3->4->6->7 -> NULL


Example Explanation
Explanation 1:

Next pointers are set as given in the output.
Explanation 2:

Next pointers are set as given in the output.
"""

"""
Solution Approach
Breadth first approach to exploring a tree is based on the concept of the level of a node.
The level of a node is its depth or distance from the root node.
We process all the nodes on one level before moving on to the next one.
We need to link all the nodes together which lie on the same level and the
level order or the breadth first traversal gives us access to all such nodes.
"""

# Definition for a  binary tree node
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
   
    def connect(self, root):
        q = []
        q.append(root)
        i = 0
        while i < len(q):
            node = q[i]
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)

            i += 1

        i = 0
        j = 0
        endIdx = 0
        while True:
            while j < endIdx:
                node = q[j]
                nxtNode = q[j+1]
                node.next = nxtNode
                j += 1
            
            j += 1
            i += 1
            endIdx += 2**i
            if endIdx > len(q):
                break
        
        return root
