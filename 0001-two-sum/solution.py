class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        lookup = {}
        for i,n in enumerate(nums):
            if target-n in lookup:
                return [lookup[target-n],i]
            lookup[n]=i
        return []
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j]==target:
        #             return [i,j]

        
