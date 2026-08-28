import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        count_heap = [(-value, key) for key, value in count.items()]
        heapq.heapify(count_heap)
        results = []
        for i in range(k):
            if len(count_heap) == 0:
                return
            results.append(heapq.heappop(count_heap)[1])
        return results