class Solution:
    def countBits(self, n: int) -> List[int]:
        # a,b=0,0
        # sol={0:0,1:1,2:2}
        # for i in range(2,n):
        #     s =i/2
        #     sol[s]=s+
        res = [0]*(n+1)
        s = 1
        for i in range(1,n+1):
            if s == i/2:
                s=i
            res[i] = 1 + res[i-s]
        return res        
