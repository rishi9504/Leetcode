class Solution(object):
    def reverse(self, x):
        """
        Reverse the digits of an integer.

        :type x: int
        :rtype: int
        """
        # Check if the number is non-negative
        if x >= 0:
            # Convert the number to a string, reverse the string, and convert it back to an integer
            reversed_num = int(str(x)[::-1])
            # Check if the reversed number is within the 32-bit signed integer range
            if reversed_num < 2147483647:
                return reversed_num
            else:
                # Return 0 if the reversed number is not within the range
                return 0
        else:
            # Convert the negative number to a positive, reverse it, and add a negative sign
            reversed_num = int("-" + str(abs(x))[::-1])
            # Check if the reversed number is within the 32-bit signed integer range
            if reversed_num > -2147483648:
                return reversed_num
            else:
                # Return 0 if the reversed number is not within the range
                return 0
        
