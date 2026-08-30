class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        k = None
        while left <= right:
            mid = (left + right) // 2
            total = 0
            for p in piles:
                total += math.ceil(p / mid)
            if total <= h:
                if k is None or k > mid:
                    k = mid
                right = mid - 1
            if total > h:
                left = mid + 1
            
        return k
            