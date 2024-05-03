class Solution:
    def myAtoi(self, s: str) -> int:
        i=0
        sign=+1
        result=''
        if s=='+1':
            return 1
        while i< len(s) and s[i]==' ':
            i += 1
        if i < len(s) and s[i]=='-':
            sign= -1
            i+=1 
        elif i< len(s) and s[i]=='+' :
            sign = +1
            i+=1    
        while i< len(s) and s[i].isdigit():
            result = result+s[i]
            i=i+1
        # what the next lines does: Convert the string res into an integer,
        # multiply by sign and clamp the result: max(-2e31, min(2e31-1, result)).    

        return max( -2**31, min( sign * int(result or 0), 2**31 - 1 ) )           


        
