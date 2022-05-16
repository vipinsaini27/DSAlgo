"""
Problem Description

Given a linked list A and a value B, partition it such that all nodes less than B come before nodes greater than or equal to B.

You should preserve the original relative order of the nodes in each of the two partitions.



Problem Constraints

1 <= |A| <= 106

1 <= A[i], B <= 109



Input Format

The first argument of input contains a pointer to the head to the given linked list.

The second argument of input contains an integer, B.



Output Format

Return a pointer to the head of the modified linked list.



Example Input

Input 1:

A = [1, 4, 3, 2, 5, 2]
B = 3
Input 2:

A = [1, 2, 3, 1, 3]
B = 2


Example Output

Output 1:

[1, 2, 2, 4, 3, 5]
Output 2:

[1, 1, 2, 3, 3]


Example Explanation

Explanation 1:

 [1, 2, 2] are less than B wheread [4, 3, 5] are greater than or equal to B.
Explanation 2:

 [1, 1] are less than B wheread [2, 3, 3] are greater than or equal to B.
"""

"""
Solution Approach
For this question, we have to maintain two pointers.
The first pointer is the one that maintains all nodes that are less than x.
The second pointer is the one that maintains the nodes that are greater than or equal to x.

As we traverse along with our list, when we are at a node that is greater than or equal to x,
we remove this node from our list and move it to a list of nodes that are greater than x.
"""

# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
    
    def partition(self, A, B):
        n = A
        cur = None
        prv = None
        while n != None and n.val < B:
            prv = n
            cur = n
            n = n.next

        while n != None:
            if n.val < B:
                lnode = n
                n = n.next
                prv.next = n

                if cur == None:
                    lnode.next = A
                    A = lnode
                    cur = lnode
                else:
                    lnode.next = cur.next
                    cur.next = lnode
                    cur = lnode
            else:
                prv = n
                n = n.next

        return A