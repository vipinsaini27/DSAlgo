
def fun(s):
    zArr = [0]*len(s)
    zArr[0] = len(s)
    i = 1
    preFixEnd = -1
    preFixStart = -1
    while i < len(s):
        if i > preFixEnd:
            preFixStart = i
            sz = 0
            j = 0
            while i+j < len(s) and s[i+j] == s[j]:
                j += 1
                sz += 1
            preFixEnd = i+j
            zArr[i] = sz
        else:
            sz = s[i-preFixStart]
            if i+sz < preFixEnd:
                zArr[i] = sz
            else:
                j = preFixEnd + 1
                k = 








s = "xxyzxxyzwxxyzxxyzx"
zArr = fun(s)
print(zArr)