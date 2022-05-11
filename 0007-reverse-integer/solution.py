class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > -1:
            return int(str(x)[::-1]) if int(str(x)[::-1]) < 2147483647 else 0
        else:
            return int("-"+str(abs(x))[::-1]) if int("-"+str(abs(x))[::-1]) > -2147483647 else 0
        
