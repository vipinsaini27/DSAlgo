"""
Problem Description
You are given an array of distinct integers A, you have to find and return all elements in array which have at-least two greater elements than themselves.

NOTE: The result should have the order in which they are present in the original array.


Problem Constraints
3 <= |A| <= 105
-109 <= A[i] <= 109


Input Format
First and only argument is an integer array A.


Output Format
Return an integer array containing the elements of A which have at-least two greater elements than themselves in A.


Example Input
Input 1:
 A = [1, 2, 3, 4, 5]

Input 2:
 A = [11, 17, 100, 5]


Example Output
Output 1:
 [1, 2, 3]

Output 2:
 [11, 5]


Example Explanation
Explanation 1:
 Number of elements greater than 1: 4
 Number of elements greater than 2: 3
 Number of elements greater than 3: 2
 Number of elements greater than 4: 1
 Number of elements greater than 5: 0
 Elements 1, 2 and 3 have atleast 2 elements strictly greater than themselves.

Explanation 2:
 Number of elements greater than 11: 2
 Number of elements greater than 17: 1
 Number of elements greater than 100: 0
 Number of elements greater than 5: 3
 Elements 5 and 11 have atleast 2 elements strictly greater than themselves.
"""

"""
Solution Approach
As the array contains distinct elements, All the elements other than the largest element and the second largest element have atleast 2 greater elements than themselves in the array.

We can find the largest/greatest element('firstGreatest') by iterating through the array once.

Once largest element is found, we can find the second largest('secondGreatest') element by just finding the largest element in the array excluding 'firstGreatest'.

Now we can build the answer by just including the array elements other than 'firstLargest' and 'SecondLargest'.
"""

class Solution:
    
    def solve(self, A):
        result = []
        for i in A:
            count = 0
            for j in A:
                if j > i:
                    count += 1
                if count == 2:
                    result.append(i)
                    break

        return result