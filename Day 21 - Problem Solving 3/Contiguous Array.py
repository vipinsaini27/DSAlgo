"""
Given an array of integers A consisting of only 0 and 1.
Find the maximum length of a contiguous subarray with equal number of 0 and 1.

Input Format
The only argument given is the integer array A.

Output Format
Return the maximum length of a contiguous subarray with equal number of 0 and 1.

Constraints
1 <= length of the array <= 100000
0 <= A[i] <= 1

For Example
Input 1:
    A = [1, 0, 1, 0, 1]
Output 1:
    4
    Explanation 1:
        Subarray from index 0 to index 3 : [1, 0, 1, 0]
        Subarray from index 1 to index 4 : [0, 1, 0, 1]
        Both the subarrays have equal number of ones and equal number of zeroes.

Input 2:
    A = [1, 1, 1, 0]
Output 2:
    2
"""

"""
Solution Approach
Let Sum be the cumulative sum till ith index (after assuming 0 as -1).
Use hashmap h to store the first index of cumulative sum.
initialse h[0] = -1 (As if there were no elements then sum is 0).
Initialize ans = 0;
loop through A and find cumulative sum X_i for each index i , whenever you find there is cumulative sum with value X_i 
already exists in the hashmap h
update ans=ams(Ans,i- h[X_i]).
else update the entry in hashmap i.e. h[X_i] = i.
"""

class Solution:

    def solve(self, A):
        hash = {}
        if A[0] == 0:
            A[0] = -1
            hash[-1] = 0
        else:
            hash[1] = 0

        ans = 0
        for i in range(1, len(A)):
            if A[i] == 1:
                A[i] = A[i-1] + 1
            else:
                A[i] = A[i-1] - 1

            if A[i] == 0:
                ans = max(ans, i+1)
            elif hash.get(A[i]) is not None:
                ans = max(ans, i - hash[A[i]])
            else:
                hash[A[i]] = i

        return ans