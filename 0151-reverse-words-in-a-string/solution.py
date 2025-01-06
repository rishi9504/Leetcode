class Solution:
    def reverseWords(self, s: str) -> str:
        # s_str = s.split()
        # s_str.reverse()
        # return " ".join(s_str)
        
        # two pointer approach

        w = s.split()
        l,r = 0,len(w)-1
        while l<r:
            w[l],w[r] = w[r],w[l]
            l+=1
            r-=1
        return ' '.join(w)            
