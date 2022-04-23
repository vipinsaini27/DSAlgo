"""
Problem Description
Akash likes playing with strings. One day he thought of applying following operations on the string in the given order:
Concatenate the string with itself.
Delete all the uppercase letters.
Replace each vowel with '#'.
You are given a string A of size N consisting of lowercase and uppercase alphabets. Return the resultant string after
applying the above operations.
NOTE: 'a' , 'e' , 'i' , 'o' , 'u' are defined as vowels.

Problem Constraints
1<=N<=100000

Input Format
First argument is a string A of size N.

Output Format
Return the resultant string.

Example Input
A="AbcaZeoB"

Example Output
"bc###bc###"

Example Explanation
First concatenate the string with itself so string A becomes "AbcaZeoBAbcaZeoB".
Delete all the uppercase letters so string A becomes "bcaeobcaeo".
Now replace vowel with '#'.
A becomes "bc###bc###".
"""

"""
Solution Approach
It can be solved using bruteforce solution i.e you just follow the operations.
Firstly concatenate the string with itself.
Then create an empty string and loop through the above obtained string and check if it is uppercase character then 
ignore that.
If it is vowel then replace it by ‘#’.
Finally return the output.
"""

class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        C = ""
        for ch in A:
            if ord(ch) >= 97 and ord(ch) <= 122:
                if ch in ['a', 'e', 'i', 'o', 'u']:
                    C += "#"
                else:
                    C += ch

        return C+C