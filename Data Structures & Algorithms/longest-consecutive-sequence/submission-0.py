class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        visited = set()
        max_count = 0
        for num in nums:
            if num in visited:
                continue
            count = 1
            curr = num + 1
            while curr in set_nums:
                visited.add(curr)
                curr += 1
                count += 1
            if (max_count < count):
                max_count = count
        return max_count

