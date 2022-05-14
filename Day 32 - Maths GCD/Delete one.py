"""
Problem Description
Given an integer array A of size N. You have to delete one element such that the GCD(Greatest 
common divisor) of the remaining array is maximum.
Find the maximum value of GCD.

Problem Constraints
2 <= N <= 105
1 <= A[i] <= 109

Input Format
First argument is an integer array A.

Output Format
Return an integer denoting the maximum value of GCD.

Example Input
Input 1:
 A = [12, 15, 18]
Input 2:
 A = [5, 15, 30]

Example Output
Output 1:
 6
Output 2:
 15

Example Explanation
Explanation 1:
 If you delete 12, gcd will be 3.
 If you delete 15, gcd will be 6.
 If you delete 18, gcd will 3.
 Maximum vallue of gcd is 6.
Explanation 2:
 If you delete 5, gcd will be 15.
 If you delete 15, gcd will be 5.
 If you delete 30, gcd will be 5.
"""

"""
Solution Approach
We can maintain two arrays for prefix and suffix gcd; likewise, we do for prefix sum and 
suffix sum.
Then,for each index, i:1 to N calculate gcd(prefix[i-1],suffix[i+1]) and return the maximum 
among all.
"""

class Solution:
    
    def gcd(self, a, b):
        if b == 0:
            return a
        
        return self.gcd(b, a%b)


    def solve(self, A):
        n = len(A)

        preFix = [A[0]]
        for i in range(1, n):
            preFix.append(self.gcd(preFix[-1], A[i]))

        postFix = [A[-1]]
        for i in range(n-2, -1, -1):
            postFix.insert(0, self.gcd(postFix[0], A[i]))

        ans = postFix[1]
        for i in range(n):
            if i+1 == n:
                ans = max(ans, preFix[i-1])
            else:
                ans = max(ans, self.gcd(preFix[i-1], postFix[i+1]))
        
        return ans
