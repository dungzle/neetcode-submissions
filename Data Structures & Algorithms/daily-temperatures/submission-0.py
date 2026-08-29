class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                t_l, i_l = stack.pop()
                result[i_l] = i - i_l
            stack.append([t, i])
        return result