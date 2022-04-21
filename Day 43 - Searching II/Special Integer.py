"""
Problem Description
Given an array of integers A and an integer B, find and return the maximum value K such that there is no subarray in A
of size K with the sum of elements greater than B.


Problem Constraints
1 <= |A| <= 100000
1 <= A[i] <= 10^9
1 <= B <= 10^9


Input Format
The first argument given is the integer array A.
The second argument given is integer B.


Output Format
Return the maximum value of K (sub array length).


Example Input
Input 1:
A = [1, 2, 3, 4, 5]
B = 10

Input 2:
A = [5, 17, 100, 11]
B = 130


Example Output
Output 1:
 2

Output 2:
 3


Example Explanation
Explanation 1:
Constraints are satisfied for maximal value of 2.

Explanation 2:
Constraints are satisfied for maximal value of 3.
"""

"""
Solution Approach
You need to find the maximal K.
Think of a way to do this by binary search.
You can use binary seacrh to find if a certain K is allowed or not.
if it is, you try finding a bigger answer
if not, try finding a smaller answer.
int l = 1, r = a.length;
while(l <= r) {
int m = (l + r) » 1;
if(check(a, b, m)) l = m + 1;
else r = m - 1;
}
return l-1;
"""

class Solution:

    def solve(self, A, B):
        l = len(A)
        sumA = [A[0]]
        for i in range(1, l):
            sumA.append(sumA[-1] + A[i])

        ans = 0
        L, H = 1, l
        while L <= H:
            M = (L + H) // 2

            i = M - 1
            v = 0
            isSmall = True
            while i < len(A):
                if sumA[i] - v > B:
                    isSmall = False
                    break
                i += 1
                v = sumA[i - M]

            if isSmall:
                ans = max(ans, M)
                L = M + 1
            else:
                H = M - 1

        return ans