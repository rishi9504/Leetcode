class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        k = 0
        while i < (len(nums)):
            nums[k] = nums[i]
            k += 1
            j = i + 1
            while j < len(nums) and nums[j] == nums[i]:
                j += 1
            i = j
        return k
        
