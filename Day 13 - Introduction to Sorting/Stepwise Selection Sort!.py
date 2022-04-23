"""
Problem Description
Given an integer array A of size N.
You need to sort the elements in increasing order using SelectionSort. Return a array containing the min value's index
position before every iteration.
NOTE:
Consider 0 based indexing while looking for min value in each step of selection sort.
There will be total N - 1 iterations in selection sort so the output array will contain N - 1 integers.


Problem Constraints
2 <= N <= 104
1 <= A[i] <= 106
All elements are distinct in array A.


Input Format
First and only argument is an integer array A.


Output Format
Return an integer array containing N - 1 integers denoting min value's index position before every iteration.


Example Input
Input 1:
 A = [6, 4, 3, 7, 2, 8]


Example Output
Output 1:
 [4, 2, 2, 4, 4]


Example Explanation
Explanation 1:
 Explanation : 6 4 3 7 2 8 : Index of 1st min - 4
 After 1st Iteration : 2 4 3 7 6 8 : Index of 2nd min - 2
 After 2nd Iteration : 2 3 4 7 6 8 : Index of 3rd min - 2
 After 3rd Iteration : 2 3 4 7 6 8 : Index of 4th min - 4
 After 4th iteration : 2 3 4 6 7 8 : Index of 5th min - 4
 After 5th iteration. : 2 3 4 6 7 8.
"""

"""
Solution Approach
The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from 
unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.

The subarray which is already sorted.
Remaining subarray which is unsorted.
In every iteration of selection sort, the minimum element (considering ascending order) from the unsorted subarray is 
picked and moved to the sorted subarray.
Time Complexity: O(N2) as there are two nested loops.

Auxiliary Space: O(1)
The good thing about selection sort is it never makes more than O(n) swaps and can be useful when memory write is a 
costly operation.
"""

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        ans = []
        for i in range(len(A) - 1):
            mn = A[i]
            mn_idx = i
            for j in range(i + 1, len(A)):
                if A[j] < mn:
                    mn = A[j]
                    mn_idx = j

            ans.append(mn_idx)
            A[i], A[mn_idx] = A[mn_idx], A[i]

        return ans