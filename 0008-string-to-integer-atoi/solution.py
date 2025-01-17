class Solution:
    def myAtoi(self, s: str) -> int:
        """
        This function takes a string and returns an integer.
        The string can contain spaces, a sign (+ or -) and digits.
        The function will return the integer value of the digits in the string
        with the sign of the first sign character found or 1 if no sign is found.
        The function will return 0 if the string does not contain any digits.
        The function will return the maximum or minimum possible integer if the
        result is out of the 32-bit signed integer range.
        """
        i=0
        sign=+1
        result=''
        if s=='+1':
            return 1
        # Skip all the spaces at the beginning of the string
        while i< len(s) and s[i]==' ':
            i += 1
        # If the first non-space character is a sign, save the sign and move to the next character
        if i < len(s) and s[i]=='-':
            sign= -1
            i+=1 
        elif i< len(s) and s[i]=='+' :
            sign = +1
            i+=1    
        # While the current character is a digit, add it to the result string
        while i< len(s) and s[i].isdigit():
            result = result+s[i]
            i=i+1
        # Convert the string res into an integer, multiply by sign and clamp the result
        # max(-2e31, min(2e31-1, result))

        return max( -2**31, min( sign * int(result or 0), 2**31 - 1 ) )           


        
