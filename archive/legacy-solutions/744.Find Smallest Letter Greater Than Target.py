# 744. Find Smallest Letter Greater Than Target
# Solved
# Easy
# Topics

# You are given an array of characters letters that is sorted in non-decreasing order, and a character target.
# There are at least two different characters in letters.

# Return the smallest character in letters that is lexicographically greater than target. 
# If such a character does not exist, return the first character in letters.

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        """
        This function takes a sorted list of characters and a target character as input.
        It returns the smallest character in the list that is lexicographically greater than the target.
        If such a character does not exist, it returns the first character in the list.

        Parameters
        ----------
        letters : List[str]
            A sorted list of characters.
        target : str
            The target character.

        Returns
        -------
        str
            The smallest character in the list that is lexicographically greater than the target.
        """
        for c in letters:
            if ord(c) >ord(target):
                return c
        return letters[0]