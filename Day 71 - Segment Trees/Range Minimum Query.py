"""
Problem Description

Given an integer array A of size N.

You have to perform two types of query, in each query you are given three integers x,y,z.

If x = 0, then update A[y] = z.
If x = 1, then output the minimum element in the array A between index y and z inclusive.
Queries are denoted by a 2-D array B of size M x 3 where B[i][0] denotes x, B[i][1] denotes y, B[i][2] denotes z.



Problem Constraints

1 <= N, M <= 105

1 <= A[i] <= 109

If x = 0, 1<= y <= N and 1 <= z <= 109

If x = 1, 1<= y <= z <= N



Input Format

First argument is an integer array A of size N.

Second argument is a 2-D array B of size M x 3 denoting queries.



Output Format

Return an integer array denoting the output of each query where value of x is 1.



Example Input

Input 1:

 A = [1, 4, 1]
 B = [ 
        [1, 1, 3]
        [0, 1, 5]
        [1, 1, 2] 
     ]
Input 2:

 A = [5, 4, 5, 7]
 B = [ 
        [1, 2, 4]
        [0, 1, 2]
        [1, 1, 4]
     ]


Example Output

Output 1:

 [1, 4]
Output 2:

 [4, 2]


Example Explanation

Explanation 1:

 For 1st query, the minimum element from range (1, 3) is 1.
 For 2nd query, update A[1] = 5, now A = [5, 4, 1].
 For 3rd query, the minimum element from range (1, 2) is 4.
Explanation 2:

 For 1st query, the minimum element from range (2, 4) is 4.
 For 2nd query, update A[1] = 2, now A = [2, 4, 5, 7].
 For 3rd query, the minimum element from range (1, 4) is 2.
"""

"""
Solution Approach
We will create Segment Tree to do preprocessing and and work in query in moderate time.
With segment tree, preprocessing time is O(N) and time to for range minimum query is O(LogN). Also, for update =operation it will O(logN)
The extra space required is O(N) to store the segment tree.

Construction of Segment Tree from given array

We start with a segment A[0 . . . n-1]. and every time we divide the current segment into two halves(if it has not yet become a segment of length 1), and then call the same procedure on both halves, and for each such segment, we store the minimum value in a segment tree node.

Once the tree is constructed we will likewise call the update and query function corresponding to the query.
We will use the same approach of dividing the segment into two halves and do the necessary operation.
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

    def __constructST(self, arr, idx, start, end):
        if start == end:
            self.STArr[idx] = arr[end]
        else:
            mid = (start + end) // 2
            left = 2*idx + 1
            right = 2*idx + 2
            self.__constructST(arr, left, start, mid)
            self.__constructST(arr, right, mid+1, end)
            self.STArr[idx] = min(self.STArr[left], self.STArr[right])

    def createST(self, arr):
        n = len(arr)
        self.__setST(n)
        self.__constructST(arr, 0, 0, n-1)

    def __minST(self, start, end, left, right, idx):
        if start <= left and end >= right:
            return self.STArr[idx]
        if end < left or right < start:
            return 10**9 + 1
        
        mid = (left + right) // 2
        leftIdx = 2*idx + 1
        rightIdx = 2*idx + 2
        return min(self.__minST(start, end, left, mid, leftIdx),
                    self.__minST(start, end, mid+1, right, rightIdx))

    def min(self, start, end):
        return self.__minST(start, end, 1, self.size, 0)

    def __updateST(self, start, end, stIdx, idx, value):
        if start == end:
            self.STArr[stIdx] = value
            return value
        else:
            mid = (start + end) // 2
            if idx <= mid:
                childValue1 = self.__updateST(start, mid, 2*stIdx+1, idx, value)
                childValue2 = self.STArr[2*stIdx+2]
            else:
                childValue1 = self.__updateST(mid+1, end, 2*stIdx+2, idx, value)
                childValue2 = self.STArr[2*stIdx+1]

            self.STArr[stIdx] = min(childValue1, childValue2)
        
        return self.STArr[stIdx]

    def update(self, idx, value):
        self.__updateST(1, self.size, 0, idx, value)

class Solution:
    
    def solve(self, A, B):
        stObj = SegmentTree()
        stObj.createST(A)

        ans = []
        for x, y, z in B:
            if x == 0:
                stObj.update(y, z)
            else:
                value = stObj.min(y, z)
                ans.append(value)

        return ans