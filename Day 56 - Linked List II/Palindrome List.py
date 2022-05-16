"""
Problem Description
Given a singly linked list A, determine if it's a palindrome. Return 1 or 0, denoting if it's a palindrome or not, respectively.



Problem Constraints
1 <= |A| <= 105



Input Format
The first and the only argument of input contains a pointer to the head of the given linked list.



Output Format
Return 0, if the linked list is not a palindrome.

Return 1, if the linked list is a palindrome.



Example Input
Input 1:

A = [1, 2, 2, 1]
Input 2:

A = [1, 3, 2]


Example Output
Output 1:

 1 
Output 2:

 0 


Example Explanation
Explanation 1:

 The first linked list is a palindrome as [1, 2, 2, 1] is equal to its reversed form.
Explanation 2:

 The second linked list is not a palindrom as [1, 3, 2] is not equal to [2, 3, 1].
"""

"""
Solution Approach
To check palindrome, we just have to reverse the latter half of the linked list, and then we can, in (n/2) steps total can compare if all elements are the same or not.
For finding the midpoint, first, we can in O(N) traverse the whole list and calculate the total number of elements.
Reversing is again O(N).
"""

# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
    
    def lPalin(self, A):
        size = 0
        n = A
        while n != None:
            size += 1
            n = n.next

        end = size // 2
        prv = None
        cur = A
        nxt = A.next

        for i in range(1, end+1):
            cur.next = prv
            prv = cur
            cur = nxt
            nxt = cur.next

        p1 = prv
        if size%2 == 0:
            p2 = cur
        else:
            p2 = nxt

        while p1 != None and p2 != None:
            if p1.val != p2.val:
                return 0
            p1 = p1.next
            p2 = p2.next

        return 1