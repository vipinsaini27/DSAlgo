"""
Problem Description
You are given a n x n 2D matrix A representing an image.
Rotate the image by 90 degrees (clockwise).
You need to do this in place.
Note: If you end up using an additional array, you will only receive partial score.


Problem Constraints
1 <= n <= 1000


Input Format
First argument is a 2D matrix A of integers


Output Format
Return the 2D rotated matrix.


Example Input
Input 1:
 [
    [1, 2],
    [3, 4]
 ]

Input 2:
 [
    [1]
 ]


Example Output
Output 1:
 [
    [3, 1],
    [4, 2]
 ]

Output 2:
 [
    [1]
 ]


Example Explanation
Explanation 1:
 After rotating the matrix by 90 degree:
 1 goes to 2, 2 goes to 4
 4 goes to 3, 3 goes to 1

Explanation 2:
 2D array remains the ssame as there is only element.
"""

"""
Solution Approach
Doing things in place can be slightly trickier.

Note that if you create a graph with each cell as vertex with an edge from source cell to the destination cell, the graph 
ends up with cycles of length 4.

Which means something like this should work:

Divide the array into 4 along the diagonals
Place each element in the top quadrant into the slot 90 degrees clockwise
Place the old 90 in 180 degrees clockwise
Place the old 180 in 270 degrees
Lastly, place the old 270 in the original place
It might be easier to understand the solution if a few examples are tried out by hand.
Let me elaborate on a 3x3 example. You can try more examples of other size.
Lets say the array is

[ 
1 2 3
4 5 6
7 8 9 
]
After rotation by 90 degree, it should be

[
7 4 1
8 5 2
9 6 3
]
Lets say you were allowed extra space and not required to do things in place.

Easier approach :
If you notice, if you read out the column ‘i’ in reverse order, it corresponds to the new row ‘i’ in resulting array. 
So, column 0 in original array read out in reverse order is 7 4 1 which is row 0 in answer. And so on. So you just 
simulate this approach and keep creating the result in another 2 D array.

However, this approach requires additional space of O(n^2) where n = number of rows in 2D array.

Now lets say we have to do things in place ( no extra space allowed ). This implies that we have to make things work with 
just moving elements around with constant extra memory.
So, lets try to observe where elements need to end up in the result array.

* 7 needs to end up in 1's position. 
* If 7 goes to 1's position, then we need to check where 1 needs to go otherwise value 1 will be lost. 1 needs to go to 
3's position. 
* 3 needs to go to 9's position. 
* 9 needs to go to 7's position. 
* We already have placed 7 in 1's position. 
So when we move these 4 elements, all 4 elements are in their correct position.

Lets look at 4 now.

4 -> 2 -> 6 -> 8. 
Again, a group of 4. So, we can move these elements group by group without requiring creating a copy of the array.

You can try a few more examples to convince yourself.

The code just tries to simulate whats being discussed here.
"""

import copy

class Solution:
    # @param A : list of list of integers
    def solve(self, A):
        n = len(A)

        a = [0, 0]
        b = [0, n-1]
        c = [n-1, n-1]
        d = [n-1, 0]

        while a[0] < c[0]:
            a1, b1, c1, d1 = copy.copy(a), copy.copy(b), copy.copy(c), copy.copy(d)
            while a1[1] < b[1]:
                A[a1[0]][a1[1]], A[d1[0]][d1[1]] = A[d1[0]][d1[1]], A[a1[0]][a1[1]]
                A[d1[0]][d1[1]], A[c1[0]][c1[1]] = A[c1[0]][c1[1]], A[d1[0]][d1[1]]
                A[c1[0]][c1[1]], A[b1[0]][b1[1]] = A[b1[0]][b1[1]], A[c1[0]][c1[1]]

                a1[1] += 1
                b1[0] += 1
                c1[1] -= 1
                d1[0] -= 1

            a[0] += 1
            a[1] += 1
            b[0] += 1
            b[1] -= 1
            c[0] -= 1
            c[1] -= 1
            d[0] -= 1
            d[1] += 1

        return A