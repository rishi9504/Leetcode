class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        l,r = 0, 1
        n=len(nums)
        while l<n and r<n:
            while l<n and nums[l]%2==0:
                l+=2
            while r<n and nums[r]%2==1:
                r+=2
            if l<n and r<n:
                nums[l],nums[r] = nums[r],nums[l]
                # l+=2
                # r+=2
        return nums                

        
