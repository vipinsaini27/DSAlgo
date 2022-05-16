"""
Problem Description
Given a string A denoting a stream of lowercase alphabets, you have to make a new string B.
B is formed such that we have to find the first non-repeating character each time a character is inserted to the stream and append it at the end to B. If no non-repeating character is found, append '#' at the end of B.



Problem Constraints
1 <= |A| <= 100000



Input Format
The only argument given is string A.



Output Format
Return a string B after processing the stream of lowercase alphabets A.



Example Input
Input 1:

 A = "abadbc"
Input 2:

 A = "abcabc"


Example Output
Output 1:

"aabbdd"
Output 2:

"aaabc#"


Example Explanation
Explanation 1:

"a"      -   first non repeating character 'a'
"ab"     -   first non repeating character 'a'
"aba"    -   first non repeating character 'b'
"abad"   -   first non repeating character 'b'
"abadb"  -   first non repeating character 'd'
"abadbc" -   first non repeating character 'd'
Explanation 2:

"a"      -   first non repeating character 'a'
"ab"     -   first non repeating character 'a'
"abc"    -   first non repeating character 'a'
"abca"   -   first non repeating character 'b'
"abcab"  -   first non repeating character 'c'
"abcabc" -   no non repeating character so '#'
"""

"""
Solution Approach
You need to maintain a map for each character of the stream.
After that, you can also maintain a queue for the extraction of information.
Each character is inserted and removed from the queue at most once; hence time complexity is O(n).
Code looks something like
for (auto c : A)
{
mp[c]++;
q.push(c);
while (!q.empty() && mp[q.front()] > 1) q.pop();
if (!q.empty()) ans.push_back(q.front());
else ans.push_back(‘#’);
}
"""

class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        qu = [A[0]]
        ans = A[0]
        hash = {}
        hash[A[0]] = 1
        i = 1

        while i < len(A):
            val = A[i]
            if val in hash:
                if qu:
                    if qu[0] == val or not hash[qu[0]]:
                        qu.pop(0)
                    else:
                        ans += qu[0]
                        i += 1
                    hash[val] = 0
                else:
                    ans += "#"
                    i += 1
            else:
                hash[val] = 1
                qu.append(val)
                ans += qu[0]
                i += 1
            
        return ans