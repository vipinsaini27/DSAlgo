"""
Given a binary string A. It is allowed to do at most one swap between any 0 and 1. Find and return the length of the
longest consecutive 1’s that can be achieved.


Input Format
The only argument given is string A.


Output Format
Return the length of the longest consecutive 1’s that can be achieved.


Constraints
1 <= length of string <= 1000000
A contains only characters 0 and 1.


For Example
Input 1:
    A = "111000"
Output 1:
    3

Input 2:
    A = "111011101"
Output 2:
    7
"""

class Solution:

    def solve(self, A):
        l = len(A)

        countOne = A.count('1')

        c = 0
        leftCount = [0]*l
        for i in range(l):
            leftCount[i] = c
            if A[i] == '1':
                c += 1
            else:
                c = 0

        c = 0
        rightCount = [0]*l
        for i in range(l-1, -1, -1):
            rightCount[i] = c
            if A[i] == '1':
                c += 1
            else:
                c = 0

        ans = 0
        for i in range(l):
            val = leftCount[i]+rightCount[i]
            if A[i] == "0":
                if val >= countOne:
                    ans = max(ans, val)
                else:
                    ans = max(ans, val+1)
            else:
                ans = max(ans, val+1)

        return ans