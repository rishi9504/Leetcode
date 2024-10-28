class Solution:
    def addDigits(self, num: int) -> int:
        if num<10:
            return num
        res=num
        while res>=10:
            res=sum([int(i) for i in str(res)])
        return res
        
