class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        next = 2
        for index in range(2,len(nums)):
            if nums[index] != nums[next-2]:
                nums[next] = nums[index]
                next+=1
        return min(next,len(nums))        

        
