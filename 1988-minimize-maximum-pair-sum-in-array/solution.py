class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        max_v = 0
        for i in range(len(nums) // 2):
            max_v = max(nums[i] + nums[-(i+1)], max_v)
        return max_v
