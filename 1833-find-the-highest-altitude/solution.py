class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        m,c=0,0
        for i in gain:
            c += i
            m=max(m,c)
        return m
        
