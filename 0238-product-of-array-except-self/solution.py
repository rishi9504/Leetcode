class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # sums = [1]*len(nums)
        # for i,n in enumerate(nums[1:],start=1):
        #     sums[i] = sums[i-1]*n
        # print(sums)

        sums = [1]
        for i in range(1,len(nums)):
            sums.append(nums[i-1]*sums[-1])

        final=1
        for i in range(len(nums)-1,-1,-1):
            sums[i]*=final
            final*=nums[i]
        return sums        
        
