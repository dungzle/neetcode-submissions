class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        left = 0
        unique = set()
        max_count = 1
        for right in range(len(s)):
            while s[right] in unique:
                unique.remove(s[left])
                left += 1
            unique.add(s[right])
            max_count = max(max_count, right - left + 1)
        return max_count