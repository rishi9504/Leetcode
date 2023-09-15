class Solution:
    def trailingZeroes(self, n: int) -> int:
        zeroes = 0
        pow_5 = 5
        while pow_5<=n:
            zeroes += n//pow_5
            pow_5 *= 5
        return zeroes    
        
