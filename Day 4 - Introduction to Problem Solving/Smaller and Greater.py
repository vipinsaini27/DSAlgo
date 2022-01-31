"""
You are given an Array A of size N.

Find for how many elements, there is a strictly smaller element and a strictly greater element.


Input Format
Given only argument A an Array of Integers.

Output Format
Return an Integer X, i.e number of elements.

Constraints
1 <= N <= 1e5
1 <= A[i] <= 1e6

For Example
Example Input:
    A = [1, 2, 3]

Example Output:
    1

Explanation:
    only 2 have a strictly smaller and strictly greater element, 1 and 3 respectively.
"""


class Solution:
    
    def solve(self, A):
        min_elem = min(A)
        max_elem = max(A)

        count = 0
        for i in A:
            if i > min_elem and i < max_elem:
                count += 1

        return count