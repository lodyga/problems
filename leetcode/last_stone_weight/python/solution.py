import heapq


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags:
            DS: heap
            A: iteration
        """
        stone_heap = [-stone for stone in stones]
        heapq.heapify(stone_heap)

        while len(stone_heap) > 1:
            stone = heapq.heappop(stone_heap) - heapq.heappop(stone_heap)
            
            if stone:
                heapq.heappush(stone_heap, stone)

        return -stone_heap[0] if stone_heap else 0


print(Solution().lastStoneWeight([2, 7, 4, 1, 8, 1]) == 1)
print(Solution().lastStoneWeight([1]) == 1)
print(Solution().lastStoneWeight([1, 1]) == 0)
