class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        start, end = 0,0
        max_index = 0
        steps = 1
        while True:
            for i in range(start, end+1):
                max_index = max(max_index, i+nums[i])
            if max_index >= len(nums)-1:
                return steps
            steps+=1
            start, end = end+1, max_index                  


        
