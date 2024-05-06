class Solution:

    def search(self, nums: List[int], target: int) -> int:
        
        left,right = 0,len(nums)-1
        # if nums[m]==target:
        #     return m
        while left<=right:
            mid = (left+right)//2
            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                left = mid+1
            else:
                right=mid-1
        return -1
    def searchMatrix(self, m: List[List[int]], target: int) -> bool:
        
        # t,b = 0,len(m)-1
        # while m[t][0]<=m[b][]:
        nums = [i for j in m for i in j]
        left,right = 0,len(nums)-1
        # if nums[m]==target:
        #     return m
        while left<=right:
            mid = (left+right)//2
            if target == nums[mid]:
                return True
            if target > nums[mid]:
                left = mid+1
            else:
                right=mid-1
        return False
