"""
Problem Description
Given an array A, find the size of the smallest subarray such that it contains at least one occurrence of the maximum
value of the array
and at least one occurrence of the minimum value of the array.


Problem Constraints
1 <= |A| <= 2000


Input Format
First and only argument is vector A


Output Format
Return the length of the smallest subarray which has at least one occurrence of minimum and maximum element of the array


Example Input
Input 1:
A = [1, 3]

Input 2:
A = [2]


Example Output
Output 1:
 2

Output 2:
 1


Example Explanation
Explanation 1:
 Only choice is to take both elements.

Explanation 2:
 Take the whole array.
"""

"""
Solution Approach
This problem can be solved in a simple O(N) complexity.
We can implement a sliding window kind of algorithm using two pointers. We can slide over the array and keep track of 
every last occurrence of the minimum and maximum element of the array.
In order to find the start point, we can simply remember the last occurrences of a minimum and a maximum value, 
respectively. And for each min-max pair, we check the length of the subarray that encloses them and then update out 
overall based on that.
"""

class Solution:

    def solve(self, A):
        mx = max(A)
        mi = min(A)
        mxI = None
        miI = None
        ans = None
        i = 0
        while i < len(A):
            val = A[i]
            if val == mx:
                mxI = i
            if val == mi:
                miI = i

            if mxI is not None and miI is not None:
                if ans is None:
                    ans = abs(mxI - miI) + 1
                elif ans > abs(mxI - miI) + 1:
                    ans = abs(mxI - miI) + 1

            i += 1

        return ans