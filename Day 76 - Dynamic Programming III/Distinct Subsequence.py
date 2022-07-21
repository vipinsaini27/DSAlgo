"""
Problem Description
Given two sequences A and B, count number of unique ways in sequence A, to form a subsequence that is identical to the sequence B.

Subsequence : A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).



Problem Constraints
1 <= length(A), length(B) <= 700



Input Format
The first argument of input contains a string A.
The second argument of input contains a string B.



Output Format
Return an integer representing the answer as described in the problem statement.



Example Input
Input 1:

 A = "abc"
 B = "abc"
Input 2:

 A = "rabbbit" 
 B = "rabbit" 


Example Output
Output 1:

 1
Output 2:

 3


Example Explanation
Explanation 1:

 Both the strings are equal.
Explanation 2:

 These are the possible removals of characters:
    => A = "ra_bbit" 
    => A = "rab_bit" 
    => A = "rabb_it"

 Note: "_" marks the removed character.
"""

"""
Solution Approach
As a typical way to implement a dynamic programming algorithm, we construct a matrix dp, where each cell dp[i][j] represents the number of solutions of aligning substring B[0..i] with A[0..j];

Rule 1). dp[0][j] = 1, since aligning B = “” with any substring of A would have only ONE solution which is to delete all characters in A.

Rule 2). when i > 0, dp[i][j] can be derived by two cases:

case 1). if B[i] != A[j], then the solution would be to ignore the character A[j] and align substring B[0..i] with A[0..(j-1)]. Bherefore, dp[i][j] = dp[i][j-1].

case 2). if B[i] == A[j], then first we could adopt the solution in case 1), but also we could match the characters B[i] and A[j] and align the rest of them (i.e. B[0..(i-1)] and A[0..(j-1)]. As a result, dp[i][j] = dp[i][j-1] + d[i-1][j-1]

e.g. B = B, A = ABC

dp[1][2]=1: Align B’=B and A’=AB, only one solution, which is to remove character A in A’.
"""

class Solution:
    
    def numDistinct(self, A, B):
        M = len(A)
        N = len(B)

        dp = [[0]*(N+1) for _ in range(M+1)]

        for i in range(0, M+1):
            dp[i][0] = 1

        for i in range(1, M+1):
            for j in range(1, N+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i-1][j]

        return dp[M][N]