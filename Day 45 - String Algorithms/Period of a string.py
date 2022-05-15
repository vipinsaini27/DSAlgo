"""
Problem Description
You are given a string A of length N consisting of lowercase alphabets. Find the period of the 
string.
Period of the string is the minimum value of k (k >= 1), that satisfies A[i] = A[i % k] for all 
valid i.

Problem Constraints
1 <= N <= 106

Input Format
First and only argument is a string A of length N.

Output Format
Return an integer, denoting the period of the string.

Example Input
Input 1:
 A = "abababab"
Input 2:
 A = "aaaa"

Example Output
Output 1:
 2
Output 2:
 1

Example Explanation
Explanation 1:
 Period of the string will be 2: 
 Since, for all i, A[i] = A[i%2]. 
Explanation 2:
 Period of the string will be 1.
"""

class Solution:

    def getZArr(self, A, arr):
        l, r = 0, 1

        for i in range(1, len(A)):
            if i >= r:
                d = 0
                l = i
                while i+d < len(A) and A[i+d] == A[d]:
                    d += 1
                r = d
                arr[i] = d
            else:
                j = i - l
                if i + arr[j] - 1 < r:
                    arr[i] = arr[j]
                else:
                    d = r - i
                    while i+d < len(A) and A[i+d] == A[d]:
                        d += 1
                    arr[i] = d
    
    def solve(self, A):
        arr = [0]*len(A)
        arr[0] = len(A)

        self.getZArr(A, arr)

        ans = len(A)
        for i in range(1, len(A)):
            if i+arr[i] == len(A):
                ans = min(ans, i)
        
        return ans