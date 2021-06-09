def trib(n, c=1, p=0, pp=0):
    if (n == 0):
        return pp
    if (n == 1):
        return p
    if (n == 0):
        return c
    else:
        return trib(n - 1, c + p + pp, c, p)


for i in range(trib(35)):
    print(i)
