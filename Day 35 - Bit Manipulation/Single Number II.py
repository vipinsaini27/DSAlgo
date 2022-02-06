"""
Problem Description
Given an array of integers, every element appears thrice except for one which occurs once.
Find that element which does not appear thrice.
NOTE: Your algorithm should have a linear runtime complexity.
Could you implement it without using extra memory?


Problem Constraints
2 <= A <= 5*106
0 <= A <= INTMAX


Input Format
First and only argument of input contains an integer array A.


Output Format
Return a single integer.


Example Input
Input 1:
 A = [1, 2, 4, 3, 3, 2, 2, 3, 1, 1]

Input 2:
 A = [0, 0, 0, 1]


Example Output
Output 1:
 4

Output 2:
 1


Example Explanation
Explanation 1:
 4 occurs exactly once in Input 1.
 1 occurs exactly once in Input 2.
"""

"""
Solution Approach
Having noticed that if X has 1 in that position, we will have 3x+1 number of 1s in that position. If X has 0 in that 
position, we will have 3x+1 number of 0 in that position.

A straightforward implementation is to use an array of size 32 to keep track of the total count of ith bit.

We can improve this based on the previous solution using three bitmask variables:

ones as a bitmask to represent the ith bit had appeared once.
twos as a bitmask to represent the ith bit had appeared twice.
threes as a bitmask to represent the ith bit had appeared three times.
When the ith bit had appeared for the third time, clear the ith bit of both ones and twos to 0. The final answer will be 
the value of ones.
"""

class Solution:

    def singleNumber(self, A):
        A = list(A)
        ans = 0
        l = len(A)
        p = 0

        while True:
            isAllZero = 1

            cnt = 0
            for i in range(l):
                if A[i]:
                    isAllZero = 0
                    if A[i] & 1 == 1:
                        cnt += 1

                    A[i] = A[i] >> 1

            if isAllZero:
                break

            if cnt % 3:
                ans = (ans + 2**p)

            p += 1

        return ans


A = [0, 0, 0, 1]
ans = Solution().singleNumber(A)
print(ans)