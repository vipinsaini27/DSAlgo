"""
Problem Description

Given an integer A denoting the size of the array consisting all ones.

You are given Q queries, for each query there are two integer x and y:

If x is 0, then update the value of array at index y to 0.
If x is 1, then output the index of yth one in the array. If there is no such index then output -1.
NOTE 1: There will atleast 1 query where value of x is 1.



Problem Constraints

1 <= A, Q <= 105

0 <= x <= 1

1 <= y <= A



Input Format

First argument is an integer A denoting the size of array.

Second argument is a 2-D array B of size Q x 2 where B[i][0] denotes x and B[i][1] denotes y.



Output Format

Return an integer array denoting the output of each query where x is 1.



Example Input

Input 1:

 A = 4
 B = [ [1, 2],
       [0, 2],
       [1, 4] ]
Input 2:

 A = 5
 B = [ [0, 3],
       [1, 4],
       [0, 3],
       [1, 5] ] 


Example Output

Output 1:

 [2, -1]
Output 2:

 [5, -1]


Example Explanation

Explanation 1:

 Initially array = [1, 1, 1, 1]. For first query 2nd one is at index 2.
 After Second query array becomes [1, 0, 1, 1].
 For third query there is no 4th one.
Explanation 2:

 Initially array = [1, 1, 1, 1, 1]. After first query array becomes [1, 1, 0, 1, 1].
 For second query 4th one is at index 5.    
 After third query array remains same [1, 1, 0, 1, 1].
 For fourth query there is no 5th one.
"""

"""
Solution Approach
We can use both Binary Indexed Tree(fenwick tree) or Segment Tree.

Since initially all value of the array A is 1.

Build segment tree on the array A. Node of segment tree will store the sum of elements of the segment represented by the node.

For query, when x == 0, update the value at index x to 0 if it is 1.

For x == 1, we will first do a binary search to find the index let’s say mid and call the query function of segment tree to find the sum of array from 1 to index(mid).

If sum == y, then index (mid) could be the answer. But there may be other value of index less than mid that satisfy the condition. So we update hi = mid-1.
If sum > y, search in the lower range. So update hi = mid - 1.
If sum < y, search in the higher range. So update lo = mid + 1.

If there is no index, output -1.
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
            self.STArr[idx] = 1
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

    def __iIndexST(self, target, left, right, idx):
        mid = (right + left) // 2
        leftIdx = 2*idx + 1
        rightIdx = 2*idx + 2

        if left == right:
            return right

        if self.STArr[idx] < target:
            return -1
        
        if self.STArr[leftIdx] < target:
            return self.__iIndexST(target-self.STArr[leftIdx], mid+1, right, rightIdx)
        
        if self.STArr[leftIdx] >= target:
            return self.__iIndexST(target, left, mid, leftIdx)
        

    def getIIndex(self, ithOne):
        return self.__iIndexST(ithOne, 1, self.size, 0)

    def __updateST(self, start, end, stIdx, idx):
        if start == end:
            self.STArr[stIdx] = 0
            return 0
        else:
            mid = (start + end) // 2
            if idx <= mid:
                childValue1 = self.__updateST(start, mid, 2*stIdx+1, idx)
                childValue2 = self.STArr[2*stIdx+2]
            else:
                childValue1 = self.__updateST(mid+1, end, 2*stIdx+2, idx)
                childValue2 = self.STArr[2*stIdx+1]

            self.STArr[stIdx] = childValue1 + childValue2
        
        return self.STArr[stIdx]

    def update(self, idx):
        self.__updateST(1, self.size, 0, idx)
        print(self.STArr)

class Solution:
    
    def solve(self, A, B):
        obj = SegmentTree()
        obj.createST(A)
        ans = []

        for x, y in B:
            if x == 0:
                obj.update(y)
            else:
                ans.append(obj.getIIndex(y))

        return ans