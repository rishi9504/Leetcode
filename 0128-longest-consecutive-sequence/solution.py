from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:        
        # m = defaultdict(list)
        # for i,n in enumerate(nums):
        #     m[n].append(n)
        #     if n-1 in m:



        m = set(nums)  # {1,2,3,100,4,200 }
        print (m)
        longest = 0

        for i in m:
            if i-1 in m:
                continue
            seq=0
            while i in m:
                seq+=1
                i+=1
            longest = max(longest,seq)
        return longest           




