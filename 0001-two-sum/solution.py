class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_done={}
        for i, num in enumerate(nums):
            if target-num in dict_done:
                return [dict_done[target-num],i]
            dict_done[num] = i
        return []        

        
