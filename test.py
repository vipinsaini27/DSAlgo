import math

maxN = 1000001
prime = [0] * maxN
flag = 0
mod = 1e9 + 7

def pre():
    global flag, maxN, prime
    flag = 1
    prime[1] = 1
    for i in range(2, maxN):
        if prime[i] == 0:
            j = i * i
            while j < maxN:
                prime[j] = 1
                j += i

def power(x, y):
    res = 1
    while y:
        if y % 2:
            res = (x * res) % mod
        y = y // 2
        x = (x * x) % mod
    return res

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        global flag, prime,mod
        if flag == 0:
            pre()
        n = len(A)
        A.sort()
        v = []
        for i in range(2, A[n - 1] + 1):
            if prime[i] == 0:
                v.append(i)
        print(v)
        ans = 0
        j = 0
        i = 0
        print(A)
        while i < n and j < len(v):
            cnt = 0
            if A[i] == 1:
                i += 1
                continue
            while i < n and A[i] < v[j]:
                i += 1
                cnt += 1
            temp = math.pow(2, cnt) - 1
            temp += mod
            temp %= mod
            ans += temp
            ans %= mod
            j += 1
        if i < n:
            temp = math.pow(2, n - i) - 1
            temp += mod
            temp %= mod
            ans += temp
            ans %= mod
        return int(ans)

A = [2, 3, 2, 3]
ans = Solution().solve(A)
print(ans)