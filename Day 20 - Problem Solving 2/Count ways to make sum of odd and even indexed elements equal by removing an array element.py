"""
Problem Description
Given an array, arr[] of size N, the task is to find the count of array indices such that removing an element from these
indices makes the sum of even-indexed and odd-indexed array elements equal.

Problem Constraints
1 <= n <= 105
-105 <= A[i] <= 105

Input Format
First argument contains an array A of integers of size N

Output Format
Return the count of array indices such that removing an element from these indices makes the sum of even-indexed and odd-indexed array elements equal.

Example Input
Input 1:
A=[2, 1, 6, 4]
Input 2:
A=[1, 1, 1]

Example Output
Output 1:
1
Output 2:
3

Example Explanation
Explanation 1:
Removing arr[1] from the array modifies arr[] to { 2, 6, 4 } such that, arr[0] + arr[2] = arr[1].
Therefore, the required output is 1.
Explanation 2:
Removing arr[0] from the given array modifies arr[] to { 1, 1 } such that arr[0] = arr[1]
Removing arr[1] from the given array modifies arr[] to { 1, 1 } such that arr[0] = arr[1]
Removing arr[2] from the given array modifies arr[] to { 1, 1 } such that arr[0] = arr[1]
Therefore, the required output is 3.
"""

"""
Solution Approach
based on the observation that removing any element from the given array makes even indices of succeeding elements as odd 
and odd indices of the succeeding elements as even. Follow the steps below to solve the problem:
Initialize two variables, say evenSum and oddSum,
 to store the sum of odd-indexed and even-indexed elements of the given array respectively.
Traverse the array using variable i.
Remove every ith element of the array and update the sum of the remaining even-indexed elements 
and the odd-indexed elements based on the above observation. Check if the sums are equal or not. 
If found to be true, then increment the count.
Finally, print the count obtained.
"""

class Solution:

    def solve(self, A):
        evenSum, oddSum = 0, 0
        ans = 0
        for i in range(0, len(A)):
            if i % 2 == 0:
                evenSum += A[i]
            else:
                oddSum += A[i]

        Lodd, Leven = 0, 0
        for i in range(0, len(A)):
            Rodd = evenSum - Leven
            Reven = oddSum - Lodd

            if i % 2 == 0:
                Rodd -= A[i]
            else:
                Reven -= A[i]

            if Lodd + Rodd == Leven + Reven:
                ans += 1

            if i % 2 == 0:
                Leven += A[i]
            else:
                Lodd += A[i]

        return ans