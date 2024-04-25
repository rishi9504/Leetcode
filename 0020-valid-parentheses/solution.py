class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        m = {
            ')':'(',
            ']':'[',
            '}':'{',
        }
        for c in s:
            if c not in m:
                stack.append(c)
            else:
                if stack and m[c] == stack.pop():
                    continue
                return False
                
        return False if stack else True
