class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        lr_product = [0] * n
        rl_product = [0] * n
        lr_product[0] = nums[0]
        rl_product[n - 1] = nums[-1]
        for i in range(1, n):
            lr_product[i] = lr_product[i - 1] * nums[i]
        for i in range(n - 2, -1, -1):
            rl_product[i] = rl_product[i + 1] * nums[i]
        result[0] = rl_product[1]
        result[n - 1] = lr_product[n - 2]
        for i in range(1, n - 1):
            result[i] = lr_product[i - 1] * rl_product[i + 1]
        return result