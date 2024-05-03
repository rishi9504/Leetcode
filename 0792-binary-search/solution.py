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


            # if nums[m]<target:
            #     print('1')
            #     l=m
            #     m = ((l+r)+1)//2
            # elif nums[m]> target:
            #     print('2')
            #     r=m
            #     m = ((l+r)+1)//2
            # else:
            #     return m
