class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        pl,c=0,0
        cl=1
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                cl+=1
            else:
                pl=cl
                cl=1
            if pl>=cl:
                c+=1
        return c                 
        
