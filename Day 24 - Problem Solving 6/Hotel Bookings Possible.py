"""
Problem Description
A hotel manager has to process N advance bookings of rooms for the next season. His hotel has K rooms.
Bookings contain an arrival date and a departure date.
He wants to find out whether there are enough rooms in the hotel to satisfy the demand.
Write a program that solves this problem in time O(N log N) .

Problem Constraints
1 <= N <= 106
1 <= K <= 106
0 <= arrive[i] <= depart[i] <= 108

Input Format
First argument is an integer array named arrive denoting the arrival times of bookings.
Second argument is an integer array named depart denoting the departure times of bookings.
Third argument is an integer K which denotes count of rooms.

Output Format
A boolean which tells whether its possible to make a booking.
Return 0/1 for C programs.
O -> No there are not enough rooms for N booking.
1 -> Yes there are enough rooms for N booking.

Example Input
Input 1:
 arrive = [1, 3, 5]
 depart = [2, 6, 8]
 K = 1

Example Output
Output 1:
 False / 0

Example Explanation
Explanation 1:
 At day = 5, there are 2 guests in the hotel. But hotel has only one room so it is not possible to take the booking
 so we will return false or 0 for C Program.
"""

"""
Solution Approach
1. Create event points for every interval start, and end. 
2. Sort it according to the day. 
3. Now, iterate over them one by one. If you encounter a start, then the number of active guests increase by one. If you 
encounter an end, the number of active guests decrease by one. 
4. If at any point, the number of active guests exceed K, we know that scheduling is not possible.
GOTCHAS : What if there are multiple start and end on the same day ? How should they be ordered ?
"""


class Solution:

    def hotel(self, arrive, depart, K):
        arrive = sorted(arrive)
        depart = sorted(depart)

        count = 0
        i, j = 0, 0
        while i < len(arrive) and j < len(depart):
            if arrive[i] <= depart[j]:
                count += 1
                i += 1
            elif arrive[i] > depart[j]:
                count -= 1
                j += 1
            else:
                i += 1
                j += 1

            if count > K:
                return False

        return True
