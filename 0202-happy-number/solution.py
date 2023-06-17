class Solution:
    def isHappy(self, n: int) -> bool:
        s = str(n)
        l = []
        while s != '1':
            c = 0
            for i in s:
                c += (int(i) ** 2)
            if c in l:
                return 0
            l.append(c)
            s = str(c)
        return 1
