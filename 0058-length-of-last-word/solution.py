class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_split = s.split()
        *a,b = s_split
        return len(b)
