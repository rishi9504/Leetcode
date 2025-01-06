class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        #easy method
        # s=list(s)
        # for i in range(0,len(s),2*k):
        #     s[i:i+k]=(s[i:i+k])[::-1]
        # return ''.join(s)

        s = list(s)
        n = len(s)
        for i in range(0,n,2*k):
            l=i
            r = min(i+k-1,n-1)
            while l<r:
                s[l],s[r] = s[r],s[l]
                l+=1
                r-=1
        return ''.join(s)        
            
