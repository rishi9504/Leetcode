class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        Convert a string s into a zigzag pattern and return the resulting string.
        The string s is written in a zigzag pattern of numRows rows, and then read off row by row.
        """
        if numRows == 1 or numRows >= len(s):
            return s

        """
        Initialize a list of empty lists, one for each row in the zigzag pattern.
        The index into this list will be the row number, and the list at that index
        will contain the characters in that row.
        """
        rows = [[] for _ in range(numRows)]

        """
        Initialize the index and direction. The index is the row number where the
        current character should go, and the direction is the direction that the
        index should move after the character is added to the appropriate row.
        """
        idx, d = 0, 1

        """
        Loop over the characters in the string.
        """
        for char in s:
            """
            Add the character to the appropriate row.
            """
            rows[idx].append(char)
            """
            If the index is 0, then we are at the first row, and the direction should
            be set to 1, so that the next character will be placed in the second row.
            If the index is equal to the number of rows minus one, then we are at the
            last row, and the direction should be set to -1, so that the next character
            will be placed in the second to last row.
            """
            if idx == 0:
                d = 1
            elif idx == numRows - 1:
                d = -1
            """
            Increment the index by the direction.
            """
            idx += d

        """
        Join the characters in each row together into a single string.
        """
        for i in range(numRows):
            rows[i] = ''.join(rows[i])

        """
        Join the strings together into a single string, with the first row first,
        the second row second, and so on.
        """
        return ''.join(rows)
