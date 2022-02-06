"""
Problem Description
Implement the next permutation, which rearranges numbers into the numerically next greater permutation of numbers for a given array A of size N.

If such arrangement is not possible, it must be rearranged as the lowest possible order i.e., sorted in an ascending order.

NOTE:
The replacement must be in-place, do not allocate extra memory.
DO NOT USE LIBRARY FUNCTION FOR NEXT PERMUTATION.


Problem Constraints
1 <= N <= 5 * 105
1 <= A[i] <= 109


Input Format
The first and the only argument of input has an array of integers, A.


Output Format
Return an array of integers, representing the next permutation of the given array.


Example Input
Input 1:
 A = [1, 2, 3]

Input 2:
 A = [3, 2, 1]


Example Output
Output 1:
 [1, 3, 2]

Output 2:
 [1, 2, 3]


Example Explanation
Explanation 1:
 Next permutaion of [1, 2, 3] will be [1, 3, 2].

Explanation 2:
 No arrangement is possible such that the number are arranged into the numerically next greater permutation of numbers.
 So will rearranges it in the lowest possible order.
"""

"""
Solution Approach
It might help to write down the next permutation on paper to see how and when the sequence changes.

You’ll realize the following pattern :

The suffix which gets affected is in a descending order before the change.

A swap with the smaller element happens and then we reverse the affected suffix.

    1 2 3 -> 1 3 2   // Suffix being just the 3. 

    1 2 3 6 5 4  -> 1 2 4 3 5 6 // Suffix being 6 5 4 in this case. 
"""

class Solution:

    def nextPermutation(self, A):
        l = len(A)
        i = l - 1
        while i > 0 and A[i-1] > A[i]:
            i -= 1

        if i == 0:
            j = l - 1
        else:
            j = i
            i -= 1

            while j < l and A[i] < A[j]:
                j += 1

            j -= 1
            A[i], A[j] = A[j], A[i]
            i += 1
            j = l - 1

        while i < j:
            A[i], A[j] = A[j], A[i]
            i += 1
            j -= 1

        return A