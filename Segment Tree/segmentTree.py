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
