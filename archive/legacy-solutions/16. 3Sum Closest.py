# 16. 3Sum Closest
# Solved
# Medium
# Topics
# Companies
# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

# Return the sum of the three integers.

# You may assume that each input would have exactly one solution.

 

# Example 1:

# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).




# This is a solution to the 3Sum Closest problem. It sorts the input list `nums` 
# and then uses a two-pointer technique to find the triplet with a sum closest to the `target`. 
# The function returns this closest sum.

# Here's a brief explanation of the code:

# 1. Sort the input list `nums`.
# 2. Initialize `diff` to infinity, which will store the minimum difference between the triplet sum
# and the target.
# 3. Iterate through the list with the first pointer `i`.
# 4. For each `i`, use two pointers `start` and `end` to form a triplet with `nums[i]`.
# 5. Calculate the sum of the triplet and update `diff` and the answer `ans` if the sum is closer to the target.
# 6. Move the pointers based on whether the sum is greater than or less than the target.
# 7. Return the closest sum `ans`.

# This solution has a time complexity of O(n^2) due to the nested loops.


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums=sorted(nums)
        diff=float('inf')
        for i in range(len(nums)-1):
            start=i+1
            end=len(nums)-1
            while(start<end):
                sum=nums[i]+nums[start]+nums[end]
                if sum==target:
                    return target
                elif abs(target-sum)<diff:
                    diff=abs(target-sum)
                    ans=sum
                if sum>target:
                    end-=1
                else:
                    start+=1
        return ans