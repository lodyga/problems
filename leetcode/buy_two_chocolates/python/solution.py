import heapq


class Solution:
    def buyChoco(self, prices: list[int], money: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: heap
        """
        heapq.heapify(prices)
        two_chocks = heapq.heappop(prices) + heapq.heappop(prices)
        leftover = money - two_chocks

        return leftover if leftover >= 0 else money


print(Solution().buyChoco([1, 2, 2], 3), 0)
print(Solution().buyChoco([3, 2, 3], 3), 3)