class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        # two pointer approach, what bad description though
        l,r = 0,len(s)
        res = []
        for c in s:
            if c=="I":
                res.append(l)
                l+=1
            else:
                res.append(r) 
                r-=1
        res.append(r)
        return res          
        
