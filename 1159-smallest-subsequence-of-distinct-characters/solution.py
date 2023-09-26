class Solution:
    def smallestSubsequence(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] in stack:
                continue
            if not stack or (ord(s[i]) > ord(stack[-1])):
                stack.append(s[i])
            elif ord(s[i]) < ord(stack[-1]):
                if stack[-1] not in s[i:]: 
                    stack.append(s[i])
                else:
                    while stack and ord(s[i]) <= ord(stack[-1]):
                        if stack[-1] not in s[i:]:
                            break
                        stack.pop()
                    stack.append(s[i])

        return "".join(stack)
        
