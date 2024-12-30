class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        r=len(numbers)-1
        cs = 0
        while l<r:
            cs = numbers[l] + numbers[r]
            if cs == target:
                return [l+1,r+1]
            elif cs<target:
                l+=1
            else: 
                r-=1
                        


