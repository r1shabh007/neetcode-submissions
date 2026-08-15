class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {")" : "(", "}" : "{", "]" : "["}
        for i in s:
            if i in matching:
                if stack and stack[-1] == matching[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False