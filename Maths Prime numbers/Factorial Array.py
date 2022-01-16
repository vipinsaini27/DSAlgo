
class Solution:

    mod = 10**9 + 7
    elem_mod = 10**6

    def getPrime(self, arr, n):
        i = 2
        while i*i <= n:
            if arr[i]:
                for j in range(i*i, n+1, i):
                    arr[j] = 0
            i += 1

    def solve(self, A):
        n = max(A)
        tmp_arr = [1]*(n+1)
        self.getPrime(tmp_arr, n)
        prime_arr = []
        for i in range(1, n+1):
            if tmp_arr[i]:
                prime_arr.append(i)

        return prime_arr

A = [2, 3, 2, 3]
ans = Solution().solve(A)
print(ans)