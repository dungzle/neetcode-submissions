class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        max_profit = 0
        while left < len(prices) and right < len(prices):
            max_profit = max(max_profit, prices[right] - prices[left])
            if prices[left] >= prices[right]:
                left = right
                right += 1
            else:
                right += 1
        return max_profit