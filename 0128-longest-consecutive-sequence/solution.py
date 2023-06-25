class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
         # Create a set to store the unique elements of the array
        num_set = set(nums)
    
    # Initialize the maximum length
        max_length = 0
    
    # Iterate through the array
        for num in nums:
        # Check if the current element is the start of a sequence
            if num - 1 not in num_set:
            # Calculate the length of the consecutive sequence
                current_length = 1
                current_num = num
            
            # Increment the current element until the next element is not in the set
                while current_num + 1 in num_set:
                    current_length += 1
                    current_num += 1
            
            # Update the maximum length if necessary
                max_length = max(max_length, current_length)
    
    # Return the maximum length of the consecutive sequence
        return max_length
