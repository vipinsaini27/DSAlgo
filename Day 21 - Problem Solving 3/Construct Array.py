"""
Problem Description
Simba has an integer array of length A. Despite having insisted alot, He is not ready to reveal the array to his friend
Expert. But now, he is ready to reveal some hints about the array and challenges Expert to find the values of his hidden
array. The hints revealed are as follows:
The array is sorted by values in ascending order.
All the elements in the array are distinct and positive (greater than 0).
The array contains two elements B and C such that B < C.
Difference between all adjacent (consecutive) elements are equal.
Among all the arrays satisfying the above conditions, his array has the minimum possible maximum element value.
If there are multiple possible arrays, his array will have minimum possible minimum element value.
Can you help Expert to construct such an array and surprise Simba?

Problem Constraints
2 <= A <= 50
1 <= B < C <= 50

Input Format
First argument is an integer A.
Second argument is an integer B.
Third argument is an integer C.

Output Format
Return a sorted integer array having length N, denoting Simba's Secret Array.

Example Input
Input 1:
 A = 5
 B = 20
 C = 50
Input 2:
 A = 2
 B = 2
 C = 3

Example Output
Output 1:
 [10, 20, 30, 40, 50]
Output 2:
 [2, 3]

Example Explanation
Explanation 1:
 Sorted array = [10, 20, 30, 40, 50] satisfies all the conditions having maximum value = 50 minimum possible.
 Other arrays such as [20, 30, 40, 50, 60] having max value = 60 or [20, 50, 80, 120] having max value = 120, also satisfy conditions but their maximum value is not minimum possible(As minimum possible max value is 50).
Explanation 2:
 As the array has only 2 elements, [2, 3] is the only possible candidate.
"""

"""
Solution Approach
The only fact required to solve this problem is just to notice that the answer array is just an arithmetic progression.
After that, we can fix the first element ‘a’, fix the difference ‘d’, construct the array 
[a, a + d, a + 2 * d, …, a + d * (A − 1)], check if B and C are in this array and, if yes, update the answer with this 
array.
This is O(n^3) solution.
"""

class Solution:

    def solve(self, A, B, C):
        n = C - B
        d = n
        while d > 0:
            if n % d == 0:
                firstElem = C - (A - 1)*d
                if (firstElem > 0 and firstElem <= B) or firstElem > B:
                    break

            d -= 1

        if firstElem > B:
            d += 1
            while n % d != 0:
                d += 1
            if d < B:
                firstElem = d
            else:
                firstElem = B
        elif firstElem < 1:
            d = 1
            firstElem = 1

        ans = []
        for i in range(A):
            ans.append(firstElem + d*i)

        return ans