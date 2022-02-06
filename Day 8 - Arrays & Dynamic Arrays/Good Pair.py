"""
Problem Description
Given an array A and a integer B. A pair(i,j) in the array is a good pair if i!=j and (A[i]+A[j]==B). Check if any good pair exist or not.


Problem Constraints
1 <= A.size() <= 104
1 <= A[i] <= 109
1 <= B <= 109


Input Format
First argument is an integer array A.
Second argument is an integer B.


Output Format
Return 1 if good pair exist otherwise return 0.


Example Input
Input 1:
A = [1,2,3,4]
B = 7

Input 2:
A = [1,2,4]
B = 4

Input 3:
A = [1,2,2]
B = 4


Example Output
Output 1:
1

Output 2:
0

Output 3:
1


Example Explanation
Explanation 1:
 (i,j) = (3,4)

Explanation 2:
No pair has sum equal to 4.

Explanation 3:
 (i,j) = (2,3)
"""

"""
Solution Approach
For every i run a loop of j and check if A[i]+A[j]==B or not. Also, check if i!=j.
"""

class Solution:

    def solve(self, A, B):
        hash = {}

        if len(A) == 1 and A[0] == B:
            return 1

        for i in range(0, len(A)):
            if A[i] not in hash.keys():
                hash[A[i]] = 0

            hash[A[i]] += 1

        for i in range(0, len(A)):
            rem = int(abs(A[i] - B))
            if rem in hash.keys():
                if rem == A[i] and hash[rem] > 1:
                    return 1
                elif rem != A[i]:
                    return 1

        return 0