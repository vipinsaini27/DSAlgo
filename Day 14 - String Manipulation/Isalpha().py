"""
Problem Description
You are given a function isalpha() consisting of a character array A.
Return 1 if all the characters of the character array are alphabetical (a-z and A-Z), else return 0.

Problem Constraints
1 <= |A| <= 105

Input Format
Only argument is a character array A.

Output Format
Return 1 if all the characters of the character array are alphabetical (a-z and A-Z), else return 0.

Example Input
Input 1:
 A = ['S', 'c', 'a', 'l', 'e', 'r', 'A', 'c', 'a', 'd', 'e', 'm', 'y']
Input 2:
 A = ['S', 'c', 'a', 'l', 'e', 'r', '#', '2', '0', '2', '0']

Example Output
Output 1:
 1
Output 2:
 0

Example Explanation
Explanation 1:
 All the characters are alphabets.
Explanation 2:
 All the characters are NOT alphabets i.e ('#', '2', '0', '2', '0').
"""

"""
Solution Approach
Loop through the character array and use the inbuilt function to check if the character is an alphabet or NOT.
In C/C++, isalpha() function takes a character and return 0 if the character is NOT an alphabet.
Similarly, in python we can use character.isalnum().
"""

class Solution:
    # @param A : list of characters
    # @return an integer
    def solve(self, A):
        for i in range(0, len(A)):
            if ord(A[i]) < 65 or ord(A[i]) > 122:
                return 0
            elif ord(A[i]) > 90 and ord(A[i]) < 97:
                return 0

        return 1