"""
Rearrange a given array so that Arr[i] becomes Arr[Arr[i]] with O(1) extra space.

Example:

Input : [1, 0]
Return : [0, 1]
Lets say N = size of the array. Then, following holds true :

All elements in the array are in the range [0, N-1]
N * N does not overflow for a signed integer
"""

"""
Solution Approach
If you had extra space to do it, the problem will be very easy.
Store a copy of Arr in B.

And then for every element, do Arr[i] = B[B[i]]

Lets restate what we just said for extra space :

If we could somehow store 2 numbers in every index ( that is, Arr[i] can contain the old value and the new value somehow 
), then the problem becomes very easy.
NewValue of Arr[i] = OldValue of Arr[OldValue of Arr[i]]

Now, we will do a slight trick to encode 2 numbers in one index.
This trick assumes that N * N does not overflow.

1) Increase every Array element Arr[i] by (Arr[Arr[i]] % n)*n.
2) Divide every element by N.
Given a number as

   A = B + C * N   if ( B, C < N )
   A % N = B
   A / N = C
We use this fact to encode 2 numbers into each element of Arr.
"""


class Solution:

    def arrange(self, A):
        l = len(A)
        for i in range(l):
            old = A[i]
            if i > old:
                new = A[old] % l
            else:
                new = A[old]

            A[i] = old + (new%l)*l

        for i in range(l):
            A[i] = A[i] // l

        return A