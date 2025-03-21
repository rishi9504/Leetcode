class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_len, p_len = len(s), len(p)
        dp = [[False] * (p_len + 1) for _ in range(s_len + 1)]

        dp[0][0] = True
        for j in range(1, p_len + 1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2]
        for i in range(1, s_len + 1):
            for j in range(1, p_len + 1):
                if p[j-1] in {s[i-1], '.'}:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i][j-2] or (dp[i-1][j] and p[j-2] in {s[i-1], '.'})
        return dp[s_len][p_len]
        
