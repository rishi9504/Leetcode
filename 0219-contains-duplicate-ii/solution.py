class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
         # Create a dictionary to store the seen numbers and their indices
        num_dict = {}
    
    # Iterate through the array
        for i, num in enumerate(nums):
        # Check if the number already exists in the dictionary
            if num in num_dict:
            # Check the difference in indices
                if abs(i - num_dict[num]) <= k:
                    return True
        
        # Update the index of the number in the dictionary
            num_dict[num] = i
    
    # If no duplicate satisfying the condition is found, return False
        return False

