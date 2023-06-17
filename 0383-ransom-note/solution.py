class Solution:
    def canConstruct(self, r: str, m: str) -> bool:
        return len(Counter(r) - Counter(m)) == 0
