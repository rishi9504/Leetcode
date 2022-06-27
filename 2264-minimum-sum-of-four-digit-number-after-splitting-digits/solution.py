class Solution:
    def minimumSum(self, num: int) -> int:
        n=sorted([int(x) for x in str(num)])
        return int(str(n[0])+str(n[2]))+int(str(n[1])+str(n[3]))
        
