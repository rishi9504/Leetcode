import time
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        res = []
        i,j=0,0
        time.sleep(0.1)
        while j<len(nums2) and i < len(nums1):
            if nums1[i]<nums2[j]:
                i+=1
            elif nums1[i]>nums2[j]:
                j+=1
            else:
                res.append(nums1[i])
                i+=1
                j+=1
        return res        

