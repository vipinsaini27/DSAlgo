"""
Problem Description
Given two arrays, A and B of size N. A[i] represents the time by which you can buy the ith car without paying any money.

B[i] represents the profit you can earn by buying the ith car. It takes 1 minute to buy a car, so you can only buy the ith car when the current time <= A[i] - 1.

Your task is to find the maximum profit one can earn by buying cars considering that you can only buy one car at a time.

NOTE:

You can start buying from time = 0.
Return your answer modulo 109 + 7.


Problem Constraints
1 <= N <= 105
1 <= A[i] <= 109
0 <= B[i] <= 109



Input Format
The first argument is an integer array A represents the deadline for buying the cars.
The second argument is an integer array B represents the profit obtained after buying the cars.



Output Format
Return an integer denoting the maximum profit you can earn.



Example Input
Input 1:

 A = [1, 3, 2, 3, 3]
 B = [5, 6, 1, 3, 9]
Input 2:

 A = [3, 8, 7, 5]
 B = [3, 1, 7, 19]


Example Output
Output 1:

 20
Output 2:

 30


Example Explanation
Explanation 1:

 At time 0, buy car with profit 5.
 At time 1, buy car with profit 6.
 At time 2, buy car with profit 9.
 At time = 3 or after , you can't buy any car, as there is no car with deadline >= 4.
 So, total profit that one can earn is 20.
Explanation 2:

 At time 0, buy car with profit 3.
 At time 1, buy car with profit 1.
 At time 2, buy car with profit 7.
 At time 3, buy car with profit 19.
 We are able to buy all cars within their deadline. So, total profit that one can earn is 30.
"""

"""
Solution Approach
If at any time we have the option to buy a car which gives more profit than any of the car already taken.

At a particular time, We can buy a car or not.

If we are able to buy all the cars, then it’s fine. If not then we should remove a car with minimum profit which we had bought earlier and take the car with more profit.

Think why this will give us maximum profit.
"""

from heapq import heappop, heappush

class Solution:
    
    def solve(self, A, B):
        mod = 10**9 + 7
        data = [[A[i], B[i]] for i in range(len(A))]

        data = sorted(data, key=lambda x: x[0])
        heap = []
        
        ans = 0
        current_time = 0
        for i in range(len(data)):
            buy_time = data[i][0]
            buy_value = data[i][1]
            if current_time < buy_time:
                ans = (ans + buy_value) % mod
                heappush(heap, buy_value)
                current_time += 1
            elif buy_value > heap[0]:
                min_value = heappop(heap)
                ans = (ans - min_value)
                ans = (ans + buy_value) % mod
                heappush(heap, buy_value)

        return ans