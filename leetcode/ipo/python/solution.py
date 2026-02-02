import heapq


class Solution:
    def findMaximizedCapital(self, project_count: int, capital: int, profits: list[int], capital_list: list[int]) -> int:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags:
            DS: heap
            A: greedy
        """
        # min-heap((capital, profit), )
        project_heap = list(zip(capital_list, profits))
        heapq.heapify(project_heap)

        # max-heap((-profit), )
        profit_heap = []

        for _ in range(project_count):
            while project_heap and project_heap[0][0] <= capital:
                _, profit = heapq.heappop(project_heap)
                heapq.heappush(profit_heap, -profit)

            if not profit_heap:
                break

            capital -= heapq.heappop(profit_heap)

        return capital


print(Solution().findMaximizedCapital(2, 0, [1, 2, 3], [0, 1, 1]) == 4)
print(Solution().findMaximizedCapital(3, 0, [1, 2, 3], [0, 1, 2]) == 6)
print(Solution().findMaximizedCapital(1, 0, [1, 2, 3], [1, 1, 2]) == 0)
