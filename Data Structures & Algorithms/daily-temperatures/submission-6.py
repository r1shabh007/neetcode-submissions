class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                index = stack.pop()
                res[index] = i - index
            stack.append(i)
        return res