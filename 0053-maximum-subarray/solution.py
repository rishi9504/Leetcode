class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        over_max = float('-inf')
        max_end = 0
        for num in nums:
            if max_end>0:
                max_end+=num
            else:
                max_end=num
            over_max = max(over_max,max_end)
        return over_max            
        
