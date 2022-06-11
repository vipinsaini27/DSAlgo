"""
Problem Description
Given a string A made up of multiple brackets of type "[]" , "()" and "{}" find the length of the longest substring which forms a balanced string .

Conditions for a string to be balanced :

Blank string is balanced ( However blank string will not be provided as a test case ).
If B is balanced : (B) , [B] and {B} are also balanced.
If B1 and B2 are balanced then B1B2 i.e the string formed by concatenating B1 and B2 is also balanced.


Problem Constraints
0 <= |A| <= 106



Input Format
First and only argument is an string A.



Output Format
Return an single integer denoting the lenght of the longest balanced substring.



Example Input
Input 1:

 A = "[()]"
Input 2:

 A = "[(])"


Example Output
Output 1:

 4
Output 2:

 0


Example Explanation
Explanation 1:

 Substring [1:4] i.e "[()]" is the longest balanced substring of length 4.
Explanation 2:

 None of the substring is balanced so answer is 0.
"""

"""
Solution Approach
The solution uses DP. The main idea is as follows:
1) Construct an array longest[] . For any index i, longest[i] stores the longest length of valid parentheses which ends at i.

And the DP idea for any string s is :

2) If s[i] is any opening bracket, set longest[i] to 0, because any string ending with an opening bracket cannot be balanced.
3) If s[i] is a closing bracket and s[i-1] is it’s opening balancing bracket then, longest[i] = longest[i-2] + 2
4) If s[i] is a closing bracket and s[i-longest[i-1]-1] is it’s opening balancing bracket then, longest[i] = longest[i-1] + 2 + longest[i-longest[i-1]-2]
5) Rest all the cases when s[i] is a closing bracket, longest[i] will be equal to 0.
"""

class Solution:
    # @param A : string
    # @return an integer

    def isValid(self, A, i, j):
        if j >= 0:
            if A[i] == ')' and A[j] == '(':
                return True
            if A[i] == ']' and A[j] == '[':
                return True
            if A[i] == '}' and A[j] == '{':
                return True

        return False

    def LBSlength(self, A):
        if len(A) == 1:
            return 0

        dp = [0 for _ in range(len(A))]

        if self.isValid(A, 1, 0):
            dp[1] = 2

        i = 2
        while i < len(A):
            if A[i] in [')', '}', ']']:
                if self.isValid(A, i, i-1):
                    dp[i] = dp[i-2] + 2
                elif A[i-1] in [')', '}', ']'] and dp[i-1] > 0:
                    if self.isValid(A, i, i-dp[i-1]-1):
                        dp[i] = dp[i-dp[i-1]-2] + dp[i-1] + 2
            
            i += 1

        return max(dp)