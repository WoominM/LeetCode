class Solution:
    def addBinary(self, a: str, b: str) -> str:
        out = ''
        a, b = sorted([a, b], key=len)
        minl, maxl = len(a), len(b)
        a, b = a[::-1], b[::-1]
        a += '0' * (maxl - minl)

        d = 0
        for i in range(maxl):
            c = int(a[i]) + int(b[i]) + d
            if c == 3:
                c, d = 1, 1
            elif c == 2:
                c, d = 0, 1
            else:
                d = 0
            out += str(c)
        if d == 1:
            out += str(d)
        return out[::-1]