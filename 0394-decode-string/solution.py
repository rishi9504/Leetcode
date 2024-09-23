class Solution:
    def decodeString(self, s: str) -> str:
        stack = []  
        current_string = "" 
        k = 0 
        
        for char in s:
            if char.isdigit():
                k = k * 10 + int(char)
            elif char == '[':
                stack.append((current_string, k))
                current_string = ""
                k = 0
            elif char == ']':
                prev_string, repeat_count = stack.pop()
                current_string = prev_string + current_string * repeat_count
            else:
                current_string += char
        return current_string

