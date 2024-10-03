class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        k=1
        i=0
        for j in range(len(nums)):
            k -= nums[j] == 0
            if k < 0:
                k+=nums[i]==0
                i+=1
        return j-i      

        
