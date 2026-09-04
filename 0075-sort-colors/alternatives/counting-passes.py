# 75. Sort Colors
# Solved
# Medium
# Topics
# Companies
# Hint
# Given an array nums with n objects colored red, white, or blue, sort them in-place so
#  that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.

 

# Example 1:

# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]

# This is a Python function that sorts an array of integers into three distinct groups: zeros, ones, and twos. 
# It does this in-place, meaning it modifies the original array instead of creating a new one.
# The function works by first counting the number of zeros and ones in the array, and then placing them
# in the first `z` and `z+o` positions of the array, respectively. 
# The remaining positions are filled with twos.


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
