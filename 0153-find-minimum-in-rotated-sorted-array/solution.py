class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-1
        cm = nums[r]
        while l<r:
            m = (l+r)//2
            # print(l,r,m,nums[m])
            if nums[m]<cm:
                cm = nums[m]
            if nums[m]>nums[r]:
                l=m+1
            else:
                r=m
        return cm
