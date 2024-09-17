class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # sliding window
        ans=0
        c=0
        v="aeiou"
        for i,j in enumerate(s):
            if i>=k:
                if s[i-k] in v:
                    c-=1
            if s[i] in v:
                c+=1
            ans = max(c,ans)
        return ans                
        
