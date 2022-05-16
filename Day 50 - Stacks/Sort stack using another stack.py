"""
Problem Description
Given a stack of integers A, sort it using another stack.
Return the array of integers after sorting the stack using another stack.

Problem Constraints
1 <= |A| <= 5000
0 <= A[i] <= 109

Input Format
The only argument is a stack given as an integer array A.

Output Format
Return the array of integers after sorting the stack using another stack.

Example Input
Input 1:
 A = [5, 4, 3, 2, 1]
Input 2:
 A = [5, 17, 100, 11]

Example Output
Output 1:
 [1, 2, 3, 4, 5]
Output 2:
 [5, 11, 17, 100]

Example Explanation
Explanation 1:
 Just sort the given numbers.
Explanation 2:
 Just sort the given numbers.
"""

"""
Solution Approach
Create a temporary stack say B.
While input stack is not empty:
1. pop an element from input stack calls it x.
2. while the temporary stack is not empty and top of the temporary stack is greater than x pop from the temporary stack and push it into input stack.
3. push x in the temporary stack.
The sorted numbers are in the temporary stack.
Worst case time complexity O(n^2).
"""

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        s1 = A
        s2 = []
        s3 = []

        is_empty = lambda x: len(x) > 0

        while is_empty(s1):
            val = s1.pop()
            while is_empty(s3) and s3[-1] < val:
                s2.append(s3.pop())
            
            s3.append(val)
            while is_empty(s2):
                s3.append(s2.pop())

        while is_empty(s3):
            s1.append(s3.pop())

        return s1