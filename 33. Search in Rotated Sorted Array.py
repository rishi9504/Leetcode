# 33. Search in Rotated Sorted Array
# Solved
# Medium
# Topics
# Companies
# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.

# This code snippet is an implementation of a binary search algorithm to find the index of a target value in a rotated sorted array. The `search` function takes in a list of integers `nums`, an integer `target`, and returns the index of the target if it is found, or -1 if it is not found.

# The algorithm uses a sliding window technique to divide the search space in half at each step. It initializes two pointers, `l` and `r`, to the start and end of the array. The function then enters a while loop that continues until `l` is less than or equal to `r`.

# Inside the loop, the function calculates the midpoint `m` of the current search space. It checks if the value at the midpoint is equal to the target. If so, it returns the index of the midpoint.

# If the value at the midpoint is not equal to the target, the function checks if the left half of the array is sorted. If it is, it compares the target with the values at the left and midpoint. If the target is between the values, it updates the right pointer to `m-1`. Otherwise, it updates the left pointer to `m+1`.

# If the left half of the array is not sorted, it means the right half is sorted. In this case, the function compares the target with the values at the right and midpoint. If the target is between the values, it updates the left pointer to `m+1`. Otherwise, it updates the right pointer to `m-1`.

# If the target is not found after the loop, the function returns -1.


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #Using sliding window technique
        l,r = 0,len(nums)-1
        while l<=r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            if nums[l] <= nums[m]:
                if target>=nums[l] and target<nums[m]:
                    r=m-1
                else:
                    l=m+1   
            else:
                if target<=nums[r] and target>nums[m]:
                    l=m+1
                else:
                    r=m-1
        return -1                
