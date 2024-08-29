class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        neg = []
        neg_idx = 0
        for i,x in enumerate(nums,start=1):
            if x<0:
                neg.append(x**2)
                neg_idx = i
            else:
                break
        # neg.reverse()
        # print(neg)
        res = []
        for x in nums[neg_idx:]:
            r = x**2
            # print(r,x)
            while neg and  r>neg[-1]:
                res.append(neg.pop())
            res.append(r)
        while neg:
            res.append(neg.pop())
        return res
            

