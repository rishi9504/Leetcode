class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        This function returns True if the given string s matches the regular expression p, and False otherwise.

        The algorithm used is dynamic programming. The idea is to build a 2D array where dp[i][j] is True if the first i characters of s match the first j characters of p.

        The base case is when both s and p are empty, in which case dp[0][0] is True.

        The recursive case is when we have two options:

        1. If the current character of p is '*', then we can either ignore the '*' and move to the next character of p, or we can use the '*' to match the current character of s and move to the next character of s.

        2. If the current character of p is not '*', then we must match the current characters of s and p, and move to the next character of both s and p.
        """
        s_len, p_len = len(s), len(p)
        dp = [[False] * (p_len + 1) for _ in range(s_len + 1)]

        # If both strings are empty, then they match.
        dp[0][0] = True

        # If p is not empty, but s is empty, then we can only match if the first character of p is '*'.
        for j in range(1, p_len + 1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2]
        # If s is not empty, but p is empty, then we can't match.
        for i in range(1, s_len + 1):
            dp[i][0] = False

        # If both s and p are not empty, then we have two options.
        for i in range(1, s_len + 1):
            for j in range(1, p_len + 1):
                # If the current character of p is '*', then we can either ignore the '*' and move to the next character of p, or we can use the '*' to match the current character of s and move to the next character of s.
                if p[j-1] == '*':
                    dp[i][j] = dp[i][j-2] or (dp[i-1][j] and p[j-2] in {s[i-1], '.'})
                # If the current character of p is not '*', then we must match the current characters of s and p, and move to the next character of both s and p.
                else:
                    dp[i][j] = dp[i-1][j-1] and p[j-1] in {s[i-1], '.'}
        return dp[s_len][p_len]
        
