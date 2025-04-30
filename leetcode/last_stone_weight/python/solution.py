import heapq


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags: heap
        """
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            smashed_stone = heapq.heappop(stones) - heapq.heappop(stones)
            if smashed_stone:
                heapq.heappush(stones, smashed_stone)

        return -heapq.heappop(stones) if stones else 0


print(Solution().lastStoneWeight([1]) == 1)
print(Solution().lastStoneWeight([1, 1]) == 0)
print(Solution().lastStoneWeight([2, 7, 4, 1, 8, 1]) == 1)