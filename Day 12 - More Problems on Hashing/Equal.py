"""
Problem Description
Given an array A of N integers, find the index of values that satisfy P + Q = R + S, where P, Q, R & S are integers
values in the array
Expected time complexity O(N2)
NOTE:
1) Return the indices `A1 B1 C1 D1`, so that
  A[A1] + A[B1] = A[C1] + A[D1]
  A1 < B1, C1 < D1
  A1 < C1, B1 != D1, B1 != C1

2) If there are more than one solutions,
   then return the tuple of values which are lexicographical smallest.

Assume we have two solutions
S1 : A1 B1 C1 D1 ( these are values of indices in the array )
S2 : A2 B2 C2 D2

S1 is lexicographically smaller than S2 if:
  A1 < A2 OR
  A1 = A2 AND B1 < B2 OR
  A1 = A2 AND B1 = B2 AND C1 < C2 OR
  A1 = A2 AND B1 = B2 AND C1 = C2 AND D1 < D2
If no solution is possible, return an empty list.



Problem Constraints
1 <= N <= 1000
0 <= A[i] <= 1000


Input Format
First and only argument is an integer array A of length N.


Output Format
Return an array of size four which contains indices of values P, Q, R, and S.


Example Input
Input 1:
 A = [3, 4, 7, 1, 2, 9, 8]

Input 2:
 A = [2, 5, 1, 6]


Example Output
Output 1:
 [0, 2, 3, 5]

Output 2:
 [0, 1, 2, 3]


Example Explanation
Explanation 1:
 A[0] + A[2] = A[3] + A[5]
 Note: indexes returned should be 0-based.

Explanation 2:
 A[0] + A[1] = A[2] + A[3]
"""

"""
Solution Approach
Loop i = 1 to N :
    Loop j = i + 1 to N :
        calculate sum
        If in the hash table any index already exists for sum, then 
            try to find out whether it is a valid solution or not. If yes, then update the solution
        update hash table
    EndLoop;
EndLoop;
"""

class Solution:

    def equal(self, arr):
        A, B, C, D = None, None, None, None

        hash = {}

        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                val = arr[i] + arr[j]
                if hash.get(val) is None:
                    hash[val] = (i, j)
                else:
                    m, n = hash[val]
                    if m < i and n != i and n != j:
                        if A is None:
                            A, B, C, D = m, n, i, j
                        elif (m < A) or (m == A and n < B) or (m == A and n == B and i < C) or (m == A and n == B and i == C and j < D):
                            A, B, C, D = m, n, i, j

        if A is None:
            return []

        return [A, B, C, D]