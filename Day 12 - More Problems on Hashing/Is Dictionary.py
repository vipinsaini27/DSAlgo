"""
Problem Description
Surprisingly, in an alien language, they also use English lowercase letters, but possibly in a different order. The
order of the alphabet is some permutation of lowercase letters.

Given an array of words A of size N written in the alien language, and the order of the alphabet denoted by string B of
size 26, return 1 if and only if the given words are sorted lexicographically in this alien language else, return 0.



Problem Constraints
1 <= N, length of each word <= 105

Sum of the length of all words <= 2 * 106



Input Format
The first argument is a string array A of size N.

The second argument is a string B of size 26, denoting the order.



Output Format
Return 1 if and only if the given words are sorted lexicographically in this alien language else, return 0.



Example Input
Input 1:

 A = ["hello", "scaler", "interviewbit"]
 B = "adhbcfegskjlponmirqtxwuvzy"
Input 2:

 A = ["fine", "none", "no"]
 B = "qwertyuiopasdfghjklzxcvbnm"


Example Output
Output 1:

 1
Output 2:

 0


Example Explanation
Explanation 1:

 The order shown in string B is: h < s < i for the given words. So return 1.
Explanation 2:

 "none" should be present after "no". Return 0.
"""

"""
Solution Approach
Let’s check whether all adjacent words a and b have a <= b.

To check whether a <= b for two adjacent words, a and b, we can find their first difference.
For example, “applying” and “apples” have the first difference of y and e.
After, we compare these characters to the index in order.

Care must be taken to deal with the blank character effectively.
If, for example, we are comparing “app” to “apply”, the first difference is between (null) and “l”.
"""

class Solution:
    # @param A : list of strings
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        if len(A) == 1:
            return 1

        hash = {}
        for i, ch in enumerate(B):
            hash[ch] = i

        i = 1
        while i < len(A):
            w1 = A[i-1]
            w2 = A[i]
            x = 0
            y = 0
            while x < len(w1) and y < len(w2):
                if hash[w1[x]] < hash[w2[y]]:
                    break
                elif hash[w1[x]] > hash[w2[y]]:
                    return 0
                x += 1
                y += 1

            if len(w1) > len(w2):
                return 0

            i += 1

        return 1