"""
Problem Description
Given a array of integers A of size N and an integer B.
Return number of non-empty subsequences of A of size B having sum <= 1000.


Problem Constraints
1 <= N <= 20
1 <= A[i] <= 1000
1 <= B <= N


Input Format
The first argument given is the integer array A.
The second argument given is the integer B.


Output Format
Return number of subsequences of A of size B having sum <= 1000.


Example Input
Input 1:
    A = [1, 2, 8]
    B = 2

Input 2:
    A = [5, 17, 1000, 11]
    B = 4


Example Output
Output 1:
3

Output 2:
0

Example Explanation
Explanation 1:
 {1, 2}, {1, 8}, {2, 8}

Explanation 1:
 No valid subsequence
"""

"""
Solution Approach
For N <= 20, we can use recursion technique to count all non-empty subsequences of A of size B having sum <= 1000.

initialize ans = 0
Consider we are at ith index with: current sum of subsequence = curSum
current size of subsequence = curSize

if (curSize == B && curSum <= 1000)
    increment the ans;
else
    for(int j = i+1; j<A.size();j++){
        Add the jth element to the current subsequence
        and recur for the next index with curSum = curSum + A[j]
                                          curSize = curSize + 1
    } 
"""


class Solution:

    def solve(self, A, B, s=0, ans=0, i=0):
        while i < len(A):
            s += A[i]
            if B > 1:
                ans = self.solve(A, B - 1, s, ans, i + 1)
            elif s <= 1000:
                ans += 1

            s -= A[i]
            i += 1

        return ans