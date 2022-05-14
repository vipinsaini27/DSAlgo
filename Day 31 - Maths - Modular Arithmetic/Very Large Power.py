"""
Problem Description
Given two Integers A, B. You have to calculate (A ^ (B!)) % (1e9 + 7).
"^" means power,
"%" means "mod", and
"!" means factorial.

Problem Constraints
1 <= A, B <= 5e5

Input Format
First argument is the integer A
Second argument is the integer B

Output Format
Return one integer, the answer to the problem

Example Input
Input 1:
A = 1
B = 1
Input 2:
A = 2
B = 2

Example Output
Output 1:
1
Output 2:
4

Example Explanation
Explanation 1:
 1! = 1. Hence 1^1 = 1.
Explanation 2:
 2! = 2. Hence 2^2 = 4.
"""

"""
Solution Approach
This problem is very simple if you know Fermat’s Little Theorem.
The basic approach to solve this problem is to find factorial of B by taking mod with (P-1), 
where P is a prime. In this problem, 10007 is also a prime.
After calculating the factorial of B, you can calculate A ^ B! by simply taking mod with P.
"""

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        m = 10**9+7

        r = 1
        for i in range(1, B+1):
            r = (r*i) % (m-1)

        x = 1
        a = A
        b = r

        while b > 1:
            if b%2 == 0:
                b = b // 2
                a = (a * a) % m
            else:
                b = (b - 1) // 2
                x = x * a
                a = (a * a) % m

        return (a*x) % m