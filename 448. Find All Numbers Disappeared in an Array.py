# 448. Find All Numbers Disappeared in an Array
# Solved
# Easy
# Topics
# Companies
# Hint
# Given an array nums of n integers where nums[i] is in the range [1, n],
#  return an array of all the integers in the range [1, n] that do not appear in nums.

# This function finds all numbers in the range [1, n] that do not appear in the input list nums, 
# where n is the length of nums. It uses set difference to achieve this.

# In essence, it creates a set of all numbers from 1 to n, 
# and then subtracts the set of numbers present in nums, 
# resulting in a set of numbers that are missing from nums.

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        #set diff
        return set(range(1,len(nums)+1))-set(nums)    


        