"""
Problem Description
A wire connects N light bulbs.
Each bulb has a switch associated with it; however, due to faulty wiring, a switch also changes the state of all the
bulbs to the right of the current bulb.
Given an initial state of all bulbs, find the minimum number of switches you have to press to turn on all the bulbs.
You can press the same switch multiple times.
Note: 0 represents the bulb is off and 1 represents the bulb is on.

Problem Constraints
1 <= N <= 5×105
0 <= A[i] <= 1

Input Format
The first and the only argument contains an integer array A, of size N.

Output Format
Return an integer representing the minimum number of switches required.

Example Input
Input 1:
 A = [0, 1, 0, 1]
Input 2:
 A = [1, 1, 1, 1]

Example Output
Output 1:
 4
Output 2:
 0

Example Explanation
Explanation 1:
 press switch 0 : [1 0 1 0]
 press switch 1 : [1 1 0 1]
 press switch 2 : [1 1 1 0]
 press switch 3 : [1 1 1 1]
Explanation 2:
 There is no need to turn any switches as all the bulbs are already on.
"""

"""
Solution Approach
The order in which you press the switch does not affect the final state.
Example:
Input : [0 1 0 1]
Case 1:
	Press switch 0 : [1 0 1 0]
	Press switch 1 : [1 1 0 1]
Case 2:
	Press switch 1 : [0 0 1 0]
	Press switch 0 : [1 1 0 1]
	
Therefore we can choose a particular order. To make things easier, let’s go from left to right. At the current position, 
if the bulb is on, we move to the right, else we switch it on. This works because changing any switch to the right of it 
will not affect it anymore.	
"""


class Solution:

    def bulbs(self, A):
        state = 0
        ans = 0
        for i in range(0, len(A)):
            if A[i] == 0:
                if state%2 == 0:
                    state += 1
                    ans += 1
            else:
                if state%2 != 0:
                    state += 1
                    ans += 1

        return ans