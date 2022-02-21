"""
Problem Description
Given a string A, partition A such that every string of the partition is a palindrome.
Return all possible palindrome partitioning of A.
Ordering the results in the answer : Entry i will come before Entry j if :
len(Entryi[0]) < len(Entryj[0]) OR
(len(Entryi[0]) == len(Entryj[0]) AND len(Entryi[1]) < len(Entryj[1])) OR * * *
(len(Entryi[0]) == len(Entryj[0]) AND ... len(Entryi[k] < len(Entryj[k]))


Problem Constraints
1 <= len(A) <= 15


Input Format
First argument is a string A of lowercase characters.


Output Format
Return a list of all possible palindrome partitioning of s.


Example Input
Input 1:
A = "aab"

Input 2:
A = "a"


Example Output
Output 1:
 [
    ["a","a","b"]
    ["aa","b"],
  ]

Output 2:
 [
    ["a"]
  ]


Example Explanation
Explanation 1:
In the given example, ["a", "a", "b"] comes before ["aa", "b"] because len("a") < len("aa").

Explanation 2:
In the given example, only partition possible is "a" .
"""

"""
Solution Approach
We can use recursion to generate all possible palindrome partitioning of s.

When on index i, you incrementally check all substring starting from i for being palindromic. If found, you recursively 
solve the problem for the remaining string and add it to your solution. Start this recursion from starting position of 
the string.

PS: You can optimize your solution by not computing the answer for same index multiple times using Dynamic Programming.
"""

import copy

class Solution:

    def isPalindrom(self, s):
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1

        return True

    def palindrome(self, s, li, ans):
        if len(s) > 0:
            for i in range(0, len(s)):
                if self.isPalindrom(s[0:i+1]):
                    li.append(s[0:i+1])
                    ans = self.palindrome(s[i+1:], li, ans)
                    li.pop()
        else:
            ans.append(copy.copy(li))

        return ans

    def partition(self, A):
        ans = self.palindrome(A, [], [])
        return ans
