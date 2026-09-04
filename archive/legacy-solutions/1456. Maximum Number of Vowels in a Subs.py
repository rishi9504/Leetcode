# 1456. Maximum Number of Vowels in a Substring of Given Length
# Solved
# Medium

# Given a string s and an integer k, 
# return the maximum number of vowel letters in any substring of s with length k.

# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # sliding window
        ans=0
        c=0
        v="aeiou"
        for i,j in enumerate(s):
            if i>=k:
                if s[i-k] in v:
                    c-=1
            if s[i] in v:
                c+=1
            ans = max(c,ans)
        return ans                
        