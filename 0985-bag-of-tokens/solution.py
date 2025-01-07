class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        # using greedy two pointer approach
        tokens.sort()
        l,r = 0,len(tokens)-1
        s,ms=0,0
        while l<=r:
            if power>=tokens[l]:
                # face up
                power -= tokens[l]
                s+=1
                l+=1
                ms = max(ms,s)
            elif s>0 and l<r:
                #face down
                power+=tokens[r]
                s-=1
                r-=1
            else:
                break
        return ms                

        
