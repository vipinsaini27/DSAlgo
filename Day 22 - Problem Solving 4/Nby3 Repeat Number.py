"""
Problem Description
You're given a read-only array of N integers. Find out if any integer occurs more than N/3 times in the array in linear
time and constant additional space.
If so, return the integer. If not, return -1.
If there are multiple solutions, return any one.

Problem Constraints
1 <= N <= 7*105
1 <= A[i] <= 109

Input Format
The only argument is an integer array A.

Output Format
Return an integer.

Example Input
[1 2 3 1 1]

Example Output
1

Example Explanation
1 occurs 3 times which is more than 5/3 times.
"""

"""
Solution Approach
It is important to note that if at a given time, you have 3 distinct element from the array, if you remove them from the 
array, your answer does not change.
Assume that we maintain 2 elements’ counts as we traverse along the array.
When we encounter a new element, there are 3 cases possible :
We don’t have 2 elements yet. So add this to the list with count as 1.
This element is different from the existing 2 elements. As we said before, we have 3 distinct numbers now. Removing them 
does not change the answer. So decrement 1 from count of 2 existing elements. If their count falls to 0, obviously its 
not a part of 2 elements anymore.
The new element is same as one of the 2 elements. Increment the count of that element.
Consequently, the answer will be one of the 2 elements left behind. If they are not the answer, there is no element with 
count > N / 3.
"""

class Solution:

    def repeatedNumber(self, A):
        first = None
        second = None
        count1 = 0
        count2 = 0

        for i in range(0, len(A)):
            if A[i] == first:
                count1 += 1
            elif A[i] == second:
                count2 += 1
            elif count1 == 0:
                first = A[i]
                count1 += 1
            elif count2 == 0:
                second = A[i]
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1

        count1 = 0
        count2 = 0
        for i in range(0, len(A)):
            if first == A[i]:
                count1 += 1
            elif second == A[i]:
                count2 += 1

        if count1 > len(A) / 3:
            return first
        elif count2 > len(A) / 3:
            return second

        return -1