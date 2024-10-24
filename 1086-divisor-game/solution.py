class Solution:
    def divisorGame(self, n: int) -> bool:
        # dp[i] will be true if the starting player has winning start with i
        dp = [False]*(n+1)
        for i in range(2,n+1):
            for x in range(1,i):
                if i%x==0 and not dp[i-x]:
                    dp[i] = True
                    break
        return dp[n]            
        
