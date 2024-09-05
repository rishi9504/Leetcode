class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        z,o = 0,0
        for n in nums:
            if n==0:
                z+=1
            elif n==1:
                o+=1
        for i in range(0,z):
            nums[i]=0
        for i in range(z,z+o):
            nums[i]=1
        for i in range(z+o,len(nums)):
            nums[i]=2                

