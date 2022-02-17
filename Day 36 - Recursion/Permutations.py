"""
Problem Description
Given an integer array A of size N denoting collection of numbers , return all possible permutations.
NOTE:
No two entries in the permutation sequence should be the same.
For the purpose of this problem, assume that all the numbers in the collection are unique.
Return the answer in any order

Problem Constraints
1 <= N <= 9


Input Format
Only argument is an integer array A of size N.


Output Format
Return a 2-D array denoting all possible permutation of the array.


Example Input
A = [1, 2, 3]


Example Output
[ [1, 2, 3]
  [1, 3, 2]
  [2, 1, 3]
  [2, 3, 1]
  [3, 1, 2]
  [3, 2, 1] ]


Example Explanation
All the possible permutation of array [1, 2, 3].
"""

"""
Solution Approach
Heap’s algorithm is used to generate all permutations of n objects. The idea is to generate each permutation from the previous permutation by choosing a pair of elements to interchange, without disturbing the other n-2 elements.

Algorithm:

1)The algorithm generates (n-1)! permutations of the first n-1 elements, adjoining the last element to each of these. This will generate all of the permutations that end with the last element.

2)If n is odd, swap the first and last element and if n is even, then swap the ith element (i is the counter starting from 0) and the last element and repeat the above algorithm till i is less than n.

3)In each iteration, the algorithm will produce all the permutations that end with the current last element.
"""

import copy

class Solution:

    def fun(self, A, ans, start):
        ans.append(A)
        i = len(A) - 1
        while i > start:
            j = i + 1
            while j < len(A):
                A1 = copy.copy(A)
                if A1[i] < A1[j]:
                    k = j - 1
                    tmp = A1[j]
                    while k >= i:
                        A1[k + 1] = A1[k]
                        k -= 1
                    A1[i] = tmp
                    ans = self.fun(A1, ans, i)
                j += 1
            i -= 1

        return ans

    def permute(self, A):
        A = sorted(A)
        ans = self.fun(A, [], -1)

        return ans


A = [1]
ans = Solution().permute(A)
for a in ans:
    print(a)

