"""
Problem Description
Given an array of words A (dictionary) and another array B (which contain some words).

You have to return the binary array (of length |B|) as the answer where 1 denotes that the word is present in the dictionary and 0 denotes it is not present.

Formally, for each word in B, you need to return 1 if it is present in Dictionary and 0 if not.

Such problems can be seen in real life when we work on any online editor (like Google Documnet), if the word is not valid it is underlined by a red line.

NOTE: Try to do this in O(n) time complexity.



Problem Constraints
1 <= |A| <= 1000

1 <= sum of all strings in A <= 50000

1 <= |B| <= 1000



Input Format
First argument is array of strings A.

First argument is array of strings B.



Output Format
Return the binary array of integers according to the given format.



Example Input
Input 1:

A = [ "hat", "cat", "rat" ]
B = [ "cat", "ball" ]
Input 2:

A = [ "tape", "bcci" ]
B = [ "table", "cci" ]


Example Output
Output 1:

[1, 0]
Output 2:

[0, 0]


Example Explanation
Explanation 1:

Only "cat" is present in the dictionary.
Explanation 2:

None of the words are present in the dictionary.
"""

"""
Solution Approach
To this in O(n), you will need a different data structure called tries.
You can insert all dictionary strings in a trie and then try finding all
given strings in the trie; each of those will take O(length) time.
Thus you can do this without the additional log factor you
get while working with sets.
"""

class Solution:
    
    def solve(self, A, B):
        ans = []
        tree = [False, {}]

        for word in A:
            node = tree
            for ch in word:
                if ch not in node[1]:
                    node[1][ch] = [False, {}]

                node = node[1][ch]

            node[0] = True
        
        for word in B:
            node = tree
            is_found = True
            for ch in word:
                if ch not in node[1]:
                    ans.append(0)
                    is_found = False
                    break
                node = node[1][ch]
            
            if is_found:
                if node[0]:
                    ans.append(1)
                else:
                    ans.append(0)

        return ans