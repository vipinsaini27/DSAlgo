"""
Problem Description
Given an index k, return the kth row of the Pascal's triangle.
Pascal's triangle: To generate A[C] in row R, sum up A'[C] and A'[C-1] from previous row R - 1.

Example:
Input : k = 3
Return : [1,3,3,1]
Note: k is 0 based. k = 0, corresponds to the row [1].
Note: Could you optimize your algorithm to use only O(k) extra space?
"""

"""
Solution Approach
Did you account for base cases like numRows = 0, numRows = 1 ?
Take a look at how we can approach this problem.
Notice that the first and last numbers in each row ( for row >= 2 ) are 1 and 1.
For all the other numbers:
num at position i = number at position i in prev row + number at position (i + 1) in previous row.
Also, notice that for a row, you only need the value in the previous rows.
The values in i-2 row do not matter.
As such, all you need is to maintain 2 vectors and alternate between them.
"""

class Solution:

    def getRow(self, K):
        ans = [1]

        if K == 0:
            return ans

        for i in range(1, K+1):
            rowLength = len(ans)
            mid = rowLength//2

            j = mid
            while j > 0:
                ans[j] = ans[j] + ans[j-1]
                j -= 1

            if rowLength%2 == 0:
                x = mid-1
                y = mid+1
            else:
                x = mid
                y = mid+1

            while x >= 0:
                if y >= len(ans):
                    ans.append(ans[x])
                else:
                    ans[y] = ans[x]
                y += 1
                x -= 1

        return ans