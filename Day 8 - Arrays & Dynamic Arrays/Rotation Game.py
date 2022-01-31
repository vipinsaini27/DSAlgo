"""
Problem Description
You are given an integer array A and an integer B. You have to print the same array after rotating it B times towards right.
NOTE: You can use extra memory.


Problem Constraints
1 <= |A| <= 106
1 <= A[i] <= 109
1 <= B <= 109


Input Format
First line begins with an integer |A| denoting the length of array, and then |A| integers denote the array elements.
Second line contains a single integer B


Output Format
Print an array of integers which is the Bth right rotation of input array A, on a separate line.


Example Input
Input 1:
 4 1 2 3 4
 2

Input 2:
 3 1 2 2
 3


Example Output
Output 1:
 3 4 1 2

Output 2:
 1 2 2


Example Explanation
Explanation 1:
 [1,2,3,4] => [4,1,2,3] => [3,4,1,2]

Explanation 2:
 [1,2,2] => [2,1,2] => [2,2,1] => [1,2,2]
"""


def main():
    s = input()
    r = int(input())

    inpt = s.split(' ')
    l = int(inpt[0])
    arr = []
    for i in range(1, l + 1):
        arr.append(int(inpt[i]))

    r = r % l

    temp = []
    for i in range(l - r, l):
        temp.append(arr[i])

    i = l - r - 1
    j = l - 1
    while i > -1:
        arr[j] = arr[i]
        i -= 1
        j -= 1

    i = 0
    while i < len(temp):
        arr[i] = temp[i]
        i += 1

    for val in arr:
        print(val, end=' ')
    print()


if __name__ == '__main__':
    main()