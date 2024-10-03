

# just number of disjoint pairs with sum k
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0
        num_dict = {}
        for num in nums:
            comp = k-num
            if comp in num_dict and num_dict[comp]>0:
                count+=1
                num_dict[comp]-=1
            else:
                num_dict[num] =num_dict.get(num,0)+1
        return count            

        
