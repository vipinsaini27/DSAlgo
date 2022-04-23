"""
Problem Description
Groot has a profound love for palindrome which is why he keeps fooling around with strings.
A palindrome string is one that reads the same backward as well as forward.
Given a string A of size N consisting of lowercase alphabets, he wants to know if it is possible to make the given
string a palindrome by changing exactly one of its character.

Problem Constraints
1 <= N <= 105

Input Format
The first and only argument is a string A.

Output Format
Return the string YES if it is possible to make the given string a palindrome by changing exactly 1 character. Else, it should return the string NO.

Example Input
Input 1:
 A = "abbba"
Input 2:
 A = "adaddb"

Example Output
Output 1:
 "YES"
Output 2:
 "NO"

Example Explanation
Explanation 1:
 We can change the character at index 3(1-based) to any other character. The string will be palindromic.
Explanation 2:
 To make the string palindromic we need to change 2 characters.
"""

"""
Solution Approach
We apply our standard palindrome checking algorithm and count the number of times a set of mirror indices has different 
characters.
If at the end of processing, this count is greater than 1, then it can never be possible since we will have to change 
more than one character to make it a palindrome.
If the count is 1, the answer is always yes.
A corner case that needs to be considered is the case when the count is 0.
If the count is 0 and the palindrome length is even, then we cannot change exactly one character to make it a 
palindrome. We will have to change two mirror indices.
But if the count is 0 and the length is odd, then it is possible as we can change the middlemost character to anything.
"""

class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        i, j = 0, len(A) - 1
        count = 0
        while i < j:
            if A[i] != A[j]:
                count += 1
            i += 1
            j -= 1

        if count == 0 and len(A) % 2 != 0:
            return "YES"
        elif count == 0:
            return "NO"

        if count > 1:
            return "NO"

        return "YES"