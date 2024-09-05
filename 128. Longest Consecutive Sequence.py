# 128. Longest Consecutive Sequence
# Solved
# Medium
# Topics
# Companies
# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.



# This code finds the length of the longest consecutive sequence of numbers in a given list `nums`. It does this by:

# 1. Converting the list to a set `m` for efficient lookups.
# 2. Iterating over each number `i` in the set.
# 3. If `i-1` is in the set, it means `i` is not the start of a sequence, so it skips to the next number.
# 4. If `i-1` is not in the set, it counts the length of the sequence starting 
#    from `i` by incrementing `i` until it's no longer in the set.
# 5. It keeps track of the longest sequence found so far and returns it.

# This code has a time complexity of O(n) because it performs a constant amount of work
# for each number in the list, and a linear amount of work for each number in the input list.

from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:        
        m = set(nums)  # {1,2,3,100,4,200 }
        print (m)
        longest = 0

        for i in m:
            if i-1 in m:
                continue
            seq=0
            while i in m:
                seq+=1
                i+=1
            longest = max(longest,seq)
        return longest  