class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        break_point = (len(nums) - k) % len(nums)
        nums[:] = nums[break_point:] + nums[:break_point]
        
