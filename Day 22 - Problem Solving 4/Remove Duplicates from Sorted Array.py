"""
Problem Description
Given a sorted array A consisting of duplicate elements.
Your task is to remove all the duplicates and return a sorted array of distinct elements consisting of all distinct
elements present in A.
NOTE: The input format has been changed from previous versions.

Problem Constraints
1 <= |A| <= 106
1 <= A[i] <= 2*109

Input Format
First and only argurment containing the integer array A.

Output Format
Return an array/vector from the function as per the question.

Example Input
Input 1:
A = [1, 1, 2]
Input 2:
A = [1, 2, 2, 3, 3]

Example Output
Output 1:
[1, 2]
Output 2:
[1, 2, 3]

Example Explanation
Explanation 1:
Updated Array: [1, 2] after removing the 2nd element.
Explanation 2:
Updated Array: [1, 2, 3] after removing the 3rd and 5th element.
"""

"""
Solution Approach
Notice that the array is sorted.
This implies that all repetitions for an element are clustered together in the array.
**Try maintaining 2 pointers in the array: **
One pointer iterates over the array and
Other pointer only moves per occurrence of a value in the array.
Now you need to make sure we choose only one occurrence per cluster of repetition in the array, we could probably just 
check if A[i] != A[i+1].
So, the second pointer only moves when A[i] != A[i+1]
"""

class Solution:
    
    def solve(self, A):
        ans = []
        ans.append(A[0])
        last_elem = A[0]

        for i in range(1, len(A)):
            if A[i] != last_elem:
                ans.append(A[i])
                last_elem = A[i]

        return ans