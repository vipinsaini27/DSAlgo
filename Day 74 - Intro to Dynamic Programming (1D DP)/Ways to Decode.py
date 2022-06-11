"""
Problem Description
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message denoted by string A containing digits, determine the total number of ways to decode it modulo 109 + 7.



Problem Constraints
1 <= length(A) <= 105



Input Format
The first and the only argument is a string A.



Output Format
Return an integer, representing the number of ways to decode the string modulo 109 + 7.



Example Input
Input 1:

 A = "12"
Input 2:

 A = "8"


Example Output
Output 1:

 2
Output 2:

 1


Example Explanation
Explanation 1:

 Given encoded message "8", it could be decoded as only "H" (8).
 The number of ways decoding "8" is 1.
Explanation 2:

 Given encoded message "12", it could be decoded as "AB" (1, 2) or "L" (12).
 The number of ways decoding "12" is 2.
"""

"""
Solution Approach
Lets first look at the bruteforce solution.
It only makes sense to look at 1 digit or 2 digit pairs ( as 3 digit sequence will be greater than 26 ).

So, when looking at the start of the string, we can either form a one digit code, and then look at the ways of forming the rest of the string of length L - 1, or we can form 2 digit code if its valid and add up the ways of decoding rest of the string of length L - 2.
This obviously is exponential.

The code would go something like the following :

 int ways(string &s, int startIndex) {
    // BASE CASES

    int answer = 0;
if (isValid(s[startIndex])) answer += ways(s, startIndex + 1);
    if (isValid(s[startIndex] + s[startIndex + 1])) answer += ways(s, startIndex + 2);
    return answer;
 }
Note that in this case, startIndex can only take L number of values. Can you use the fact to store the result so that the function processing does not happen so many times ?
"""

class Solution:
    
    def numDecodings(self, A):
        if A[0] == '0':
            return 0
        
        if len(A) == 1:
            return 1
        
        dp = []
        if A[0] != '0':
            dp.append(1)
        else:
            return 0

        if A[1] != '0':
            if int(A[0:2]) < 27:
                dp.append(2)
            else:
                dp.append(1)
        elif int(A[0:2]) < 27:
            dp.append(1)
        else:
            dp.append(0)

        i = 2
        while i < len(A):
            if A[i] != '0':
                if A[i-1] != '0':
                    if int(A[i-1:i+1]) < 27:
                        dp.append((dp[-1] + dp[-2])%(10**9+7))
                    else:
                        dp.append(dp[-1])
                else:
                    dp.append(dp[-1])
            elif A[i-1] != '0':
                if int(A[i-1:i+1]) < 27:
                    dp.append(dp[-2])
                else:
                    return 0
            else:
                return 0
            
            i += 1

        return dp[-1]