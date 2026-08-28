class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = defaultdict(list)
        for i in range(len(nums)):
            num_dict[nums[i]].append(i)
        for num in nums:
            temp = target - num
            if temp in num_dict:
                if temp == num and len(num_dict[num]) > 1:
                    return [num_dict[num][0], num_dict[num][1]]
                elif temp != num:
                    return [num_dict[num][0], num_dict[temp][0]]
        return []