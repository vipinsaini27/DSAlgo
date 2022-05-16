"""
Problem Description
A linked list A is given such that each node contains an additional random pointer which could point to any node in the list or NULL.

Return a deep copy of the list.



Problem Constraints
0 <= |A| <= 106



Input Format
The first argument of input contains a pointer to the head of linked list A.



Output Format
Return a pointer to the head of the required linked list.



Example Input
Given list
   1 -> 2 -> 3
with random pointers going from
  1 -> 3
  2 -> 1
  3 -> 1
  


Example Output
   1 -> 2 -> 3
with random pointers going from
  1 -> 3
  2 -> 1
  3 -> 1
  


Example Explanation
You should return a deep copy of the list. The returned answer should not contain the same node as the original list, but a copy of them. The pointers in the returned list should not link to any node in the original input list.
"""

"""
Solution Approach
There are 2 approaches to solving this problem.

Approach 1: Using hashmap.
Use a hashmap to store the mapping from oldListNode to the newListNode. Whenever you encounter a new node in the oldListNode (either via a random pointer or through the next pointer ), create the newListNode, store the mapping. And update the next and random pointers of the newListNode using the mapping from the hashmap.

Approach 2 : Using 2 traversals of the list.
Step 1: create a new node for each existing node and join them together eg: A->B->C will be A->A’->B->B’->C->C’

Step2: copy the random links: for each new node n’, n’.random = n.random.next

Step3: detach the list: basically n.next = n.next.next; n’.next = n’.next.next
"""

# Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        node = head
        while node != None:
            copy_node = RandomListNode(node.label)
            copy_node.next = node.next
            node.next = copy_node
            node = node.next.next
        
        head1 = head.next
        node = head
        while node != None:
            copy_node = node.next
            if node.random != None:
                copy_node.random = node.random.next
            else:
                copy_node.random = None
            node = node.next.next
            
        node = head
        copy_node = node.next
        while copy_node.next != None:
            node.next = copy_node.next
            node = node.next
            copy_node.next = node.next
            copy_node = copy_node.next
            
        node.next = None
        copy_node.next = None
        
        return head1
            
        
