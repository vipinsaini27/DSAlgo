"""
Problem Description
You are given an array A of integers of size N.
Your task is to find the equilibrium index of the given array
The equilibrium index of an array is an index such that the sum of elements at lower indexes is equal to the sum of
elements at higher indexes.
NOTE:
Array indexing starts from 0.
If there is no equilibrium index then return -1.
If there are more than one equilibrium indexes then return the minimum index.

Problem Constraints
1 <= N <= 105
-105 <= A[i] <= 105

Input Format
First arugment is an array A .

Output Format
Return the equilibrium index of the given array. If no such index is found then return -1.

Example Input
Input 1:
A=[-7, 1, 5, 2, -4, 3, 0]
Input 2:
A=[1,2,3]

Example Output
Output 1:
3
Output 2:
-1

Example Explanation
Explanation 1:
3 is an equilibrium index, because:
A[0] + A[1] + A[2] = A[4] + A[5] + A[6]
Explanation 1:
There is no such index.
"""

"""
Solution Approach
The idea is to get the total sum of the array first. Then Iterate through the array and keep updating the left sum which 
is initialized as zero. In the loop, we can get the right sum by subtracting the elements one by one.
1) Initialize leftsum  as 0
2) Get the total sum of the array as sum
3) Iterate through the array and for each index i, do following.
    a)  Update sum to get the right sum.  
           sum = sum - arr[i] 
       // sum is now right sum
    b) If leftsum is equal to sum, then return current index. 
       // update leftsum for next iteration.
    c) leftsum = leftsum + arr[i]
4) return -1 
// If we come out of loop without returning then
// there is no equilibrium index
"""

class Solution:

    def solve(self, A):
        rSum = sum(A)
        lSum = 0

        for i in range(0, len(A)):
            rSum -= A[i]
            if lSum == rSum:
                return i
            lSum += A[i]

        return -1