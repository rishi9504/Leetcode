class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_to_index = {}           # key is number, value is index in nums

        for i, num in enumerate(nums):

            if target - num in num_to_index:
                return [num_to_index[target - num], i]

            num_to_index[num] = i

        return []   # no sum
        
