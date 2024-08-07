# from operators import xor
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        r = set()
        for n in nums:
            if n in r:
                return n
            else:
                r.add(n)
                
        # res = nums[0]
        # for n in range(len(nums)):
            
        #     # if:
        #     res^=n
        # return res
