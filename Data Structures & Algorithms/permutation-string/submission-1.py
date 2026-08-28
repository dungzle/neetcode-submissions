class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_count = Counter(s1)
        left = 0
        right = len(s1)
        while right <= len(s2):
            s2_count = Counter(s2[left:right])
            if (s1_count == s2_count):
                return True
            left += 1
            right += 1
        return False