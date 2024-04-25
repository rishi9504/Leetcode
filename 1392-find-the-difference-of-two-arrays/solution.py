class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        one = list(set(nums1)-set(nums2))
        two = list(set(nums2)-set(nums1))
        return [one,two]

        
