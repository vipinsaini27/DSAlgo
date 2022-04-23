"""
Problem Description
Given an array A of non-negative integers, arrange them such that they form the largest number.
Note: The result may be very large, so you need to return a string instead of an integer.


Problem Constraints
1 <= len(A) <= 100000
0 <= A[i] <= 2*109


Input Format
The first argument is an array of integers.


Output Format
Return a string representing the largest number.


Example Input
Input 1:
 A = [3, 30, 34, 5, 9]

Input 2:
 A = [2, 3, 9, 0]


Example Output
Output 1:
 "9534330"

Output 2:
 "9320"


Example Explanation
Explanation 1:
Reorder the numbers to [9, 5, 34, 3, 30] to form the largest number.

Explanation 2:
Reorder the numbers to [9, 3, 2, 0] to form the largest number 9320.
"""

"""
Solution Approach
Sorting all numbers in descending order is the simplest solution that occurs to us. But this doesn’t work. 
For example, 548 is greater than 60, but in the output, 60 comes before 548. As a second example, 98 is greater than 9, 
but 9 comes before 98 in the output.
The solution is to use any comparison-based sorting algorithm. Thus, instead of using the default comparison, write a 
comparison function myCompare() and use it to sort numbers. 
Given two numbers, X and Y, how should myCompare() decide which number to put first – we compare two numbers XY (Y 
appended at the end of X) and YX (X appended at the end of Y). 
If XY is greater, then, in the output, X should come before Y, else Y should come before X. 
For example, let X and Y be 542 and 60. To compare X and Y, we compare 54260 and 60542. Since 60542 is greater than 
54260, we put Y first.
"""

class Solution:

    def largestNumber(self, A):
        A = list(A)
        A = sorted(A, key=lambda x: x / (10 ** len(str(x)) - 1), reverse=True)
        ans = ''
        if A[0] == 0:
            ans = '0'
        else:
            ans = ''.join(str(x) for x in A)

        return ans