class Solution:
    def reverseWords(self, s: str) -> str:
        s_str = s.split()
        s_str.reverse()
        return " ".join(s_str)

