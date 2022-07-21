"""
Problem Description
Given an array with non negative numbers, divide the array into two parts such that the average of both the parts is equal. Return both parts (If exist). If there is no solution. return an empty list.

NOTE 1: If a solution exists, you should return a list of exactly 2 lists of integers A and B which follow the following condition : numElements in A <= numElements in B

If numElements in A = numElements in B, then A is lexicographically smaller than B ( https://en.wikipedia.org/wiki/Lexicographical_order )

NOTE 2: If multiple solutions exist, return the solution where length(A) is minimum. If there is still a tie, return the one where A is lexicographically smallest.

NOTE 3: Array will contain only non negative numbers.



Problem Constraints
|A| <= 100

A[i] <= 100



Input Format
First and only argument is the vector A.



Output Format
Return the 2 lists if target can be achieved, otherwise return empty lists.



Example Input
Input 1:

 A = [1, 7, 15, 29, 11, 9]
Input 2:

 A = [2, 2] 


Example Output
Output 1:

[ [9 15], [1 7 11 29]  ]
Output 2:

[ [2], [2]  ]


Example Explanation
Explanation 1:

 
The average of first part is (15 + 9) / 2 = 12,


average of second part elements is (1 + 7 + 11 + 29) / 4 = 12


Explanation 2:

 [2] and [2] have equal average

"""

class Solution:
    
    def avgset(self, A):
        pass