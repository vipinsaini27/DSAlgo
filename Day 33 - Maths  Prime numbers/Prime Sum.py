'''
Problem Description
Given an even number A ( greater than 2 ), return two prime numbers whose sum will be equal to given number.

If there are more than one solutions possible, return the lexicographically smaller solution.

If [a, b] is one solution with a <= b, and [c,d] is another solution with c <= d, then
[a, b] < [c, d], If a < c OR a==c AND b < d.
NOTE: A solution will always exist. Read Goldbach's conjecture.


Problem Constraints
4 <= A <= 2*107


Input Format
First and only argument of input is an even number A.


Output Format
Return a integer array of size 2 containing primes whose sum will be equal to given number.


Example Input
 4

Example Output
 [2, 2]


Example Explanation
 There is only 1 solution for A = 4.
'''

n = 2*10**7

prime = [1]*(n+1)
i = 2
while i*i <= n:
    if prime[i]:
        j = i*i
        while j <= n:
            prime[j] = 0
            j += i
    i += 1

class Solution:

    def primesum(self, A):
        global prime

        for i in range(2, (A//2)+1):
            if prime[i]:
                a = i
                b = A - a
                if prime[b]:
                    break

        return [a, b]


