"""
Problem Description

Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 < index2.
Please note that your returned answers (both index1 and index2 ) are not zero-based. Put both these numbers in order in
an array and return the array from your function ( Looking at the function signature will make things clearer ). Note
that, if no pair exists, return empty list.

If multiple solutions exist, output the one where index2 is minimum. If there are multiple solutions with the minimum
index2, choose the one with minimum index1 out of them.

Input: [2, 7, 11, 15], target=9
Output: index1 = 1, index2 = 2
"""

"""
Solution Approach
Have you checked cases where the element you are looking up in the map is same as the curValue.

For example, consider the following cases :

A:[4 4] target : 8
and A :[3 4] target : 8

The answer in first case should be [1 2] and in second case, it should be empty.
"""

class Solution:

    def twoSum(self, A, B):
        ans = []

        hash = {}
        for i in range(len(A)):
            if A[i] not in hash.keys():
                hash[A[i]] = []

            hash[A[i]].append(i)

        for i in range(len(A)):
            rem = B - A[i]
            if rem in hash.keys():
                j = 0
                while j < len(hash[rem]) - 1 and hash[rem][j] <= i:
                    j += 1
                if hash[rem][j] > i:
                    if len(ans) == 0:
                        ans = [i + 1, hash[rem][j] + 1]
                    elif hash[rem][j] + 1 < ans[1]:
                        ans = [i + 1, hash[rem][j] + 1]
                    elif hash[rem][j] + 1 == ans[1] and i < ans[0]:
                        ans = [i + 1, hash[rem][j] + 1]

        return ans