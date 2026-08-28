class MinStack:

    def __init__(self):
        self.stack = []
        self.min_val = None

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_val is None or self.min_val > val:
            self.min_val = val

    def pop(self) -> None:
        if len(self.stack) == 0:
            return
        to_remove = self.stack[-1]
        self.stack.pop()
        if to_remove == self.min_val and len(self.stack) > 0:
            self.min_val = min(self.stack)
        elif len(self.stack) == 0:
            self.min_val = None

    def top(self) -> int:
        if len(self.stack) == 0:
            return None
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_val
