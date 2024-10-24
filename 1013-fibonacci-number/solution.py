class Solution:
    def fib(self, n: int) -> int:
        if n<=1:
            return n
        p1,p2 = 0,1
        for i in range(1,n+1):
            c = p1+p2
            p2,p1 = c,p2
        return p1        

        
