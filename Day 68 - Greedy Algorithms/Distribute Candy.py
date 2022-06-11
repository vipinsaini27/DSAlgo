"""
Problem Description
N children are standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum number of candies you must give?



Problem Constraints
1 <= N <= 105
-109 <= A[i] <= 109



Input Format
The first and only argument is an integer array A representing the rating of children.



Output Format
Return an integer representing the minimum candies to be given.



Example Input
Input 1:

 A = [1, 2]
Input 2:

 A = [1, 5, 2, 1]


Example Output
Output 1:

 3
Output 2:

 7


Example Explanation
Explanation 1:

 The candidate with 1 rating gets 1 candy and candidate with rating 2 cannot get 1 candy as 1 is its neighbor. 
 So rating 2 candidate gets 2 candies. In total, 2 + 1 = 3 candies need to be given out.
Explanation 2:

 Candies given = [1, 3, 2, 1]
"""

"""
Solution Approach
Greedy will work here ( Think of a supportive proof as an assignment ).

Start with the guy with the least rating. Obviously, he will receive one candy.

If he did receive more than one candy, we could lower it to 1 as none of the neighbors have a higher rating.
Now, let us move to the one which is the second least. If the least element is its neighbor, then it receives two candies, else we can get away with assigning it just one candy.

We keep repeating the same process to arrive at the optimal solution.
"""

class Solution:
    
    def candy(self, A):
        c = [1]*len(A)
        sIdx = sorted(range(len(A)), key = lambda x: A[x])
        for idx in sIdx:
            val = A[idx]
            lN = idx - 1
            rN = idx + 1
            
            if lN >= 0 and rN < len(A):
                if A[lN] < val and val > A[rN]:
                    c[idx] = max(c[lN], c[rN]) + 1
                elif A[lN] < val:
                    c[idx] = c[lN] + 1
                elif A[rN] < val:
                    c[idx] = c[rN] + 1
            elif lN >= 0:
                if A[lN] < val:
                    c[idx] = c[lN] + 1
            elif rN < len(A):
                if A[rN] < val:
                    c[idx] = c[rN] + 1

        return sum(c)