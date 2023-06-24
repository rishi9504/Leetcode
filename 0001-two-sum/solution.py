class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
         # Create a dictionary to store the complement of each number
        complement_map = {}
    
    # Iterate through the array
        for i, num in enumerate(nums):
        # Check if the complement of the current number exists in the dictionary
            complement = target - num
            if complement in complement_map:
            # Return the indices of the two numbers
                return [complement_map[complement], i]
        
        # Store the index of the current number in the dictionary
            complement_map[num] = i
    
    # If no solution is found, return an empty list
        return []
