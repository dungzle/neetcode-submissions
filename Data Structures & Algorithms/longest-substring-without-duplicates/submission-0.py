class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        left = 0
        right = 1
        unique = set([s[left]])
        max_count = 1
        while right < len(s):
            if s[right] in unique:
                while s[right] in unique:
                    unique.remove(s[left])
                    left += 1
                unique.add(s[right])
            else:
                unique.add(s[right])
            max_count = max(max_count, right - left + 1)
            right += 1
        return max_count