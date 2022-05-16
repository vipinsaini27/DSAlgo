"""
Problem Description
Given an array of integers A.

value of a array = max(array) - min(array).

Calculate and return the sum of values of all possible subarrays of A modulo 109+7.



Problem Constraints
1 <= |A| <= 100000

1 <= A[i] <= 1000000



Input Format
The first and only argument given is the integer array A.



Output Format
Return the sum of values of all possible subarrays of A modulo 109+7.



Example Input
Input 1:

 A = [1]
Input 2:

 A = [4, 7, 3, 8]


Example Output
Output 1:

 0
Output 2:

 26


Example Explanation
Explanation 1:

Only 1 subarray exists. Its value is 0.
Explanation 2:

value ( [4] ) = 4 - 4 = 0
value ( [7] ) = 7 - 7 = 0
value ( [3] ) = 3 - 3 = 0
value ( [8] ) = 8 - 8 = 0
value ( [4, 7] ) = 7 - 4 = 3
value ( [7, 3] ) = 7 - 3 = 4
value ( [3, 8] ) = 8 - 3 = 5
value ( [4, 7, 3] ) = 7 - 3 = 4
value ( [7, 3, 8] ) = 8 - 3 = 5
value ( [4, 7, 3, 8] ) = 8 - 3 = 5
sum of values % 10^9+7 = 26
"""

"""
Solution Approach
Calculate the next greater element and previous greater element for each element in the array. Each element Ai is the maximum of all subarrays starting at (previous greater element)i + 1 to (next greater element)i - 1.

Similarly, the next smaller element and previous smaller element can be used for minimum values of subarrays

Time Complexity:- O(N)
"""

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        max_sum, min_sum = 0, 0
        ans = 0
        i = 0
        while i < len(A):
            val = A[i]
            rSMax, lSMax, rSMin, lSMin = 0, 0, 0, 0
            j = i - 1
            while j >= 0 and val > A[j]:
                j -= 1
                lSMax += 1
            
            j = i + 1
            while j < len(A) and val > A[j]:
                j += 1
                rSMax += 1

            j = i - 1
            while j >= 0 and val < A[j]:
                j -= 1
                lSMin += 1
            
            j = i + 1
            while j < len(A) and val < A[j]:
                j += 1
                rSMin += 1

            max_sum = (val*(rSMax*lSMax + rSMax + lSMax + 1))
            min_sum = (val*(rSMin*lSMin + rSMin + lSMin + 1))

            ans = (ans + (max_sum - min_sum)) % (10**9 + 7)

            i += 1

        return ans