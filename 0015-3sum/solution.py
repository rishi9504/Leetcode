class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Approach: Sort the array and use a two-pointer technique to find the triplets.
        #
        # Step 1: Sort the array
        nums.sort()

        # Step 2: Iterate over the array and for each element, find a pair that sums up to its negation
        result = []
        for i in range(len(nums)):
            # Skip duplicate values for nums[i]
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Set the target for the two-pointer technique
            target = -nums[i]

            # Initialize the two pointers
            left, right = i + 1, len(nums) - 1

            # Iterate until the two pointers meet
            while left < right:
                # Calculate the current sum
                current_sum = nums[left] + nums[right]

                # If the current sum is equal to the target, then we have found a triplet
                if current_sum == target:
                    # Add the triplet to the result
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicates for nums[left] and nums[right]
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # Move pointers
                    left += 1
                    right -= 1
                
                # If the current sum is less than the target, then we need to increase the sum
                elif current_sum < target:
                    left += 1
                # If the current sum is greater than the target, then we need to decrease the sum
                else:
                    right -= 1
        
        # Return the result
        return result               




        
