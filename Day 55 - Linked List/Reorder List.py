"""
Problem Description
Given a singly linked list A

 A: A0 → A1 → … → An-1 → An 
reorder it to:

 A0 → An → A1 → An-1 → A2 → An-2 → … 
You must do this in-place without altering the nodes' values.



Problem Constraints
1 <= |A| <= 106



Input Format
The first and the only argument of input contains a pointer to the head of the linked list A.



Output Format
Return a pointer to the head of the modified linked list.



Example Input
Input 1:

 A = [1, 2, 3, 4, 5] 
Input 2:

 A = [1, 2, 3, 4] 


Example Output
Output 1:

 [1, 5, 2, 4, 3] 
Output 2:

 [1, 4, 2, 3] 


Example Explanation
Explanation 1:

 The array will be arranged to [A0, An, A1, An-1, A2].
Explanation 2:

 The array will be arranged to [A0, An, A1, An-1, A2].
"""

"""
Solution Approach
We can try to break down the solution approach into majorly three parts.

Firstly, we try to break the list from the middle into two separate linked lists.
Now, we reverse the latter half of the linked list.
Finally, we would merge the lists so that the nodes alternate to get the required answer.
"""

# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reorderList(self, A):
        n = A
        nodeList = []
        while n != None:
            nodeList.append(n)
            n = n.next

        listSize = len(nodeList)
        if listSize % 2 == 0:
            end = (listSize // 2)
        else:
            end = (listSize // 2) + 1

        node = A
        j = 1
        for i in range(1, end):
            newNode = nodeList[-j]
            newNode.next = node.next
            node.next = newNode
            node = newNode.next
            j += 1

        nodeList[-j].next = None

        return A