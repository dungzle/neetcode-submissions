class TimeMap:

    def __init__(self):
        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemap:
            self.timemap[key] = [(value, timestamp)]
        else:
            self.timemap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if len(self.timemap) == 0 or key not in self.timemap:
            return ""
        curr = self.timemap[key]
        left = 0
        right = len(curr) - 1
        while left <= right:
            mid = (left + right) // 2
            if curr[mid][1] <= timestamp:
                res = curr[mid][0]
                left = mid + 1
            else:
                right = mid - 1
        return res

        
