"""
Problem Description
Given an array, A of integers of size N. Find the subarray AL, AL+1, AL+2, ... AR with 1<=L<=R<=N, which has maximum XOR value.

NOTE: If there are multiple subarrays with the same maximum value, return the subarray with minimum length. If the length is the same, return the subarray with the minimum starting index.



Problem Constraints
1 <= N <= 100000
0 <= A[i] <= 109



Input Format
First and only argument is an integer array A.



Output Format
Return an integer array B of size 2. B[0] is the starting index(1-based) of the subarray and B[1] is the ending index(1-based) of the subarray.



Example Input
Input 1:

 A = [1, 4, 3]
Input 2:

 A = [8]


Example Output
Output 1:

 [2, 3]
Output 2:

 [1, 1]


Example Explanation
Explanation 1:

 There are 6 possible subarrays of A:
 subarray            XOR value
 [1]                     1
 [4]                     4
 [3]                     3
 [1, 4]                  5 (1^4)
 [4, 3]                  7 (4^3)
 [1, 4, 3]               6 (1^4^3)

 [4, 3] subarray has maximum XOR value. So, return [2, 3].
Explanation 2:

 There is only one element in the array. So, the maximum XOR value is equal to 8 and the only possible subarray is [1, 1]. 
"""

"""
Solution Approach
Build a prefXor array in which the ith element represents the xor of all elements from 0 to i. To find the xor of any subarray[l..r], we can just take the xor of prefXor[r] and prefXor[l-1].

To find the maximum xor subarray ending at the index i, insert the bit representation(starting from most significant bit) of all the elements of prefXor array upto i-1 into the trie data structure.
We have two possible cases at ith index.

The prefix itself has maximum xor.
We need to remove some prefix (ending at index from 0 to i-1).Try to have most significant bit to be set bit i.e. 1. As we have maintained the trie data structure of bit representation of i-1 elements of prefXor array, we can find the maximum xor in O(logm) where m is the maximum number present in the given array.
We can find the maximum subarray ending at every index and return the subarray, which has the maximum XOR value.
"""

class Solution:

    def insert(self, tree, bin, num, idx):
        node = tree
        for bit in bin:
            if bit not in node[2]:
                node[2][bit] = [None, None, {}]

            node = node[2][bit]

        node[0] = num
        node[1] = idx

        return tree

    def search(self, tree, bin):
        node = tree
        for bit in bin:
            if bit == '1':
                if '0' in node[2]:
                    node = node[2]['0']
                else:
                    node = node[2]['1']
            elif bit == '0':
                if '1' in node[2]:
                    node = node[2]['1']
                else:
                    node = node[2]['0']

        return (node[0], node[1])

    def solve(self, A):
        preFixXOR = [A[0]]
        preFixXORBin = []
        for i in range(1, len(A)):
            preFixXOR.append(A[i] ^ preFixXOR[i-1])
        
        for num in preFixXOR:
            preFixXORBin.append(bin(num).replace("0b", ""))

        max_len = 0
        for bit in preFixXORBin:
            if len(bit) > max_len:
                max_len = len(bit)

        i = 0
        while i < len(preFixXORBin):
            val = preFixXORBin[i]
            l = len(preFixXORBin[i])
            preFixXORBin[i] = "".join(("0"*(max_len - l), val))
            i += 1

        tree = [None, None, {}]
        maxXOR = preFixXOR[0]
        s, e = 1, 1
        tree = self.insert(tree, preFixXORBin[0], preFixXOR[0], 1)

        i = 1
        while i < len(preFixXOR):
            binary = preFixXORBin[i]
            val = preFixXOR[i]

            (num, idx) = self.search(tree, binary)

            if val > maxXOR:
                maxXOR = val
                s = 1
                e = i + 1

            if num^val > maxXOR:
                maxXOR = num^val
                s = idx + 1
                e = i + 1
            elif num^val == maxXOR:
                s1 = idx + 1
                e1 = i + 1
                if e1-s1 < e-s:
                    s = s1
                    e = e1
                elif e1-s1 == e-s:
                    if s1 < s:
                        s = s1
                        e = e1

            tree = self.insert(tree, binary, val, i+1)
            
            i += 1

        return [s, e]