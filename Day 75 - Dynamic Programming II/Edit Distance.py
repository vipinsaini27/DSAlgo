"""
Problem Description
Given two strings A and B, find the minimum number of steps required to convert A to B. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character


Problem Constraints
1 <= length(A), length(B) <= 450



Input Format
The first argument of input contains a string, A.
The second argument of input contains a string, B.



Output Format
Return an integer, representing the minimum number of steps required.



Example Input
Input 1:

 A = "abad"
 B = "abac"
Input 2:

 A = "Anshuman"
 B = "Antihuman


Example Output
Output 1:

 1
Output 2:

 2


Example Explanation
Exlanation 1:

 A = "abad" and B = "abac"
 After applying operation: Replace d with c. We get A = B.
 
Explanation 2:

 A = "Anshuman" and B = "Antihuman"
 After applying operations: Replace s with t and insert i before h. We get A = B.
"""

"""
Solution Approach
This is a very standard Dynamic programming problem.

Lets look at the bruteforce approach for finding edit distance of S1 and S2.
We are trying to modify S1 to become S2.

We look at the first character of both the strings.
If they match, we can look at the answer from remaining part of S1 and S2.
If they don’t, we have 3 options.
1) Insert S2’s first character and then solve the problem for remaining part of S2, and S1.
2) Delete S1’s first character and trying to match S1’s remaining string with S2.
3) Replace S1’s first character with S2’s first character in which case we solve the problem for remaining part of S1 and S2.

The code would probably look something like this :

int editDistance(string &S1, int index1, string &S2, int index2) {
// BASE CASES

if (S1[index1] == S2[index2]) {
     return editDistance(S1, index1 + 1, S2, index2 + 1);
} else {
     return min(
    1 + editDistance(S1, index1 + 1, S2, index2), // Delete S1 char
            1 + editDistance(S1, index1, S2, index2 + 1), // Insert S2 char
            1 + editDistance(S1, index1 + 1, S2, index2 + 1) // Replace S1 first char with S2 first char
     );
} }
The above approach is definitely exponential.
However, lets look at the number of ways in which the function can be called. S1 and S2 remain constant. The only thing changing is index1 and index2 which can take len(S1) * len(S2) number of values. Can you use it to memoize ?

You can use the above observation to also come up with a non recursive solution.
"""

import sys

sys.setrecursionlimit(450*450)

class Solution:

    def minSteps(self, A, B, i, j, dp):
        if i < len(A) and j < len(B):
            if dp[i][j] != -1:
                return dp[i][j]
            
            if A[i] == B[j]:
                dp[i][j] = self.minSteps(A, B, i+1, j+1, dp)
            else:
                a = self.minSteps(A, B, i+1, j, dp)
                b = self.minSteps(A, B, i, j+1, dp)
                c = self.minSteps(A, B, i+1, j+1, dp)
                dp[i][j] = min(a, b, c) + 1
        else:
            return max(len(A) - i, len(B) - j)

        return dp[i][j]
    
    def minDistance(self, A, B):
        dp = [[-1]*len(B) for _ in range(len(A))]

        ans = self.minSteps(A, B, 0, 0, dp)

        return ans