

a = 2
p = 11
m = 13
x = 1

while p > 1:
    if p%2 == 0:
        p = p // 2
        a = (a * a) % m
    else:
        p = (p - 1) // 2
        x = x * a
        a = (a * a) % m

print((a * x) % m)