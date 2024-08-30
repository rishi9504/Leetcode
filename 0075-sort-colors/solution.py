class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # nums = nums.sort()

        z,o,t = 0,0,0
        for n in nums:
            if n==0:
                z+=1
            elif n==1:
                o+=1
            else:
                t+=1
        for i in range(0,z):
            nums[i]=0
        for i in range(z,z+o):
            nums[i]=1
        for i in range(z+o,len(nums)):
            nums[i]=2                
        # print(f'{z=},{o=}{t=}')
        # c = 0
        # i=0
        # for i in range(z):
        #     nums[i+c]=0
        #     print(f'{i=},{nums=}')
        # print(nums)
        # c=i+1
        # print(f'{c=}')
        # for i in range(o):
        #     nums[i+c]=1
        #     print(f'{i=},{nums=}')
        # c=c+i+1
        # print(f'{c=}')
        # print(nums)
        # for i in range(t):
        #     nums[i+c]=2
        #     print(f'{i=},{nums=}')
        # print(nums)
        
        
        # return nums
