"""
Problem Description
Find the number of occurrences of bob in string A consisting of lowercase English alphabets.

Problem Constraints
1 <= |A| <= 1000

Input Format
The first and only argument contains the string A, consisting of lowercase English alphabets.

Output Format
Return an integer containing the answer.

Example Input
Input 1:
  "abobc"
Input 2:
  "bobob"

Example Output
Output 1:
  1
Output 2:
  2

Example Explanation
Explanation 1:
  The only occurrence is at second position.
Explanation 2:
  Bob occures at first and third position.
"""

"""
Solution Approach
Let's use str.find() to find the first occurrence.
Then, can use str.find() multiple times by changing start index each time.
"""

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        ans = 0
        for i in range(0, len(A) - 2):
            if A[i] == 'b' and A[i + 1] == 'o' and A[i + 2] == 'b':
                ans += 1

        return ans