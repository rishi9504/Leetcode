class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        return ((c & a) ^ a).bit_count() + ((c & b) ^ b).bit_count() + (((a | b) & c) ^ c).bit_count()
