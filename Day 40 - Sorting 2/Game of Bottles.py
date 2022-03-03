"""
Problem Description
Given an array of integers A of size N which denotes N cylindrical empty bottles. The radius of the ith bottle is A[i].
You can put the ith bottle into the jth bottle if the following conditions are met:

ith bottle is not put into another bottle.
jth bottle dosen't contain any other bottle.
The radius of bottle i is smaller than bottle j (A[i] < A[j]).
You can put bottles into each other any number of times. You want to MINIMIZE the number of visible bottles. A bottle is called visible if it is not put into any other bottle.

Find and return the minimum number of visible bottles.


Problem Constraints
1 <= N <= 100000
1<= A[i] <= 100000000


Input Format
First argument is an integer array A denoting the radius of the cyclindrical bottles.


Output Format
Return a single integer corresponding to the minimum number of visible bottles.


Example Input
Input 1:
A = [1, 2, 3]

Input 2:
A = [1, 1]


Example Output
Output 1:
 1

Output 2:
 2


Example Explanation
Explanation 1:
 In example 1 it is possible to put bottle 1 into bottle 2, and 2 into 3.

Explanation 2:
 Both bottles will be visible.
"""

"""
Solution Approach
You can always show that the answer is equal to the amount of bottles of the size appearing the most in array. Result 
can be easily obtained by constructive algorithm: take these most appearing bottles, put smaller bottles in decreasing 
order of their size into free ones (there always be space) and put resulting bottles into the larger ones in increasing 
order. You have 2 approaches to solve this problem, One uses O(n) time and O(n) space(requires a hashmap) and other uses 
O(nlogn) time and O(1) space(requires sorting).
"""

class Solution:

    def solve(self, A):
        if len(A) == 1:
            return 1

        A = sorted(A)

        i, j = 0, 1
        while j < len(A):
            if A[j] > A[i]:
                A[i] = -1
                i += 1
            j += 1

        ans = 0
        for i in A:
            if i != -1:
                ans += 1

        return ans