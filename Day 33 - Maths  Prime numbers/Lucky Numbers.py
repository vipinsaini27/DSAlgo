"""
Problem Description
A lucky number is a number which has exactly 2 distinct prime divisors.

You are given a number A and you need to determine the count of lucky numbers between the range 1 to A (both inclusive).


Problem Constraints
1 <= A <= 50000


Input Format
The first and only argument is an integer A.


Output Format
Return an integer i.e the count of lucky numbers between 1 and A, both inclusive.


Example Input
Input 1:
 A = 8

Input 2:
 A = 12


Example Output
Output 1:
 1

Output 2:
 3


Example Explanation
Explanation 1:
 Between [1, 8] there is only 1 lucky number i.e 6.
 6 has 2 distinct prime factors i.e 2 and 3.

Explanation 2:
 Between [1, 12] there are 3 lucky number: 6, 10 and 12.
"""

n = 50000
sieve = [1]*(n+1)
div = [0]*(n+1)

i = 2
while i*i <= n:
    if sieve[i]:
        j = i*i
        while j <= n:
            sieve[j] = 0
            j += i
    i += 1

prime = []
for i in range(2, n+1):
    if sieve[i]:
        prime.append(i)

i = 0
while i < len(prime):
    j = i + 1
    while j < len(prime):
        v = prime[i]*prime[j]
        if v <= n:
            div[v] = 1
        j += 1
    i += 1

class Solution:

    def solve(self, A):
        global div
        ans = 0
        for i in range(1, A+1):
            print(f"{i} = {div[i]}")
            if div[i]:
                ans += 1

        return ans