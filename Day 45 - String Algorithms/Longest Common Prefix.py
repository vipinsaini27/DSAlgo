"""
Problem Description
Given the array of strings A, you need to find the longest string S, which is the prefix of 
ALL the strings in the array.
The longest common prefix for a pair of strings S1 and S2 is the longest string S which is the 
prefix of both S1 and S2.
Example: the longest common prefix of "abcdefgh" and "abcefgh" is "abc".

Problem Constraints
0 <= sum of length of all strings <= 1000000

Input Format
The only argument given is an array of strings A.

Output Format
Return the longest common prefix of all strings in A.

Example Input
Input 1:
A = ["abcdefgh", "aefghijk", "abcefgh"]
Input 2:
A = ["abab", "ab", "abcd"];

Example Output
Output 1:
"a"
Output 2:
"ab"

Example Explanation
Explanation 1:
Longest common prefix of all the strings is "a".
Explanation 2:
Longest common prefix of all the strings is "ab".
"""

"""
Solution Approach
Note: the prefix has to be the prefix of ALL the strings.
So, you can pick any random string from the array and start checking its characters from the 
beginning to see if they can be a part of the common substring.
"""

class Solution:
    
    def longestCommonPrefix(self, A):
        l = 0
        minLen = 1000000
        for s in A:
            minLen = min(minLen, len(s))

        while l < minLen:
            c = A[0][l]
            i = 1
            while i < len(A):
                if c != A[i][l]:
                    return A[0][0:l]
                i += 1
            l += 1

        return A[0][0:l]