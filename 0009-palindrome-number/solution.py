class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        Determine if a number is a palindrome by converting it to a string and
        comparing it to the reversed string.

        :param x: The number to check
        :return: True if it is a palindrome, False otherwise
        """
        # Convert the number to a string
        data = str(x)

        # Reverse the string
        reversed_data = data[::-1]

        # Check if the reversed string is equal to the original string
        # If it is, then the number is a palindrome
        return data == reversed_data
