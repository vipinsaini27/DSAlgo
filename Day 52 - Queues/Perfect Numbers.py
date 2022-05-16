"""
Problem Description
Given an integer A, you have to find the Ath Perfect Number.

A Perfect Number has the following properties:

It comprises only 1 and 2.

The number of digits in a Perfect number is even.

It is a palindrome number.

For example, 11, 22, 112211 are Perfect numbers, where 123, 121, 782, 1 are not.



Problem Constraints
1 <= A <= 100000



Input Format
The only argument given is an integer A.



Output Format
Return a string that denotes the Ath Perfect Number.



Example Input
Input 1:

 A = 2
Input 2:

 A = 3


Example Output
Output 1:

 22
Output 2:

 1111


Example Explanation
Explanation 1:

First four perfect numbers are:
1. 11
2. 22
3. 1111
4. 1221
Explanation 2:

First four perfect numbers are:
1. 11
2. 22
3. 1111
4. 1221
"""

"""
Solution Approach
Can you precompute the answer of all times and
then answer as the queries come in??
It appears that we can use Queue and precompute for 100000 Perfect numbers.
First insert “1” and “2” and then use s -> s+’1’
and s -> s+’2’
to fill up the queue.
"""

class Solution:
    # @param A : integer
    # @return a strings
    def solve(self, A):
        pNumbers = []
        pNumbers.insert(0, [1, 1])
        pNumbers.insert(1, [2, 2])
        s = 0
        e = 1
        while len(pNumbers) < A:
            i = 0
            e = e * 2
            while len(pNumbers) < A and s+i < e+s:
                number = pNumbers[s+i].copy()
                number.append(1)
                number.insert(0, 1)
                pNumbers.append(number)
                i += 1

            i = 0
            while len(pNumbers) < A and s+i < e+s:
                number = pNumbers[s+i].copy()
                number.append(2)
                number.insert(0, 2)
                pNumbers.append(number)
                i += 1
            
            s = e + s

        ans = 0
        for i in pNumbers[A-1]:
            ans = ans*10 + i
        return ans