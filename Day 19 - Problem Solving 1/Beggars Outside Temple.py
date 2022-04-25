"""
Problem Description
There are A beggars sitting in a row outside a temple. Each beggar initially has an empty pot. When the devotees come to
the temple, they donate some amount of coins to these beggars. Each devotee gives a fixed amount of coin(according to
their faith and ability) to some K beggars sitting next to each other.
Given the amount P donated by each devotee to the beggars ranging from L to R index, where 1 <= L <= R <= A, find out
the final amount of money in each beggar's pot at the end of the day, provided they don't fill their pots by any other
means.
For ith devotee B[i][0] = L, B[i][1] = R, B[i][2] = P, Given by the 2D array B

Problem Constraints
1 <= A <= 2 * 105
1 <= L <= R <= A
1 <= P <= 103
0 <= len(B) <= 105

Input Format
The first argument is a single integer A.
The second argument is a 2D integer array B.

Output Format
Return an array(0 based indexing) that stores the total number of coins in each beggars pot.

Example Input
Input 1:-
A = 5
B = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]

Example Output
Output 1:-
10 55 45 25 25

Example Explanation
Explanation 1:-
First devotee donated 10 coins to beggars ranging from 1 to 2. Final amount in each beggars pot after first devotee:
[10, 10, 0, 0, 0]
Second devotee donated 20 coins to beggars ranging from 2 to 3. Final amount in each beggars pot after second devotee:
[10, 30, 20, 0, 0]
Third devotee donated 25 coins to beggars ranging from 2 to 5. Final amount in each beggars pot after third devotee:
[10, 55, 45, 25, 25]
"""

"""
Solution Approach
Instead of updating each beggar ranging from i to j, we could update index i with +S and index j + 1 with -S, where S is 
a donation made by some devotee. So if you want to know the number of coins taken by kth beggar, you just need to find 
the prefix sum of all the values(coins) from 1 to k(Try to prove it by yourself that values between i to j contains +S 
as you are doing prefix sum).
Example:
N = 5, D = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
Initial array: [0, 0, 0, 0, 0]
After first devotee, if we update i = 1 with +10 and j + 1 = 3 with -10, we get [10, 0, -10, 0, 0]. Now note that if you 
add 10 to 1st index and subtract 10 with 3rd index and do a prefix sum at every array element, you will get +10 at 1st 
and 2nd.
After second devotee, if we update i = 2 with +20 and j + 1 = 4 with -20, we get [10, 20, -10, -20, 0].
Similarly, after third devotee, if we update i = 2 with +25 and j + 1 = 6 with -25, we get [10, 45, -10, -20, 0].
Now, if we calculate the prefix sum at every index, we get [10, 55, 45, 25, 25].
"""

class Solution:

    def solve(self, A, B):
        sm = 0
        ans = []
        s, e, c = [], [], []
        for d in B:
            s.append(d[0])
            e.append(d[1])
            c.append(d[2])

        i = 0
        s_idx = 0
        e_idx = 0
        while i < A:
            while s_idx < len(s) and i + 1 >= s[s_idx]:
                sm += c[s_idx]
                s_idx += 1

            ans.append(sm)

            while e_idx < len(e) and i + 1 >= e[e_idx]:
                sm -= c[e_idx]
                e_idx += 1

            i += 1

        return ans