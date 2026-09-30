class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        digits = []
        res = 0
        for i in tokens:
            if i.isnumeric() or i[1:].isnumeric():
                digits.append(int(i))
            else:
                a = digits.pop()
                b = digits.pop()
                if i == "+":
                    digits.append(b + a)
                elif i == "-":
                    digits.append(b - a)
                elif i == "*":
                    digits.append(b * a)
                else: # i == "/":
                    digits.append(int(b / a))
        return digits[0]