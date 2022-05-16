"""
Problem Description
Given a linked list A, remove the B-th node from the end of the list and return its head.

For example, Given linked list: 1->2->3->4->5, and B = 2. After removing the second node from the end, the linked list becomes 1->2->3->5.

NOTE: If B is greater than the size of the list, remove the first node of the list.

NOTE: Try doing it using constant additional space.



Problem Constraints
1 <= |A| <= 106



Input Format
The first argument of input contains a pointer to the head of the linked list.

The second argument of input contains the integer B.



Output Format
Return the head of the linked list after deleting the B-th element from the end.



Example Input
Input 1:

A = [1, 2, 3, 4, 5]
B = 2
Input 2:

A = [1]
B = 1


Example Output
Output 1:

[1, 2, 3, 5]
Output 2:

 [] 


Example Explanation
Explanation 1:

In the first example, 4 is the second last element.
Explanation 2:

In the second example, 1 is the first and the last element.
"""

"""
Solution Approach
Obviously, since we do not have back pointers, reaching the end node and then making our way back is not an option.

There are 2 approaches :
1) Find out the length of the list in one go. Then you know the number of the node to be removed. Traverse to the node and remove it.
2) Make the first pointer go n nodes. Then move the second and first pointer simultaneously. This way, the first pointer is always ahead of the second pointer by n nodes. So when the first pointer reaches the end, you are on the node to be removed.
"""

# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
    
    def removeNthFromEnd(self, A, B):
        count = 0
        node = A
        while node:
            count += 1
            node = node.next

        np = count - B + 1
        if np <= 1:
            prev = A
            A = A.next
            prev.next = None
            del prev
            return A

        i = 2
        node = A.next
        prev = A
        while i < np:
            prev = node
            node = node.next
            i += 1

        prev.next = node.next
        node.next = None
        del node

        return A