"""
Problem Description
Given three integers A, B and C, where A represents n, B represents r and C represents p and p is a prime number greater than equal to n, find and return the value of nCr % p where nCr % p = (n! / ((n-r)! * r!)) % p.

x! means factorial of x i.e. x! = 1 * 2 * 3... * x.

NOTE: For this problem, we are considering 1 as a prime.


Problem Constraints
1 <= A <= 106
1 <= B <= A
A <= C <= 109+7


Input Format
The first argument given is the integer A ( = n).
The second argument given is the integer B ( = r).
The third argument given is the integer C ( = p).


Output Format
Return the value of nCr % p.


Example Input
Input 1:
 A = 5
 B = 2
 C = 13

Input 2:
 A = 6
 B = 2
 C = 13


Example Output
Output 1:
 10

Output 2:
 2


Example Explanation
Explanation 1:
 nCr( n=5 and r=2) = 10.
 p=13. Therefore, nCr%p = 10.
"""

"""
Solution Approach
This problem can be solved using Fermat’s Little theorem.

a^p = a (mod p) where p is a prime number.

a^(p-1) = 1 (mod p)

Multiply by a inverse on both sides

a^(p-2) = a^(-1) (mod p).
Using the above result, nCr can be calulated as ( fact[n]%p ) * inversemodulo( fact[n-r] %p ) * inversemodulo( fact[r] %p ).
"""

import time

class Solution:

    def solve(self, A, B, C):
        if A == 1 and B == 1 and C == 1:
            return 0

        den = num = 1
        B = min(B, A-B)
        for i in range(B):
            num = (num * (A - i)) % C
            den = (den * (i + 1)) % C

        return (num * pow(den, C-2, C)) % C