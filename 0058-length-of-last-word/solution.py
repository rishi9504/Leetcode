class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        x = s.split()
        y=len(x[len(x)-1])
        return y
        
