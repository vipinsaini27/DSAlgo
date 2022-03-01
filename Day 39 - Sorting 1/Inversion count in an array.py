"""
Problem Description
Given an array of integers A. If i < j and A[i] > A[j] then the pair (i, j) is called an inversion of A. Find the total number of inversions of A modulo (109 + 7).


Problem Constraints
1 <= length of the array <= 100000
1 <= A[i] <= 10^9


Input Format
The only argument given is the integer array A.


Output Format
Return the number of inversions of A modulo (109 + 7).


Example Input
Input 1:
A = [3, 2, 1]

Input 2:
A = [1, 2, 3]


Example Output
Output 1:
3

Output 2:
0


Example Explanation
Explanation 1:
 All pairs are inversions.

Explanation 2:
 No inversions.
"""

"""
Solution Approach
Algorithm :
Traverse through the array from start to end
For every element find the count of elements smaller than the current number upto that index using another loop.
Sum up the count of inversion for every index.
Print the count of inversions.
"""

class Solution:

    def mSort(self, A, ans):
        if len(A) < 2:
            return ans

        m = len(A) // 2
        lArr = A[:m]
        rArr = A[m:]
        ans = self.mSort(lArr, ans)
        ans = self.mSort(rArr, ans)

        flag = False
        i, j = len(lArr) - 1, len(rArr) - 1
        while i >= 0 and j >= 0:
            if lArr[i] > rArr[j]:
                ans = (ans + j + 1) % (10**9 + 7)
                i -= 1
            else:
                j -= 1

        i, j = 0, 0
        k = 0
        while i < len(lArr) and j < len(rArr):
            if lArr[i] >= rArr[j]:
                A[k] = rArr[j]
                j += 1
            else:
                A[k] = lArr[i]
                i += 1
            k += 1

        while i < len(lArr):
            A[k] = lArr[i]
            i += 1
            k += 1

        while j < len(rArr):
            A[k] = rArr[j]
            j += 1
            k += 1

        return ans

    def solve(self, A):
        ans = self.mSort(A, 0)

        return ans