class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        if len(s)==1:
            return 1    

        
        # if string length is more than 2
        maxLength = 0
        visited = [False] * 256

        # left and right pointer of sliding window
        left, right = 0, 0
        while right < len(s):

            # if character is visited
            if visited[ord(s[right])]:

                # The left pointer moves to the right while
                # marking visited characters as false until the
                # repeating character is no longer part of the
                # current window.
                while visited[ord(s[right])]:

                    visited[ord(s[left])] = False
                    left += 1

            visited[ord(s[right])] = True

            # The length of the current window (right - left + 1)
            # is calculated and the answer is updated accordingly.
            maxLength = max(maxLength, right - left + 1)
            right += 1

        return maxLength    
        
