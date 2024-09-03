class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        #set diff
        return set(range(1,len(nums)+1))-set(nums)    


        
