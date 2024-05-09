class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # l = len(nums1)+len(nums2)
        # m = l//2
        # a1,a2 = nums1[:m],nums2[:m]

        # a1l = a1[-1]
        # a2f = a1[0]
        # if a1l<a2f:
        #     try:
        #         return a1[m]
        #     except:
        #         pass
                
        #     try:
        #         return a2[m%len(a1)]
        #     except:
        #         pass
                

        
        # if a2 and a2[-1] > a1[-1]:
        #     return a2[-1]
        # if a1 and a2[-1] <= a1[-1]:
        #     return a1[-1]
        # for i,j in zip(a1[::-1],a2[::-1]):
        #     if 

        # nlogn solution
        c= nums1+nums2
        c.sort()
        n = len(c)

        if n%2!=0:
            med = c[int(n/2)]
        else:
            b=int(n/2)
            a=b-1
            med = (c[a]+c[b])/2
        return med   




