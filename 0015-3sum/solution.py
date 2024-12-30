class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # approach: sort and use two pointers pattern, make one element as anchor and check with 
        # other two elements
        nums.sort()  # Step 1: Sort the array
        result = []
        
        for i in range(len(nums)):
            # Skip duplicate values for nums[i]
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            target = -nums[i]
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                current_sum = nums[left] + nums[right]
                
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
                
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1
        
        return result               




        
