class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #Using sliding window technique
        if target in nums:
            return True
        return False    

        # l,r = 0,len(nums)-1
        # while l<=r:
        #     m = (l+r)//2
        #     if nums[m] == target:
        #         return True
        #     if nums[l] <= nums[m]:
        #         if target>=nums[l] and target<nums[m]:
        #             r=m-1
        #         else:
        #             l=m+1   
        #     else:
        #         if target<=nums[r] and target>nums[m]:
        #             l=m+1
        #         else:
        #             r=m-1
        # return False              


        
