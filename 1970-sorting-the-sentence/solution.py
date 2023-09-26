class Solution:
    def sortSentence(self, s: str) -> str:
        return ' '.join(x[1:] for x in sorted(i[-1]+i[:-1] for i in s.split()))
