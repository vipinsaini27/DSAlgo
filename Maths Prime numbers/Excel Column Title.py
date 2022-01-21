'''
Problem Description
Given a positive integer A, return its corresponding column title as appear in an Excel sheet.

For example:
    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB


Problem Constraints
1 <= A <= 109


Input Format
First and only argument of input contains single integer A


Output Format
Return a string denoting the corresponding title.


Example Input
Input 1:
A = 3

Input 2:

A = 27


Example Output
Output 1:
"C"

Output 2:
"AA"


Example Explanation
Explanation 1
3 corrseponds to C.

Explanation 2:
    1 -> A,
    2 -> B,
    3 -> C,
    ...
    26 -> Z,
    27 -> AA,
    28 -> AB
'''



class Solution:
    c = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H", 9: "I", 10:"J",
         11: "K", 12: "L", 13: "M", 14: "N", 15: "O", 16: "P", 17: "Q", 18: "R", 19: "S",
         20: "T", 21: "U", 22: "V", 23: "W", 24: "X", 25: "Y", 26: "Z"}

    def convertToTitle(self, A):
        ans = ""
        while A:
            p = A % 26
            if p == 0:
                ans = "Z" + ans
                A = (A // 26) - 1
            else:
                ans = self.c[p] + ans
                A = A // 26

        return ans