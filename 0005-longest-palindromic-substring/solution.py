class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # We're going to iterate through all possible centres of the palindrome
        # and check the longest palindrome that can be formed from each centre.
        # The longest palindrome will be the one that has the longest length.

        # Create list of 2n-1 possible centres, each letter and between each pair
        # even indices represent letters, odd represent between letters
        # start with middle index that potentially creates longest palindrome
        centres = [len(s) - 1]
        for diff in range(1, len(s)):  # build list of indices from long to short
            centres.append(centres[0] + diff)
            centres.append(centres[0] - diff)

        # Initialize the longest palindrome
        longest = ""

        for centre in centres:

            # If the remaining length of the string to be checked is
            # less than or equal to the length of the longest palindrome
            # found so far, break and return the longest palindrome.
            # This is an optimization to avoid checking unnecessary cases.
            if (min(centre + 1, 2 * len(s) - 1 - centre) <= len(longest)):
                break

            # Check if the centre is between two letters (odd index)
            # or is a letter (even index)
            if centre % 2 == 0:
                # left and right are one position away from the centre
                left, right = (centre // 2) - 1, (centre // 2) + 1
            else:
                # left and right are on the same position as the centre
                left, right = centre // 2, (centre // 2) + 1

            # Check if the letters to the left and right of the centre
            # are the same. If they are, expand outwards to find the longest
            # palindrome.
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # left and right are now beyond the ends of the substring

            # If the length of the palindrome is longer than the longest found
            # so far, update the longest palindrome.
            if right - left - 1 > len(longest):
                longest = s[left + 1:right]

        return longest
        
