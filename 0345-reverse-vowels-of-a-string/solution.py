class Solution:
    def reverseVowels(self, s: str) -> str:
        s=list(s)
        l,r=0,len(s)-1
        vowels = set('aeiouAEIOU')
        while l<r:
            while l<r and s[l] not in vowels:
                l+=1
            while l<r and s[r] not in vowels:
                r-=1
            s[l],s[r]=s[r],s[l]
            r-=1
            l+=1

        return ''.join(s)
