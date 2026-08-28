class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        max_count = 0
        for num in nums:
            if num - 1 not in set_nums:
                count = 1
                curr = num
                while curr + 1 in set_nums:
                    curr += 1
                    count += 1
                if (max_count < count):
                    max_count = count
        return max_count

