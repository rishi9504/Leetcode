class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n= len(numbers)
        l= 0 
        r= n-1
        res=[]
        while l<r:
            if (numbers[l] + numbers[r] ==target):
                res.append(l+1)
                res.append(r+1)
            if (numbers[l]+numbers[r]>target):
                r-=1
            else:
                l+=1
        res.sort()
        return res
