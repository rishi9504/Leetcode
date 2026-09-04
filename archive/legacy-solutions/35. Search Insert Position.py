# 35. Search Insert Position
# Solved
# Easy
# Topics
# Companies
# Given a sorted array of distinct integers and a target value, return the index if the target is found.
#  If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.



# This is a binary search algorithm. 
# It finds the index of a `target` value in a sorted list `nums`. 
# If the `target` is not found, it returns the index where it should be inserted to maintain the sorted order. 

# The algorithm iteratively divides the search space in half until 
# it finds the target or determines its insertion point.

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)-1
        pos = 0
        while (l<=r):
            mid = (l+r)//2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                l = mid+1
            else:
                r =mid-1
        return l            
