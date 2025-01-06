class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #modification of two pointer approach, using three pointers
        l,c,h = 0,0,len(nums)-1
        while c<=h:
            if nums[c]==0:
                nums[l],nums[c] = nums[c],nums[l]
                l+=1
                c+=1
            elif nums[c]==2:
                nums[h],nums[c] = nums[c],nums[h]
                h-=1
            else:
                c+=1        
