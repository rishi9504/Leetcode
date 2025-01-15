class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        We use a dictionary to keep track of the numbers we've seen so far and their indices.
        Then we go through the list and for each number, we check if it's in the dictionary.
        If it is, that means we've seen it before and its complement (target - number) is in the dictionary as well.
        So we return the indices of the two numbers that sum up to the target.
        If we don't find a match, we add the number to the dictionary and keep going.
        """

        lookup = {}
        for i,n in enumerate(nums):
            # Check if we've seen the number before and if its complement is in the dictionary
            if target-n in lookup:
                # Return the indices of the two numbers that sum up to the target
                return [lookup[target-n],i]
            # If we haven't seen it before, add it to the dictionary
            lookup[n]=i
        # If we don't find a match, return an empty list
        return []
        
        
