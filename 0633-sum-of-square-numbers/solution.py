class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l=0
        r=int(c**0.5)
        while l<=r:
            cs = l**2+r**2
            if cs ==c:
                return True
            elif cs<c:
                l+=1
            else:
                r-=1
        return False                


        
