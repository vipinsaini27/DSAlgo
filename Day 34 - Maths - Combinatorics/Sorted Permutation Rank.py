"""
Problem Description
Given a string A. Find the rank of the string amongst its permutations sorted lexicographically.
Assume that no characters are repeated.

Note: The answer might not fit in an integer, so return your answer % 1000003


Problem Constraints
1 <= |A| <= 1000


Input Format
First argument is a string A.


Output Format
Return an integer denoting the rank of the given string.


Example Input
Input 1:
A = "acb"

Input 2:
A = "a"


Example Output
Output 1:
2

Output 2:
1


Example Explanation
Explanation 1:
Given A = "acb".
The order permutations with letters 'a', 'c', and 'b' :
abc
acb
bac
bca
cab
cba
So, the rank of A is 2.

Explanation 2:
Given A = "a".
Rank is clearly 1.
"""

class Solution:
    MAX_CHAR = 256
    count = [0]*(MAX_CHAR + 1)
    m = 10**5 + 3

    def fact(self, n):
        return 1 if n <= 1 else (n * self.fact(n-1))

    def getCharCount(self, S):
        for i in range(len(S)):
            self.count[ord(S[i])] += 1

        for i in range(1, self.MAX_CHAR):
            self.count[i] += self.count[i - 1]

    def updateCount(self, ch):
        for i in range(ord(ch), self.MAX_CHAR):
            self.count[i] -= 1

    def findRank(self, A):
        ans = 1
        l = len(A)
        f = self.fact(l)

        self.getCharCount(A)
        for i in range(l):
            f = f // (l - i)

            ans = (ans + (self.count[ord(A[i]) - 1] * f) % self.m) % self.m

            self.updateCount(A[i])

        return ans
