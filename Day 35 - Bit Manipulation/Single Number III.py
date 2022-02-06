"""
Problem Description
Given an array of numbers A , in which exactly two elements appear only once and all the other elements appear exactly
twice. Find the two elements that appear only once.
Note: Output array must be sorted.


Problem Constraints
2 <= |A| <= 100000
1 <= A[i] <= 109


Input Format
First argument is an array of interger of size N.


Output Format
Return an array of two integers that appear only once.


Example Input
Input 1:
A = [1, 2, 3, 1, 2, 4]

Input 2:
A = [1, 2]


Example Output
Output 1:
[3, 4]

Output 2:
[1, 2]


Example Explanation
Explanation 1:
 3 and 4 appear only once.

Explanation 2:
 1 and 2 appear only once.
"""

"""
Solution Approach
If extra memory is used, we can directly store the count and find the elements which occur only once.

To solve without extra memory
We can use the xor operation , as the xor of two elements gives 0. Take the xor of all the elements of the array. Elements
which occurs twice will not contribute anything to the xor value.

Suppose that the ith bit is set in the xor value which means that exactly one of the two required number has that bit set.

If we the divide the array elements int two groups: one group contain all elements which have the ith bit set and the other group
conatins elements which have 0 at the ith bit.

Each group contains one of the two required numbers and for other numbers both of their occurrences will be in the same group.

Now, Xor of elements in the first group gives a number which occurs exactly once.
Xor of elements in the second group gives another number which occurs exactly once.
"""

class Solution:

    def solve(self, A):

        n = A[0]
        for i in range(1, len(A)):
            n = n ^ A[i]

        i = 0
        while n:
            if n & 1 == 1:
                n1, n2 = 0, 0
                for val in A:
                    if (val >> i) & 1 == 1:
                        n1 = n1 ^ val
                    else:
                        n2 = n2 ^ val
                break

            i += 1
            n = n >> 1

        if n1 > n2:
            return [n2, n1]

        return [n1, n2]


A = [1, 2, 3]
ans = Solution().solve(A)
print(ans)