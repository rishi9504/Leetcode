class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # return len(set(nums)) != len(nums)  
        e = set()
        for i in nums:
            if i in e:
                return True
            e.add(i)


        
