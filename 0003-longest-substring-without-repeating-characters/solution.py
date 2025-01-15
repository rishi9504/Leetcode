class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        

# This code calculates the length of the longest substring without repeating characters in a given string `s`. It uses a sliding window approach with two pointers (`left` and `right`) and a boolean array `visited` to keep track of characters that have been seen. The `maxLength` variable stores the maximum length of a substring without repeating characters found so far.
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
        
