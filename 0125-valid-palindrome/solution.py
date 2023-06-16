class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == " ":
            return True
        else:
            filter = ''.join([i.lower() for i in s if i.isalnum()])
            return filter == filter[::-1]

