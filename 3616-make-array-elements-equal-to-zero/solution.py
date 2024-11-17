class Solution:
    def countValidSelections(self,nums):
        n = len(nums)
        
        def simulate(start_pos, direction, curr_nums):
            nums_copy = curr_nums.copy()
            curr = start_pos
            
            while 0 <= curr < n:
                if nums_copy[curr] == 0:
                    curr = curr + (1 if direction else -1)
                else:
                    nums_copy[curr] -= 1
                    direction = not direction
                    curr = curr + (1 if direction else -1)
            
            return all(num == 0 for num in nums_copy)
        
        valid_count = 0
        
        for pos in range(n):
            if nums[pos] == 0:
                if simulate(pos, True, nums):
                    valid_count += 1
                
                if simulate(pos, False, nums):
                    valid_count += 1
        
        return valid_count
    
    
    
            
