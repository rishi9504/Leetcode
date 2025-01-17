class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Finds the longest common prefix among the given list of strings.

        Example: ["flower", "flow", "flight"] returns "fl", as that is the longest
        common prefix to all three strings.

        :param strs: The list of strings to search for the common prefix.
        :return: The longest common prefix, or an empty string if no common
                 prefix exists.
        """
        if not strs:
            # If the list is empty, there is no common prefix, so return an empty
            # string.
            return ''

        # Sort the list of strings. This is useful because it allows us to find
        # the common prefix by comparing the first and last strings.
        strs.sort()

        # Take the first and last strings from the sorted list. These will be the
        # strings with the most and least characters in common, respectively.
        first = strs[0]
        last = strs[-1]

        # Start at the first character of both strings, and keep going until
        # either the end of the first string or the end of the last string is
        # reached, or until the characters at the current position are not
        # equal.
        i = 0
        while i < len(first) and i < len(last) and first[i] == last[i]:
            # If the characters are equal, move on to the next characters.
            i += 1

        # Return the common prefix, which is the substring of the first string
        # from the beginning to the last common character.
        return first[:i]
