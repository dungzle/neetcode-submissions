class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_brackets = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for c in s:
            if c in close_brackets:
                if len(stack) == 0:
                    return False
                last = stack.pop()
                if last != close_brackets[c]:
                    return False
            else:
                stack.append(c)
        if len(stack) > 0:
            return False
        return True