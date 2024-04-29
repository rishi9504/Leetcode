
import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = set(string.ascii_lowercase+string.digits)
        s = [c for c in s.lower() if c   in chars ]
        l,r = 0,len(s)-1
        while l<r:
            if s[l].lower()!=s[r].lower():
                return False
            l+=1
            r-=1
        return True
