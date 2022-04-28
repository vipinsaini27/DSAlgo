"""
Problem Description
You are given an array A having N integers.
You have to divide / split the array into 2 subsequence partitions such that:
Both the partitions are non-empty.
Each integer A[i] in the array belongs to exactly one of the two partitions.
Absolute difference between the maximum of first partition and the minimum of second partition is minimum possible.
If B and C represent the two partitions, then size(B) >= 1, size(C) >= 1 and |max(B) - min(C)| is minimum possible. You
have to find such a spliting and tell the minimum value of |max(B) - max(C)|.

Problem Constraints
2 <= N <= 105
-109 <= A[i] <= 109

Input Format
First and only argument is an integer array A.

Output Format
Return a single integer denoting the absolute difference.

Example Input
Input 1:
 A = [3, 1, 2, 6, 4]
Input 2:
 A = [2, 1, 3, 2, 4, 3]

Example Output
Output 1:
 1
Output 2:
 0

Example Explanation
Explanation 1:
 B = [1, 2, 4]
 C = [3, 6]
 max(B) = 4, min(C) = 3
 abs(max(B) - min(C)) = abs(4 - 3) = abs(1) = 1
Explanation 2:
 B = [2, 1]
 C = [3, 2, 4, 3]
 max(B) = 2, min(C) = 2
 abs(max(B) - min(C)) = abs(2 - 2) = abs(0) = 0
"""

"""
Solution Approach
Let’s found two values a and b (value a is not greater than value b), which have the minimal modulus of the difference 
of their values.
Obviously, we cannot get an answer less than this. Let’s show how to get the partition with exactly this answer.
Sort the array by values. Our two values will stand in neighboring positions (otherwise, we can decrease the answer). 
Let the first partition contain all values who stand on positions not further than a’s position, and the second 
partition contains other values. We got a partition, in which the value a is maximal in the first partition, and value b 
is minimal in the second partition.
"""

import math
class Solution:
    def solve(self, A):
        A.sort()
        ans = math.inf

        for i in range(1, len(A)):
            if abs(A[i] - A[i-1]) < ans:
                ans = abs(A[i] - A[i-1])

        return ans