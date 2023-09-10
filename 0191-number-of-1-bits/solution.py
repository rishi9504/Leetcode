class Solution:
    def hammingWeight(self, n: int) -> int:
        return sum(c=='1' for c in bin(n)[2:])
        
