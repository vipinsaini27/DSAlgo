"""
Problem Description
Given three integers A, B and C, where A represents n, B represents r and C represents m, find and return the value of nCr % m where nCr % m = (n!/((n-r)!*r!))% m.

x! means factorial of x i.e. x! = 1 * 2 * 3... * x.


Problem Constraints
1 <= A * B <= 106

1 <= B <= A

1 <= C <= 106


Input Format
The first argument given is integer A ( = n).
The second argument given is integer B ( = r).
The third argument given is integer C ( = m).


Output Format
Return the value of nCr % m.


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
 The value of 5C2 % 11 is 10.

Explanation 2:
 The value of 6C2 % 13 is 2.
"""

"""
Solution Approach
If we calculate nCr by calculating factorial of each number and then doing n! / (r! * (n-r)!) % m. This will not work as 
the factorial can be very large and will cause overflow.

As we know nCr = n-1Cr-1 + n-1Cr.

So we will use Dynamic Programming approach and calculate the value of nCr.
"""

class Solution:

    def solve(self, A, B, C):
        hash = [[1] * (B + 1) for _ in range(A + 1)]

        for i in range(A + 1):
            hash[i][1] = i % C

        for i in range(2, A + 1):
            j = 2
            while j <= B and j < i:
                hash[i][j] = (hash[i - 1][j] + hash[i - 1][j - 1]) % C
                j += 1

        return hash[A][B]
