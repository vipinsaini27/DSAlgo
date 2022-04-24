"""
Problem Description
Given an array A of N integers, find three integers in A such that the sum is closest to a given number B. Return the
sum of those three integers.
Assume that there will only be one solution.

Problem Constraints
-108 <= B <= 108
1 <= N <= 104
-108 <= A[i] <= 108

Input Format
First argument is an integer array A of size N.
Second argument is an integer B denoting the sum you need to get close to.

Output Format
Return a single integer denoting the sum of three integers which is closest to B.

Example Input
Input 1:
A = [-1, 2, 1, -4]
B = 1
Input 2:
A = [1, 2, 3]
B = 6

Example Output
Output 1:
2
Output 2:
6

Example Explanation
Explanation 1:
 The sum that is closest to the target is 2. (-1 + 2 + 1 = 2)
Explanation 2:
 Take all elements to get exactly 6.
"""

"""
Solution Approach
As stated in the earlier hint, the naive approach is to have 3 loops of i,j,k over the array. We then just track 
S[i]+S[j]+S[k] for the case when (S[i]+S[j]+S[k]-target) is minimum.
The code for the same looks something like the following :

IF number of elements in S < 3
    THEN return -1; // Invalid case
  minDifference = abs(S[0] + S[1] + S[2] - target);
  bestTillNow = S[0] + S[1] + S[2];
  FOR i = 0 to size of S
    FOR j = i + 1 to size of S
      FOR k = j + 1 to size of S
        newDiff = abs(S[i] + S[j] + S[k] - target)
        IF newDiff < minDifference
          minDifference = newDiff
          bestTillNow = S[i] + S[j] + S[k]
        END IF
      END FOR
    END FOR
  END FOR

  bestTillNow is my answer. 
  
However, as stated earlier this approach is O(N^3). Lets see if we can do better.

Lets sort the array.
When the array is sorted, try to fix the least integer by looping over it.
Lets say the least integer in the solution is arr[i].

Now we need to find a pair of integers j and k, such that arr[j] + arr[k] is closest to (target - arr[i]).
To do that, let us try the 2 pointer approach.
If we fix the two pointers at the end ( that is, i+1 and end of array ), we look at the sum.

If the sum is smaller than the sum we need to get to, we increase the first pointer.
If the sum is bigger, we decrease the end pointer to reduce the sum.
"""

class Solution:

    def threeSumClosest(self, A, B):
        A = sorted(A)
        ans = sum(A[0:3])
        minDiff = abs(B - ans)
        i = 3
        while i < len(A):
            j, k = 0, i - 1
            while j < k:
                s = A[i] + A[j] + A[k]
                diff = abs(B - s)
                if diff < minDiff:
                    minDiff = diff
                    ans = s

                if s == B:
                    break
                elif s > B:
                    k -= 1
                else:
                    j += 1
            i += 1

        return ans