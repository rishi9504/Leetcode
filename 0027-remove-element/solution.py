class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # while val in nums:
        #     nums.remove(val)
        #while that work, tried solving two pointer app

        k=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[k]=nums[i]
                k+=1
        return k                   


