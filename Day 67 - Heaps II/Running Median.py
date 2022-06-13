"""
Problem Description
Given an array of integers, A denoting a stream of integers. New arrays of integer B and C are formed.
Each time an integer is encountered in a stream, append it at the end of B and append the median of array B at the C.

Find and return the array C.

NOTE:

If the number of elements is N in B and N is odd, then consider the median as B[N/2] ( B must be in sorted order).
If the number of elements is N in B and N is even, then consider the median as B[N/2-1]. ( B must be in sorted order).


Problem Constraints
1 <= length of the array <= 100000
1 <= A[i] <= 109



Input Format
The only argument given is the integer array A.



Output Format
Return an integer array C, C[i] denotes the median of the first i elements.



Example Input
Input 1:

 A = [1, 2, 5, 4, 3]
Input 2:

 A = [5, 17, 100, 11]


Example Output
Output 1:

 [1, 1, 2, 2, 3]
Output 2:

 [5, 5, 17, 11]


Example Explanation
Explanation 1:

 stream          median
 [1]             1
 [1, 2]          1
 [1, 2, 5]       2
 [1, 2, 5, 4]    2
 [1, 2, 5, 4, 3] 3
Explanation 2:

 stream          median
 [5]              5
 [5, 17]          5
 [5, 17, 100]     17
 [5, 17, 100, 11] 11 
"""

"""
Solution Approach
As it is mentioned in the hint, the median is an element of the array such that half elements are smaller and half elements are greater than that element.

So, the idea is to use max heap and min heap to store the elements of the higher half and lower half.

Max heap and min heap can be implemented using STL.

Algorithm

Create two heaps. One max heap to maintain elements of the lower half and one min heap to maintain elements of the higher half at any point in time.
Take the initial value of the median as 0.
For every newly read element, insert it into either max heap or min-heap and calculate the median based on the following conditions:

1 If the size of the max-heap is greater than the size of the min-heap and the element is less than the previous median, then pop the top element from the max-heap and insert it into the min-heap and insert the new element into the max-heap else insert the new element to min-heap. Calculate the new median as the average of the top of elements of both max and min-heap.

2 If the size of the max-heap is less than the size of the min-heap and the element is greater than the previous median, then pop the top element from the min-heap and insert it into the max heap and insert the new element to the min-heap else insert the new element to max-heap. Calculate the new median as the average of the top of elements of both max and min-heap.

3 If the size of both heaps are the same. Then check if the current is less than the previous median or not. If the current element is less than the previous median, then insert it into the max-heap, and the new median will be equal to the top element of the max-heap. If the current element is greater than the previous median, then insert it into the min-heap, and the new median will be equal to the top element of the min-heap.

Time Complexity:- O(NlogN)
Space Complexity:- O(N)
"""

from heapq import heappush, heappop

class Solution:
    
    def solve(self, A):
        if len(A) in [1, 2]:
            return A[0]

        ans = [A[0]]
        maxHeap = []
        minHeap = []
        heappush(maxHeap, A[0])
        for i in range(1, len(A)):
            val = A[i]
            if val < abs(maxHeap[0]):
                heappush(maxHeap, -1*val)
                if len(maxHeap) - len(minHeap) > 1:
                    rootVal = abs(heappop(maxHeap))
                    heappush(minHeap, rootVal)
            else:
                heappush(minHeap, val)
                if len(minHeap) - len(maxHeap) > 0:
                    rootVal = heappop(minHeap)
                    heappush(maxHeap, -1*rootVal)

            ans.append(abs(maxHeap[0]))

        return ans