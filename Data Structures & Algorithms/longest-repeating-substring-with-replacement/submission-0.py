class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        max_count = 0
        left = 0
        counts = defaultdict(int)
        for right in range(len(s)):
            counts[s[right]] += 1
            max_count = max(counts[s[right]], max_count)

            while (right - left + 1 - max_count > k):
                counts[s[left]] -= 1
                left += 1

            result = max(result, right - left + 1)
        

        return result