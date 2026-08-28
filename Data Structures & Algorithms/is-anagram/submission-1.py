class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_count = Counter(s)
        t_count = Counter(t)
        if len(s_count) != len(t_count):
            return False
        for key in s_count:
            if key not in t_count or s_count[key] != t_count[key]:
                return False
        return True