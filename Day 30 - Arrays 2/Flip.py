"""
Problem Description
You are given a binary string A(i.e., with characters 0 and 1) consisting of characters A1, A2, 
..., AN. In a single operation, you can choose two indices, L and R, such that 1 ≤ L ≤ R ≤ N 
and flip the characters AL, AL+1, ..., AR. By flipping, we mean changing character 0 to 1 and 
vice-versa.
Your aim is to perform ATMOST one operation such that in the final string number of 1s is 
maximized.
If you don't want to perform the operation, return an empty array. Else, return an array 
consisting of two elements denoting L and R. If there are multiple solutions, return the 
lexicographically smallest pair of L and R.
NOTE: Pair (a, b) is lexicographically smaller than pair (c, d) if a < c or, if a == c and b < 
d.

Problem Constraints
1 <= size of string <= 100000

Input Format
First and only argument is a string A.

Output Format
Return an array of integers denoting the answer.

Example Input
Input 1:
A = "010"
Input 2:
A = "111"

Example Output
Output 1:
[1, 1]
Output 2:
[]

Example Explanation
Explanation 1:
A = "010"
Pair of [L, R] | Final string
_______________|_____________
[1 1]          | "110"
[1 2]          | "100"
[1 3]          | "101"
[2 2]          | "000"
[2 3]          | "001"
We see that two pairs [1, 1] and [1, 3] give same number of 1s in final string. So, we return 
[1, 1].
Explanation 2:
No operation can give us more than three 1s in final string. So, we return empty array [].
"""

"""
Solution Approach
Note the net change in the number of 1s in string S when we flip bits of string S.
Say it has A 0s and B 1s. Eventually, there are B 0s and A 1s.

So, the number of 1s increased by A - B. We want to choose a subarray that maximizes this. Note 
that if we change 1s to -1, the sum of values will give us A - B. Then, we have to find a 
subarray with the maximum sum, which can be done via Kadane’s Algorithm.
"""

class Solution:
    # @param A : string
    # @return a list of integers
    def flip(self, A):
        s = [0]*len(A)
        oneCount = [0]*len(A)
        zeroCount = [0]*len(A)

        ans = []
        diff = 0

        i = 0
        while i < len(A) and A[i] == "0":
            s[i] = i+1
            zeroCount[i] = i+1
            diff = s[i]
            ans = [1, i+1]
            i += 1

        if i < len(A):
            s[i] = i-1
            minIdx = i
            oneCount[i] = 1
            zeroCount[i] = i
            diff = i

        i += 1
        while i < len(A):
            if A[i] == "1":
                s[i] = s[i-1] - 1
                oneCount[i] = oneCount[i-1] + 1
                zeroCount[i] = zeroCount[i-1]

                if s[minIdx] > s[i]:
                    minIdx = i
            else:
                s[i] = s[i-1] + 1
                oneCount[i] = oneCount[i-1]
                zeroCount[i] = zeroCount[i-1] + 1

                if oneCount[i] < zeroCount[i]:
                    if zeroCount[i] - oneCount[i] > diff:
                        ans = [1, i+1]
                        diff = zeroCount[i] - oneCount[i]
                if oneCount[i]-oneCount[minIdx] < zeroCount[i]-zeroCount[minIdx]:
                    zero = zeroCount[i]-zeroCount[minIdx]
                    one = oneCount[i]-oneCount[minIdx]
                    if zero - one > diff:
                        ans = [minIdx+2, i+1]
                        diff = zero - one

            i += 1

        return ans