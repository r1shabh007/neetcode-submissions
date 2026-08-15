class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        stacklen = 0
        matching = {")" : "(", "}" : "{", "]" : "["}
        for i in s:
            if i in matching:
                if stacklen > 0 and stack[-1] == matching[i]:
                    stack.pop()
                    stacklen -= 1
                    continue
            stack.append(i)
            stacklen += 1
        return True if not stack else False