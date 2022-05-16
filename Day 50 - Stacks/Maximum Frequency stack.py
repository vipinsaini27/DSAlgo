"""
Problem Description
You are given a matrix A which represents operations of size N x 2. Assume initially you have 
a stack-like data structure you have to perform operations on it.
Operations are of two types:
1 x: push an integer x onto the stack and return -1.
2 0: remove and return the most frequent element in the stack.
If there is a tie for the most frequent element, the element closest to the top of the stack 
is removed and returned.
A[i][0] describes the type of operation to be performed. A[i][1] describe the element x or 0 
corresponding to the operation performed.

Problem Constraints
1 <= N <= 100000
1 <= A[i][0] <= 2
0 <= A[i][1] <= 109

Input Format
The only argument given is the integer array A.

Output Format
Return the array of integers denoting the answer to each operation.

Example Input
Input 1:
A = [
            [1, 5]
            [1, 7]
            [1, 5]
            [1, 7]
            [1, 4]
            [1, 5]
            [2, 0]
            [2, 0]
            [2, 0]
            [2, 0]  ]
Input 2:
 A =  [   
        [1, 5]
        [2, 0]
        [1, 4]   ]

Example Output
Output 1:
 [-1, -1, -1, -1, -1, -1, 5, 7, 5, 4]
Output 2:
 [-1, 5, -1]

Example Explanation
Explanation 1:
 Just simulate given operations.
Explanation 2:
 Just simulate given operations.
"""

"""
Solution Approach
Pushing into a stack looks like this:
void push(int x)
{
freq[x]++;
if(freq[x] > max_freq) max_freq = freq[x];

if(stacks.count(freq[x]))
{
    stacks[freq[x]].push(x);    
}
else
{
    stack<int> st;
    st.push(x);
    stacks[freq[x]] = st;
} } 
This helps in maintaining the required answer and getting the answer to each of the  parts 
that need to be done such as push and pop of the elements
"""

class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):
        ans = []
        stack = []
        temp_stack = []
        hash = {}
        empty = lambda x: len(x) == 0
        for q in A:
            op = q[0]
            val = q[1]

            if op == 1:
                if val not in hash:
                    hash[val] = 0
                hash[val] += 1
            
                while not empty(stack) and stack[-1][1] > hash[val]:
                    temp_stack.append(stack.pop())

                stack.append((val, hash[val]))
                ans.append(-1)

                while not empty(temp_stack):
                    stack.append(temp_stack.pop())
            else:
                if not empty(stack):
                    v, c = stack.pop()
                    if v in hash:
                        hash[v] -= 1
                        if hash[v] == 0:
                            del hash[v]
                    ans.append(v)

        return ans
