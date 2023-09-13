class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = float('-inf')
        sell = 0
        for price in prices:
            buy = max(-price,buy)
            sell = max(price+buy,sell)
        return sell    
        
