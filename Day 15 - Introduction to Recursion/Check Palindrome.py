"""
Problem Description
Write a recursive function that checks whether string A is a palindrome or Not.
Return 1 if the string A is a palindrome, else return 0.
Note: A palindrome is a string that's the same when read forward and backward.

Problem Constraints
1 <= A <= 50000
String A consists only of lowercase letters.

Input Format
The first and only argument is a string A.

Output Format
Return 1 if the string A is a palindrome, else return 0.

Example Input
Input 1:
 A = "naman"
Input 2:
 A = "strings"

Example Output
Output 1:
 1
Output 2:
 0

Example Explanation
Explanation 1:
 "naman" is a palindomic string, so return 1.
Explanation 2:
 "strings" is not a palindrome, so return 0.
"""

"""
Solution Approach
Consider two indexes i and j, initially at the first and last index of the string, respectively.
If the character at both i and j index is the same, check recursively for i+1, j-1.
We can say that, F(i, j) tell if the string from i to j is palindrome or not:
if(A[i] == A[j])
F(i, j) = F(i+1, j-1)
else
F(i, j) = 0
"""

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A, i = 0):
        if i > len(A)//2:
            return 1
        strLen = len(A)
        if A[i] == A[strLen - i - 1]:
            isValid = self.solve(A, i + 1)
        else:
            return 0

        return isValid