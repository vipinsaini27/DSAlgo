"""
Problem Description
Given two binary strings A and B, count how many cyclic permutations of B when taken XOR with 
A give 0.
NOTE: If there is a string, S0, S1, ... Sn-1 , then it is a cyclic permutation is of the form 
Sk, Sk+1, ... Sn-1, S0, S1, ... Sk-1 where k can be any integer from 0 to N-1.

Problem Constraints
1 ≤ length(A) = length(B) ≤ 105

Input Format
The first argument is a string A.
The second argument is a string B.

Output Format
Return an integer denoting the required answer.

Example Input
Input 1:
 A = "1001"
 B = "0011"
Input 2:
 A = "111"
 B = "111"

Example Output
Output 1:
 1
Output 2:
 3

Example Explanation
Explanation 1:
 4 cyclic permutations of B exists: "0011", "0110", "1100", "1001".  
 There is only one cyclic permutation of B i.e. "1001" which has 0 xor with A.
Explanation 2:
 All cyclic permutations of B are same as A and give 0 when taken xor with A. So, the ans is 3.
"""

class Solution:

    def compute_z(self, s, z):
        l = 0
        r = 0
        n = len(s)
        for i in range(1, n, 1):
            if (i > r):
                l = i
                r = i
                while (r < n and s[r - l] == s[r]):
                    r += 1
                z[i] = r - l
                r -= 1
        
            else:
                k = i - l
                if (z[k] < r - i + 1):
                    z[i] = z[k]
                
                else:
                    l = i
                    while (r < n and s[r - l] == s[r]):
                        r += 1
                    z[i] = r - l
                    r -= 1


    def solve(self, a, b):
        b = b + b
 
        b = b[0:len(b) - 1]
    
        ans = 0
        s = a + "$" + b
        n = len(s)
    
        z = [0 for i in range(n)]
        self.compute_z(s, z)
    
        for i in range(1, n, 1):
            if (z[i] == len(a)):
                ans += 1
        
        return ans
