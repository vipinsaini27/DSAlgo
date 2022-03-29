"""
Problem Description
Given a sorted array of integers A of size N and an integer B.
array A is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2 ).
You are given a target value B to search. If found in the array, return its index otherwise, return -1.
You may assume no duplicate exists in the array.
NOTE: Users are expected to solve this in O(log(N)) time.


Problem Constraints
1 <= N <= 1000000
1 <= A[i] <= 10^9
all elements in A are distinct.


Input Format
The first argument given is the integer array A.
The second argument given is the integer B.


Output Format
Return index of B in array A, otherwise return -1


Example Input
Input 1:
A = [4, 5, 6, 7, 0, 1, 2, 3]
B = 4

Input 2:
A = [1]
B = 1

Example Output
Output 1:
 0

Output 2:
 0


Example Explanation
Explanation 1:
Target 4 is found at index 0 in A.

Explanation 2:
Target 1 is found at index 0 in A.
"""

"""
Solution Approach
A naive solution is a linear search.

To improve, let us break our approach into two steps. First, we find the pivot (the index of minimum in the array).

Once we know the pivot, to search for x, we can do a conventional binary search in the left and right parts of the pivot 
in the array.

Now, let us look at how binary search can be applied in this scenario to find the minimum.

There are 2 cases:

1)
          mid 
           |
   6 7 8 9 1 2 3 4 5  
arr[mid] > arr[end]

The min lies in (mid, end]

Mid is excluded from the range because arr[mid] > arr[end]

2)
         mid       
          | 
  6 7 8 9 1 2 3 4 5
arr[mid] < arr[end]

The min lies in [start, mid]

3) Note: If there are duplicates, making either decision might be difficult, and hence linear search might be required.
               mid  
                |
1 1 1 1 2 0 1 1 1 1 1 1 1 1 1 1 1 
arr[mid] = arr[end]

Indecisive. We would need to explore the whole array.
"""

class Solution:

    def search(self, A, B):
        l = len(A)
        L, H = 0, l - 1
        while L < H:
            S = (L + H) // 2
            if A[L] < A[H]:
                S = L
                break
            if S in [0, l-1]:
                break
            if A[S-1] > A[S+1]:
                if A[S] > A[S+1]:
                    S = S+1
                break
            if A[S] > A[H]:
                L = S
            else:
                H = S

        L, H = 0, S-1
        while L < H:
            M = (L + H) // 2
            if A[M] == B:
                return M
            elif A[M] > B:
                H = M
            else:
                L = M+1

        if A[L] == B:
            return L

        L, H = S, l-1
        while L < H:
            M = (L + H) // 2
            if A[M] == B:
                return M
            elif A[M] > B:
                H = M
            else:
                L = M+1

        if A[L] == B:
            return L

        return -1