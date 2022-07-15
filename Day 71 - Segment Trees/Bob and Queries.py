"""
Problem Description
Bob has an array A of N integers. Initially, all the elements of the array are zero. Bob asks you to perform Q operations on this array.

You have to perform three types of query, in each query you are given three integers x, y and z.

if x = 1: Update the value of A[y] to 2 * A[y] + 1.
if x = 2: Update the value A[y] to ⌊A[y]/2⌋ , where ⌊⌋ is Greatest Integer Function.
if x = 3: Take all the A[i] such that y <= i <= z and convert them into their corresponding binary strings. Now concatenate all the binary strings and find the total no. of '1' in the resulting string.
Queries are denoted by a 2-D array B of size M x 3 where B[i][0] denotes x, B[i][1] denotes y, B[i][2] denotes z.



Problem Constraints
1 <= N, Q <= 100000
1 <= y, z <= N
1 <= x <= 3



Input Format
The first argument has the integer A.
The second argument is a 2d matrix B, of size Q x 3, representing the queries.



Output Format
Return an array of integers where ith index represents the answer of the ith type 3 query.



Example Input
Input 1:

 A = 5
 B = [   
        [1, 1, -1]
        [1, 2, -1]
        [1, 3, -1]   
        [3, 1, 3] 
        [3, 2, 4]   
     ]
Input 2:

 A = 5
 B = [   
        [1, 1, -1]
        [1, 2, -1]
        [3, 1, 3]
        [2, 1, -1]
        [3, 1, 3]   
     ]


Example Output
Output 1:

 [3, 2]
Output 2:

 [2, 1]


Example Explanation
Explanation 1:

 Initial array A = [0, 0, 0, 0, 0]
 After query 1, A => [1, 0, 0, 0, 0]
 After query 2, A => [1, 1, 0, 0, 0]
 After query 3, A => [1, 1, 1, 0, 0]
 For query 4, Concatenation of Binary String between index 1 and 3 : 111. So, number of 1's = 3
 For query 5, Concatenation of Binary String between index 2 and 4 : 110. So, number of 1's = 2
 So, output array is [3, 2].
Explanation 2:

 Initial array A = [0, 0, 0, 0, 0]
 After query 1, A => [1, 0, 0, 0, 0]
 After query 2, A => [1, 1, 0, 0, 0]
 For query 3, Concatenation of Binary String between index 1 and 3 : 110. So, number of 1's = 2
 After query 4, A => [0, 1, 0, 0, 0]
 For query 5, Concatenation of Binary String between index 2 and 4 : 010. So, number of 1's = 1.
 So, output array is [2, 1].
"""

"""
Solution Approach
For each node in a segment tree, you could store the number of 1s in the binary representation of the numbers stored in them.

For type 1 query, the number of 1s increase by 1.
For type 2 query, the number of 1s decrease by 1 but make sure to keep them greater than or equal to 0.
For type 3 query, you can simply return a range sum query over the required indices.
"""

from math import ceil, log2

class SegmentTree():

    def __init__(self):
        self.STArr = []
        self.size = None

    def __setST(self, n):
        self.size = n
        x = (int)(ceil(log2(n)))
        max_size = 2 * (int)(2**x) - 1
        self.STArr = [None]*(max_size)

    def getST(self):
        return self.STArr

    def __constructST(self, idx, start, end):
        if start == end:
            self.STArr[idx] = 0
        else:
            mid = (start + end) // 2
            left = 2*idx + 1
            right = 2*idx + 2
            self.__constructST(left, start, mid)
            self.__constructST(right, mid+1, end)
            self.STArr[idx] = self.STArr[left] + self.STArr[right]

    def createST(self, n):
        self.__setST(n)
        self.__constructST(0, 0, n-1)

    def __sumST(self, start, end, left, right, idx):
        if start <= left and end >= right:
            return self.STArr[idx]
        if end < left or right < start:
            return 0
        
        mid = (left + right) // 2
        leftIdx = 2*idx + 1
        rightIdx = 2*idx + 2
        return self.__sumST(start, end, left, mid, leftIdx) + \
                    self.__sumST(start, end, mid+1, right, rightIdx)

    def sum(self, start, end):
        return self.__sumST(start, end, 1, self.size, 0)

    def __updateST(self, start, end, stIdx, idx, op):
        if start == end:
            if op == 1:
                self.STArr[stIdx] += 1
            else:
                self.STArr[stIdx] = max(0, self.STArr[stIdx] - 1)
            return self.STArr[stIdx]
        else:
            mid = (start + end) // 2
            if idx <= mid:
                childValue1 = self.__updateST(start, mid, 2*stIdx+1, idx, op)
                childValue2 = self.STArr[2*stIdx+2]
            else:
                childValue1 = self.__updateST(mid+1, end, 2*stIdx+2, idx, op)
                childValue2 = self.STArr[2*stIdx+1]

            self.STArr[stIdx] = childValue1 + childValue2
        
        return self.STArr[stIdx]

    def update(self, idx, op):
        self.__updateST(1, self.size, 0, idx, op)

class Solution:
    
    def solve(self, A, B):
        ans = []
        obj = SegmentTree()
        obj.createST(A)
        for x, y, z in B:
            if x == 1:
                obj.update(y, 1)
            elif x == 2:
                obj.update(y, 2)
            else:
                value = obj.sum(y, z)
                ans.append(value)

        return ans

A = 5
B = [   
    [1, 1, -1],
    [1, 2, -1],
    [3, 1, 3],
    [2, 1, -1],
    [3, 1, 3]  
    ]

ans = Solution().solve(A, B)
print(ans)