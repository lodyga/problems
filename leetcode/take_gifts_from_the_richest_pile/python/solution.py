import heapq


class Solution:
    def pickGifts(self, gifts: list[int], k: int) -> int:
        """
        Time complexity: O(n + klogn)
        Auxiliary space complexity: O(n)
        Tags:
            DS: heap
            A: iteration
        """
        gift_heap = [-gift for gift in gifts]
        heapq.heapify(gift_heap)

        for _ in range(k):
            gift = -heapq.heappop(gift_heap)
            heapq.heappush(gift_heap, -int(gift**0.5))

        return -sum(gift_heap)


print(Solution().pickGifts([25, 64, 9, 4, 100], 4) == 29)
print(Solution().pickGifts([1, 1, 1, 1], 4) == 4)
