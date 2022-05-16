"""
Problem Description
An arithmetic expression is given by a character array A of size N. Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each character may be an integer or an operator.



Problem Constraints
1 <= N <= 105



Input Format
The only argument given is character array A.



Output Format
Return the value of arithmetic expression formed using reverse Polish Notation.



Example Input
Input 1:
    A =   ["2", "1", "+", "3", "*"]
Input 2:
    A = ["4", "13", "5", "/", "+"]


Example Output
Output 1:
    9
Output 2:
    6


Example Explanation
Explaination 1:
    starting from backside:
    * : () * ()
    3 : () * (3)
    + : (() + ()) * (3)
    1 : (() + (1)) * (3)
    2 : ((2) + (1)) * (3)
    ((2) + (1)) * (3) = 9
Explaination 2:
    + : () + ()
    / : () + (() / ())
    5 : () + (() / (5))
    13 : () + ((13) / (5))
    4 : (4) + ((13) / (5))
    (4) + ((13) / (5)) = 6
"""

"""
Solution Approach
This is pretty much a simulation problem.
Think using stack.

When you encounter an operator, that is when you need the top 2 numbers on the stack, perform the operation on them, and put them on the stack.
"""

class Solution:
    
    def evalRPN(self, A):
        operator = ["+", "-", "*", "/"]
        st = []
        i = len(A) - 1

        while i >= 0:
            if A[i] in operator or (st and st[-1] in operator):
                st.append(A[i])
            else:
                a = int(A[i])
                while st and st[-1] not in operator:
                    b = int(st.pop())
                    op = st.pop()
                    if op == "+":
                        r = a + b
                    elif op == "-":
                        r = a - b
                    elif op == "*":
                        r = a * b
                    else:
                        r = a // b
                    
                    a = r
                
                st.append(a)
            
            i -= 1

        return st[-1]