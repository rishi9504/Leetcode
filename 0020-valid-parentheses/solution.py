class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}  # Mapping of closing to opening parentheses

        for char in s:
            if char in mapping:  # Closing parenthesis
                if not stack or stack.pop() != mapping[char]:
                    return False
            else:
                stack.append(char)  # Opening parenthesis

        return not stack  # Return True if stack is empty, else False
