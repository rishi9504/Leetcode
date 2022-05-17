class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        x=0
        ops = {'--X':-1,'X--':-1,'++X':1,'X++':1}
        for i in operations:
            x += ops[i]
        return x    
        
