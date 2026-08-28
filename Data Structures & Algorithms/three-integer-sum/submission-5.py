class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)

        result = []
        for i in range(len(nums) - 2):
            if sorted_nums[i] > 0:
                break
            if i > 0 and sorted_nums[i] == sorted_nums[i-1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                three_sum = sorted_nums[i] + sorted_nums[left] + sorted_nums[right]
                if three_sum < 0:
                    left += 1
                elif three_sum > 0:
                    right -= 1
                else:
                    result.append([sorted_nums[i], sorted_nums[left], sorted_nums[right]])
                    left += 1
                    right -= 1
                    while left < right and sorted_nums[left] == sorted_nums[left - 1]:
                        left += 1
                    while left < right and sorted_nums[right] == sorted_nums[right + 1]:
                        right -= 1

        return result
