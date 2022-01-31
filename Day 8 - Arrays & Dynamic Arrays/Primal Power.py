"""
Problem Description
"Primal Power" of an array is defined as the count of prime numbers present in it.
Given an array of integers A of length N, you have to calculate its Primal Power.


Problem Constraints
1 <= N <= 103
-106 <= A[i] <= 106


Input Format
First and only argument is an integer array A.


Output Format
Return the Primal Power of array A.


Example Input
Input 1:
 A = [-6, 10, 12]

Input 2:
 A = [-11, 7, 8, 9, 10, 11]


Example Output
Output 1:
 0

Output 2:
 2


Example Explanation
Explanation 1:
 -6 is not a prime number, as prime numbers are always natural numbers(by definition).
  Also, both 10 and 12 are composite numbers.

Explanation 2:
 7 and 11 are prime numbers. Hence, Primal Power = 2.
"""

class Solution:
    
    def solve(self, A):
        ans = 0
        n = 10**6
        prime = [True for i in range(n+1)]
        p = 2
        while p*p < n:
            if prime[p] == True:
                for i in range(p*2, n+1, p):
                    prime[i] = False

            p += 1

        prime[0] = False
        prime[1] = False
        for val in A:
            if val > 1 and prime[val]:
                ans += 1

        return ans