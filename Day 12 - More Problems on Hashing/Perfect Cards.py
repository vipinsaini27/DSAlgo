"""
Problem Description

Tom and Harry are given N numbers, with which they play a game as a team.

Initially, Tom chooses a particular number P from the N numbers, and he takes away all the numbers that are equal to P.

Next, Harry chooses a different number Q, different from what Tom chose, and takes away all the numbers equal to Q from
the remaining N numbers.

They win the game if they can take all the numbers by doing the above operation once and if each of them has the same
amount of numbers towards the end.

If they win, return the string "WIN", else return "LOSE".



Problem Constraints

2 <= N <= 100

1 <= A[i] <= 100



Input Format

The first and the only argument of input contains an integer array, A.



Output Format

Return a string, denoting the answer.



Example Input

Input 1:

 A = [1, 2]
Input 2:

 A = [1, 1, 2, 2, 3]


Example Output

Output 1:

 "WIN"
Output 2:

 "LOSE"


Example Explanation

Explanation 1:

 In the his turn, Tom can take 1 away, and then Harry take take 2 away. The array is empty and both of them have equal
 number of cards, so we can say that they have won the game.
Explanation 2:

 No matter how they take away the elements, >= 1 card will always remain, hence, they lose.
"""

"""
Solution Approach
We have to check for two things:

Check that A contains only 2 unique numbers
If A contains 2 unique numbers, the count of both the numbers is the same
If our array A satisfies the above two points, Tom and Harry win, otherwise they lose.

We can hash each number of array A in a map, and then check the size of the map.
If the size is not 2, they lose, otherwise we check the count of the 2 numbers in the map, and if they are equal, 
they win else they lose.
"""

class Solution:
    # @param A : list of integers
    # @return a strings
    def solve(self, A):
        hash = {}

        for val in A:
            if val not in hash.keys():
                hash[val] = 0

            hash[val] += 1

        freq = []
        for _, val in hash.items():
            freq.append(val)

        freq.sort()

        a = 0
        b = 0
        for i in range(0, len(freq), 2):
            a += freq[i]

        for i in range(1, len(freq), 2):
            b += freq[i]

        if a == b:
            return "WIN"

        return "LOSE"