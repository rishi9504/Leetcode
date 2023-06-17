class Solution:
    def isPalindrome(self, x: int) -> bool:
        data = str(x)
        return data == data[::-1]
