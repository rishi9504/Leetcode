# 977. Squares of a Sorted Array
# Solved
# Easy
# Topics
# Companies
# Given an integer array nums sorted in non-decreasing order, 
# return an array of the squares of each number sorted in non-decreasing order.

 

# Example 1:

# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].

# This code snippet sorts the squares of numbers in a given sorted array. 

# It separates the negative numbers from the non-negative numbers, squares them, and then
# merges the two lists in sorted order. 

# The key insight is that the largest squares come from the numbers with the largest absolute values,
#  which are either the most negative numbers or the most positive numbers. 

# The code uses two lists: `neg` to store the squares of the negative numbers and 
# `res` to store the final sorted result. 

# It iterates through the array, squaring each number and comparing it with the
# largest square of a negative number. If the square of the current number is smaller,
# it adds the square of the negative number to the result list. 

# Finally, it adds any remaining squares of negative numbers to the result list.


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        neg = []
        neg_idx = 0
        for i,x in enumerate(nums,start=1):
            if x<0:
                neg.append(x**2)
                neg_idx = i
            else:
                break
        res = []
        for x in nums[neg_idx:]:
            r = x**2
            while neg and  r>neg[-1]:
                res.append(neg.pop())
            res.append(r)
        while neg:
            res.append(neg.pop())
        return res