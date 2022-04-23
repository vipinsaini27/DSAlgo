"""
Problem Description
You are given a function isalpha() consisting of a character array A.
Return 1 if all the characters of a character array are alphanumeric (a-z, A-Z, and 0-9) else, return 0.

Problem Constraints
1 <= |A| <= 105

Input Format
Only argument is a character array A.

Output Format
Return 1 if all the characters of the character array are alphanumeric (a-z, A-Z and 0-9), else return 0.

Example Input
Input 1:
 A = ['S', 'c', 'a', 'l', 'e', 'r', 'A', 'c', 'a', 'd', 'e', 'm', 'y', '2', '0', '2', '0']
Input 2:
 A = ['S', 'c', 'a', 'l', 'e', 'r', '#', '2', '0', '2', '0']

Example Output
Output 1:
 1
Output 2:
 0

Example Explanation
Explanation 1:
 All the characters are alphanumeric.
Explanation 2:
 All the characters are NOT alphabets i.e ('#').
"""

"""
Solution Approach
Loop through the character array and use the inbuilt function to check if the character is an alphabet or a number.
In C/C++, isalnum() function takes a character and return 0 if the character is NOT an alphabet or a number.
Similarly, in python, we can use character.isalnum().
"""

class Solution:
    # @param A : list of characters
    # @return an integer
    def solve(self, A):
        for val in A:
            if ord(val) < 48 or ord(val) > 122:
                return 0
            elif ord(val) > 57 and ord(val) < 65:
                return 0
            elif ord(val) > 90 and ord(val) < 97:
                return 0

        return 1