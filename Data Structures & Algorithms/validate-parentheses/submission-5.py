class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_brackets = set(['[', '{', '('])
        close_brackets = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for c in s:
            if c in open_brackets:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                last = stack.pop()
                if last != close_brackets[c]:
                    return False
        if len(stack) > 0:
            return False
        return True