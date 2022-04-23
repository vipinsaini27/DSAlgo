"""
Problem Description
You are given an array A of N elements. You have to make all elements unique. To do so, in one step you can increase any
number by one.
Find the minimum number of steps.


Problem Constraints
1 <= N <= 105
1 <= A[i] <= 109


Input Format
The only argument given is an Array A, having N integers.


Output Format
Return the minimum number of steps required to make all elements unique.


Example Input
Input 1:
 A = [1, 1, 3]

Input 2:
 A = [2, 4, 5]


Example Output
Output 1:
 1

Output 2:
 0


Example Explanation
Explanation 1:
 We can increase the value of 1st element by 1 in 1 step and will get all unique elements. i.e [2, 1, 3].

Explanation 2:
 All elements are distinct.
"""

"""
Solution Approach
The task is to make all the array elements unique, which needs to be done optimally in the minimum number of steps.
Sort the Array and then start the traversing from the 2nd element.
If the current element is the same as the previous one, then make this element equal to (previous + 1) and count the 
steps.
"""

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A.sort()
        ans = 0
        i = 1
        while i < len(A):
            if A[i] <= A[i - 1]:
                old_val = A[i]
                diff = A[i - 1] - A[i]
                A[i] = A[i] + diff + 1
                ans += (A[i] - old_val)

            i += 1

        return ans