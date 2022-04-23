"""
Problem Description
Given a string A, rotate the string B times in clockwise direction and return the string.

Problem Constraints
1 <= |A| <= 105
1 <= B <= 109
String A consist only of lowercase characters.

Input Format
First and only argument is a string A.

Output Format
Return a string denoting the rotated string.

Example Input
Input 1:
 A = "scaler"
 B = 2
Input 2:
 A = "academy"
 B = 7

Example Output
Output 1:
 "erscal"
Output 2:
 "academy"

Example Explanation
Explanation 1:
 Rotate the given string twice so the string becomes "erscal".
"""

"""
Solution Approach
One thing we can do is remove the last character B times and add it at the beginning of the string.
Try to do it in more efficient way by using reverse method.
Firstly, If B >= length of A, do B = B % length of A.
For doing the clockwise rotation, we can do N-B times anticlockwise rotation.
Let’s say d = N-B
For that, reverse the first d characters of string, then last N-d characters and then reverse the whole string.
We will get the B times rotated clockwise string.
"""

class Solution:
    # @param A : string
    # @param B : integer
    # @return a strings
    def solve(self, A, B):
        B = B % len(A)
        ans = ""
        i = len(A) - B
        while i < len(A):
            ans += A[i]
            i += 1

        i = 0
        while i < len(A) - B:
            ans += A[i]
            i += 1

        return ans
