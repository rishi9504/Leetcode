class Solution:
    def countAsterisks(self, s: str) -> int:
        return sum(chunk.count('*') for chunk in s.split('|')[0::2])

        
