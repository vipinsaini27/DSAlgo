"""
Problem Description
You are given three positive integers, A, B, and C.
Any positive integer is magical if divisible by either B or C.
Return the Ath smallest magical number. Since the answer may be very large, return modulo 109 + 7.


Problem Constraints
1 <= A <= 109
2 <= B, C <= 40000


Input Format
The first argument given is an integer A.
The second argument given is an integer B.
The third argument given is an integer C.


Output Format
Return the Ath smallest magical number. Since the answer may be very large, return modulo 109 + 7.


Example Input
Input 1:
 A = 1
 B = 2
 C = 3

Input 2:
 A = 4
 B = 2
 C = 3


Example Output
Output 1:
 2

Output 2:
 6


Example Explanation
Explanation 1:
 1st magical number is 2.

Explanation 2:
 First four magical numbers are 2, 3, 4, 6 so the 4th magical number is 6.
"""

"""
Solution Approach
Say L = lcm(B, C), the least common multiple of B and C, and let f(x) be the number of magical numbers less than or 
equal to x.
A well known result says that L = (B*C)/gcd(B,C), and that we can calculate the function gcd.

Then f(x) = x/B + x/C - x/L (floor of all the divisions)

Why? There are x/B numbers B, 2B, 3B…. that are divisible by B, there are x/C numbers divisible by C, and we need to 
subtract the x/L numbers divisible by B and C that we double-counted.

Finally,the answer must be between 0 and A * min(B,C).

If x increases f(x) increases, we can use binary search on x to find the Ath number.

Algorithm:
1) Low=1 and High = A * min(B,C)
2) Find mid = (low + high)/2
3) Find f(mid) let it be count
4) If count>=A then mark it as a answer and try to find smaller number which implies high = mid-1
5) Else low = mid+1
6) Repeat steps 2 to 5 until low<=high

Time Complexity: O(log (A * min(B, C)))
Space Complexity: O(1).
"""

class Solution:

    def GCD(self, n1, n2):
        if n2 == 0:
            return n1

        return self.GCD(n2, n1 % n2)

    def LCM(self, n1, n2):
        return (n1 * n2) // self.GCD(n1, n2)

    def solve(self, A, B, C):
        mod = 10 ** 9 + 7

        if B == C:
            return (B * A) % mod
        lcm = self.LCM(B, C)

        L = min(B, C)
        H = L * A
        ans = H

        while L <= H:
            M = (L + H) // 2
            val = M // B + M // C - M // lcm

            if val == A:
                if M % B == 0 or M % C == 0:
                    ans = (min(ans, M)) % mod
                H = M - 1
            elif val > A:
                H = M - 1
            else:
                L = M + 1

        return ans