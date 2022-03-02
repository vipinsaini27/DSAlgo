"""
Problem Description
Given an array A of non-negative integers of size N. Find the minimum sub-array Al, Al+1 ,…, Ar such that if we sort(in
ascending order) that sub-array, then the whole array should get sorted. If A is already sorted, output -1.


Problem Constraints
1 <= N <= 1000000
1 <= A[i] <= 1000000


Input Format
First and only argument is an array of non-negative integers of size N.


Output Format
Return an array of length 2 where First element denotes the starting index(0-based) and second element denotes the
ending index(0-based) of the sub-array. If the array is already sorted, return an array containing only one element
i.e. -1.


Example Input
Input 1:
A = [1, 3, 2, 4, 5]

Input 2:
A = [1, 2, 3, 4, 5]


Example Output
Output 1:
[1, 2]

Output 2:
[-1]


Example Explanation
Explanation 1:
If we sort the sub-array A1, A2, then the whole array A gets sorted.

Explanation 2:
A is already sorted.
"""

"""
Solution Approach
Assume that Al, …, Ar is the minimum-unsorted-subarray which is to be sorted.
then min(Al, …, Ar) >= max(A0, …, Al-1)
and max(Al, …, Ar) <= min(Ar+1, …, AN-1)
You can use this to observe and solve.
How would you solve now?
You can use 2 pointer technique to solve this question.
"""

class Solution:

    def subUnsort(self, A):
        i = 0
        a, b = None, None
        while i < len(A) - 1:
            if A[i] > A[i+1]:
                if a is None and b is None:
                    a = A[i + 1]
                    b = A[i]
                else:
                    if A[i+1] < a:
                        a = A[i + 1]
                    if A[i] > b:
                        b = A[i]

            i += 1

        if a is None and b is None:
            return [-1]

        ai = 0
        while ai < len(A) and a >= A[ai]:
            ai += 1

        bi = len(A) - 1
        while bi >= 0 and b <= A[bi]:
            bi -= 1

        if ai < bi:
            return [ai, bi]

        return [-1]