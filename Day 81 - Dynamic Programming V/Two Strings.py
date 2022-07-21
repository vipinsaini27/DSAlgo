"""
Problem Description
Given two strings A and B consisting of lowercase English alphabets. Consider all subsequences of A that are equal to string B.
You have to find whether each character(each index) of string A occurs in at least one of these subsequences.
Return 1 if each character(each index) of string A occurs in at least one of these subsequences, Else return 0.

NOTE: Your solution will run on multiple test cases. Make sure to clear the global variable each time.



Problem Constraints
1 <= |A| <= 100000
1 <= |B| <= 100000



Input Format
The first argument is a string A.
The second argument is a string B.


Output Format
Return 1 if each character(each index) of string s occurs in at least one of these subsequences, Else return 0.



Example Input
A = "abab"
B = "ab"


Example Output
1


Example Explanation
Total possible subsequences in A that are equal to B:
(0, 1), (0, 3), (2, 3)
All indices of string A occurs atleast once in all of these subsequences.
"""

class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        pass