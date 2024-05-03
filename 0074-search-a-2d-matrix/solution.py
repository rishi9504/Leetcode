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

        rows,cols = len(m),len(m[0])
        l,r = 0,(rows*cols)-1
        
        # l,r = 0,len(m)-1
        while l<=r:
            mid = (l+r)//2
            d,mod = divmod(mid,cols)
            # print(d,mod,l,r,mid,rows,cols,m[d][mod])
            if target == m[d][mod]:
                return True
            if target > m[d][mod]:
                l = mid+1
            else:
                r=mid-1
        return False
