class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # return [x for x in nums if x % 2 == 0] + [x for x in nums if x % 2 == 1]
        i,j = 0, len(nums)-1
        while i<j:
            while i<j and nums[i]%2==0:
                i+=1
            while i<j and nums[j]%2==1:
                j-=1
            nums[i],nums[j] = nums[j],nums[i]
        return nums        
