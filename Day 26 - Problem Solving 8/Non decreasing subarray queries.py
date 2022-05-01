"""
Problem Description
Given an array A of size N. You will be given M queries to process. Each query will be of the form B[i][0] B[i][1].
If the subarray from B[i][0] to B[i][1] is non decreasing, the output should be 1 else output should be 0.
Return an array of integers answering each query.

Problem Constraints
1 <= N <= 105
1 <= A[i] <= 109
1 <= M <= 105
1 <= B[i][0], B[i][1] <= N

Input Format
First argument contains the array A.
Second argument contains B, denoting the queries.

Output Format
Return an array of integers consisting of 0 and 1

Example Input
Input :
A = [1, 7, 3, 4, 9]
B = [
      [1, 2],
      [2, 4]
    ]

Example Output
Output :
[1, 0]

Example Explanation
Explanation :
Query 1: The subarray in the range [1, 2] is {1, 7} which is non-decreasing. Therefore, ans = 1
Query 2: The subarray in the range [2, 4] is {7, 3, 4, 9} which is not non-decreasing. Therefore, ans = 0
"""

"""
Solution Approach
If we want to prove that some subarray is actually not non-decreasing then all we need that is there should be atleast 
one irregularity. Irregularity can be defined as if for some i, A[i]>A[i+1]. That means the subarray was not 
non-decreasing.
We can create a new array where if arr[i] is 1 then it will mean that A[i]>A[i+1], that means it was an irregularity. 
Now we need to find whether there is some arr[i] = 1 for i between l and r-1.
We can create a prefix array that stores the sum of these irregularities. If there is even a single irregularity between 
l and r then ans will be 0.
We can find the sum of irregularities as pre[r-1]-pre[l-1].
Here note that we are not taking the arr[r] value because A[r+1] is not our concern.
"""

class Solution:

    def solve(self, A, B):
        ans = []
        for q in B:
            s = q[0]-1
            e = q[1]-1
            is_valid = True
            for i in range(s+1, e+1):
                if A[i] < A[i-1]:
                    ans.append(0)
                    is_valid = False
                    break
            if is_valid:
                ans.append(1)

        return ans
