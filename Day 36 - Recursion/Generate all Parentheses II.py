"""
Problem Description
Given an integer A pairs of parentheses, write a function to generate all combinations of well-formed parentheses of length 2*A.


Problem Constraints
1 <= A <= 20


Input Format
First and only argument is integer A.


Output Format
Return a sorted list of all possible paranthesis.


Example Input
Input 1:
A = 3

Input 2:
A = 1


Example Output
Output 1:
[ "((()))", "(()())", "(())()", "()(())", "()()()" ]

Output 2:
[ "()" ]


Example Explanation
Explanation 1:
 All paranthesis are given in the output list.

Explanation 2:
 All paranthesis are given in the output list.
"""

"""
Solution Approach
Again, think recursion.
At every step, you have 2 options :
1) Add ‘(‘ to the string.
2) Add ‘)’ to the string.
However, you need to make sure, that the number of closing brackets do not exceed number of opening brackets at any point of time.
Also, make sure that the number of opening brackets never exceeds n.
"""

class Solution:

    def fun(self, A, st, p, ans):
        if p < A:
            s = ''
            i = len(st) - 1
            while i > 0:
                ans = self.fun(A, st + '(' + s + ')', p + 1, ans)
                stack = [st[i]]
                i -= 1
                while i >= 0 and stack:
                    if st[i] == ')':
                        stack.append(')')
                    else:
                        stack.pop()
                    i -= 1

                s = st[i + 1:] + s
                st = st[:i + 1]

            ans = self.fun(A, st + '(' + s + ')', p + 1, ans)
        else:
            ans.append(st)

        return ans

    def generateParenthesis(self, A):
        ans = self.fun(A, '()', 1, [])

        ans = sorted(ans)

        return ans
