class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        """
        Returns True if we can write c as a sum of two perfect squares, False otherwise.
        """
        # Initialize two pointers, one at the beginning of the range and one at the
        # end of the range. This range is [0, int(c**0.5)].
        l = 0
        r = int(c**0.5)
        
        # Loop until the two pointers meet
        while l <= r:
            # Calculate the sum of the squares of the two values at the pointers
            cs = l**2 + r**2
            
            # If the sum is equal to c, then we've found two perfect squares that sum
            # to c, so return True.
            if cs == c:
                return True
            
            # If the sum is less than c, then we need to increase the sum, so we
            # increment the left pointer to make the sum larger. This is because the
            # square of the value at the left pointer is being added to the sum, and
            # increasing the value at the left pointer will increase the sum.
            elif cs < c:
                l += 1
            
            # If the sum is greater than c, then we need to decrease the sum, so we
            # decrement the right pointer to make the sum smaller. This is because the
            # square of the value at the right pointer is being added to the sum, and
            # decreasing the value at the right pointer will decrease the sum.
            else:
                r -= 1
        
        # If the loop completes without finding two perfect squares that sum to c,
        # then return False.
        return False


        
