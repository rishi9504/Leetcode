class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        even = [v for i,v in enumerate(nums) if i%2==0]
        odd = [v for i,v in enumerate(nums) if i%2!=0]
        even.sort()
        odd.sort(reverse=True)
        res = []
        for i,j in zip(even,odd):
            res.extend([i,j])
        if len(even)==len(odd):
            return res
        elif len(even)>len(odd):
            res.append(even[-1])
        else:
            res.append(odd[-1])
        return res
