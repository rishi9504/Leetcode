class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # r = set()
        # res = []
        # for n in nums:
        #     if n in r:
        #         res.append(n)
        #     else:
        #         r.add(n)
        # return res
        ans=[]
        for n in nums:
            if nums[abs(n)-1]<0:
                ans.append(abs(n))
            else:
                nums[abs(n)-1]=-nums[abs(n)-1]
        return ans            
