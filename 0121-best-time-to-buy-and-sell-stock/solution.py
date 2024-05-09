class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1
        maxP = 0
        while r<len(prices):
            if prices[r]>prices[l]:
                maxP = max(maxP,(prices[r]-prices[l]))
            else:
                l=r
            r+=1
        return maxP

        
