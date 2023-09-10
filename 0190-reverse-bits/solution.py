class Solution:
    def reverseBits(self, n: int) -> int:
        return int((('{0:032b}'.format(n))[::-1]),2)
        # ('{0:032b}'.format(n) Converts to a 32 bit representation of the number in binary. 
        #This is formatted as a string
