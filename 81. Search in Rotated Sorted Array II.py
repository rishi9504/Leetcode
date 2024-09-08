# 81. Search in Rotated Sorted Array II
# Solved
# Medium

# There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

# Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length)
#  such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]
# (0-indexed).
# For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

# Given the array nums after the rotation and an integer target, return true if target is in nums,
# or false if it is not in nums.

# You must decrease the overall operation steps as much as possible.

# Explanation



# This is a binary search algorithm designed to find a target value in a rotated sorted array
# with duplicate values.

# The algorithm handles the duplicates by incrementing the `low` pointer when `nums[low]`
# equals `nums[mid]`, effectively skipping over the duplicate values. 
# Otherwise, it uses the standard binary search approach to narrow down the search space.

# The function returns `True` if the target is found and `False` otherwise.

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return True
         
            if nums[low] == nums[mid]:
                low += 1
                continue
            
            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        
        return False