"""
Problem Description
Given an array of size N, find the majority element. The majority element is the element that appears more than
floor(n/2) times.
You may assume that the array is non-empty and the majority element always exists in the array.

Problem Constraints
1 <= N <= 5*105
1 <= num[i] <= 109

Input Format
Only argument is an integer array.

Output Format
Return an integer.

Example Input
[2, 1, 2]

Example Output
2

Example Explanation
2 occurs 2 times which is greater than 3/2.
"""

"""
Solution Approach
If we cancel out each occurrence of an element X with all the other elements that are different from X, then X will 
exist till the end if it is a majority element. 
Loop through each element and maintain a count of the element that has the potential of being the majority element. 
If the next element is the same, then increments the count, otherwise decrements the count. 
If the count reaches 0, then update the potential index to the current element and reset the count to 1.
"""

class Solution:

    def majorityElement(self, A):
        mec = 0
        me = None

        for i in A:
            if me is None:
                me = i
                mec += 1
            elif me != i:
                mec -= 1
                if mec == 0:
                    me = None
            else:
                mec += 1

        return me